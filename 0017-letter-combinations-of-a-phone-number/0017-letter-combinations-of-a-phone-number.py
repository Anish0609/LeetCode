class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        n=len(digits)

        keypad={"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        temp=[]
        res=[]

        def fun(idx):
            if idx==n :
                res.append("".join(temp))
                return
            
            for ch in keypad[digits[idx]] :
                temp.append(ch)
                fun(idx+1)
                temp.pop()


        fun(0)
        return res

            
        