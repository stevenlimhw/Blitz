class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_ptr = len(a) - 1
        b_ptr = len(b) - 1
        carry = 0
        res = ""

        while a_ptr >= 0 or b_ptr >= 0:
            lhs = 0
            rhs = 0
            if a_ptr >= 0:
                lhs = int(a[a_ptr])
            if b_ptr >= 0:
                rhs = int(b[b_ptr])
            sum = lhs + rhs + carry
            res = str(sum % 2) + res
            carry = sum // 2

            a_ptr -= 1
            b_ptr -= 1
        
        if carry == 1:
            res = "1" + res
        
        return res
