def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        def check_noncoprime(a, b):
            while b != 0:
                a, b = b, a % b
            return a 

        def check_lcm(a, b):
            return abs(a * b) // check_noncoprime(a, b)
        
        stack = []

        for num in nums:
            stack.append(num)
            while len(stack) > 1 and check_noncoprime(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                lcm = check_lcm(a, b)
                stack.append(lcm)
        
        
        return stack