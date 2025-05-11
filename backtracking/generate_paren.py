class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def gen(s, opened, close):
            if len(s) == 2 * n:
                result.append(s)
                return

            if opened < n:
                gen(s + "(", opened + 1, close)

            if close < opened:
                gen(s + ")", opened, close + 1)
        
        gen("", 0, 0)
        return result
