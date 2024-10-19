from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        start, end = 0, 0
        state = {}

        while end != len(fruits):
            state[fruits[end]] = state.get(fruits[end], 0) + 1

            while len(state) > 2:
                state[fruits[start]] -= 1
                if state[fruits[start]] == 0:
                    del state[fruits[start]]
                start += 1
            max_fruits = max(max_fruits, end - start + 1)
            end += 1

        return max_fruits
