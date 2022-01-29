"""
Sort together
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def compare_function(log):
            # Pick digit-log
            if log[-1].isnumeric():
                return (1,)
            iden, value = log.split(" ", 1)
            return (0, value, iden)

        return sorted(logs, key=compare_function)


"""
Split then sort
Merge
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Split based on letter and digit
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log[-1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        # sort the letter logs
        letter_logs.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        letter_logs.extend(digit_logs)
        # Merge all logs
        return letter_logs






