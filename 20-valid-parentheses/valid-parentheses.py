class Solution:
    def isValid(self, s: str) -> bool:
        valid_inputs = {'(': ')', '{': '}', '[': ']'}
        inputs = []
        for i in s:
            if i in valid_inputs:
                inputs.append(i)
            else:
                if len(inputs) == 0:
                    return False
                if i != valid_inputs[inputs.pop()]:
                    return False
        if len(inputs) != 0:
            return False 
        return True
