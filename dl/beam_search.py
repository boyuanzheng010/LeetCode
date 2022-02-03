import torch

def best_k(self, Beam, k, encoder_output, x_padding_masks, x, len_oovs):
    """Get best k tokens to extend the current sequence at the current time step.
    """
    # use decoder to generate vocab distribution for the next token
    x_t = torch.tensor(Beam.tokens[-1]).reshape(1, 1)
    x_t = x_t.to(self.DEVICE)

    # Get context vector from attention network.
    context_vector, attention_weights, coverage_vector = \
        self.model.attention(Beam.decoder_states,
                             encoder_output,
                             x_padding_masks,
                             Beam.coverage_vector)

    # Replace the indexes of OOV words with the index of OOV token
    # to prevent index-out-of-bound error in the decoder.

    p_vocab, decoder_states, p_gen = \
        self.model.decoder(replace_oovs(x_t, self.vocab),
                           Beam.decoder_states,
                           context_vector)

    final_dist = self.model.get_final_distribution(x,
                                                   p_gen,
                                                   p_vocab,
                                                   attention_weights,
                                                   torch.max(len_oovs))
    # Calculate log probabilities.
    log_probs = torch.log(final_dist.squeeze())
    # Filter forbidden tokens.
    # EOS token penalty. Follow the definition in
    # https://opennmt.net/OpenNMT/translation/beam_search/.
    log_probs[self.vocab.EOS] *= \
        config.gamma * x.size()[1] / len(Beam.tokens)
    log_probs[self.vocab.UNK] = -float('inf')
    # Get top k tokens and the corresponding logprob.
    topk_probs, topk_idx = torch.topk(log_probs, k)

    # Extend the current hypo with top k tokens, resulting k new hypos.
    best_k = [Beam.extend(x,
                          log_probs[x],
                          decoder_states,
                          coverage_vector) for x in topk_idx.tolist()]

    return best_k