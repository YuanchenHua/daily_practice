class Solution:
    def reverse(self, x: int) -> int:
    	# 拿1进行向左位运算，再减1，就快速得到上限
    	# ~x 类似于 -x-1
        bound = (1 << 31) -1 if x > 0 else 1 << 31 
        y , res = abs(x),0
        while y != 0 :
        	# % 取余，相当于mod
            res  = res * 10 + y%10
            if res >  bound:
                return 0
            # 向下取整
            y = y//10
        if x < 0:
            res = -res
        return res 