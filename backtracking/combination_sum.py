class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(cand, index, current_sum, res):
            if target == current_sum:
                result.append(res[:])

            for i in range(index, len(cand)):
                if current_sum > target:
                    return
                res.append(cand[i])
                backtrack(cand, i, current_sum + cand[i], res)
                res.pop()

        backtrack(candidates, 0, 0, [])

        return result
