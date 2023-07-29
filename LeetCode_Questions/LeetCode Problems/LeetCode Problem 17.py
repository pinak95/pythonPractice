class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        digits_to_characters = {"2" : "abc",
                                "3" : "def",
                                "4" : "ghi",
                                "5" : "jkl",
                                "6" : "mno",
                                "7" : "pqrs",
                                "8" : "tuv",
                                "9" : "wxyz"}

        def backtrack(i, temp_ans):
            if len(temp_ans) == len(digits):
                answer.append(temp_ans)
                return
            for c in digits_to_characters[digits[i]]:
                backtrack(i + 1, temp_ans + c)
        if digits:
            backtrack(0, "")
        return answer