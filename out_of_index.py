class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    	# 要对输入的参数进行判断，有时候可能为空集
    	# 注意边际等特殊情况
        if len(strs) ==0:
            return ''
        elif len(strs) ==1:
            return strs[0]
        a = strs[0]
        k = True
        n = 0
        for i in range(len(a)):
            n = i
            for j in range(len(strs)-1):
                if len(strs[j+1]) == i:
                    k = False
                    break
                else:
                    if strs[j+1][i] != a[i]:
                        k =False
                        break
            if not k :
                break
        
        if n == 0 and not k:
            return ''
        elif k:
            return a
        else:
            return a[:n]
    
