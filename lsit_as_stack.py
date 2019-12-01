class Solution:
    def isValid(self, s: str) -> bool:
        if s =='':
            return True
        if s[0] != '(' and s[0] != '[' and s[0] != '{':
            return False
        for i in range(len(s)):
            if s[i] =='(' or s[i] =='[' or s[i] =='{':
                a.append(s[i])
            # 只要内弹出，就都要丢进栈
            elif s[i] ==')':
                if a[-1]=='(':
                    a.pop()
                else:
                    a.append(s[i])
            elif s[i] ==']':
                if a[-1]=='[':
                    a.pop()
                else:
                    a.append(s[i])
               
            elif s[i] =='}':
                if a[-1]=='{':
                    a.pop()
                else:
                    a.append(s[i])
                
        if len(a)==0:
            return True
        else:
            return False

