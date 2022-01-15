class Solution:
    def isHappy(self, n: int) -> bool:
        # Set history to record whether the number has appeared
        history = set()
        history.add(n)

        # Function to calculate happy number
        def calculate_happy(num):
            sum_ = 0
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            else:
                if n in history:
                    return False
                history.add(n)