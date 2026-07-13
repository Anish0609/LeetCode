class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp=[]
        res=[]

        def brac(open,close,temp,res):
            if open==close==n :
                res.append("".join(temp))
                return 
            
            if open<n :
                temp.append("(")
                brac(open+1,close,temp,res)
                temp.pop()
            
            if close<open :
                temp.append(")")
                brac(open,close+1,temp,res)
                temp.pop()
        
        brac(0,0,temp,res)

        return res
            


        