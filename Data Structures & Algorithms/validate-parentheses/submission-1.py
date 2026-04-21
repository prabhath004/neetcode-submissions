class Solution:
    def isValid(self, s: str) -> bool:
        instack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                instack.append(c)
            else:
                if not instack:
                    return False
                top = instack.pop()
                if c == ']' and top != '[':
                    return False
                if c == '}' and top != '{':
                    return False   
                if c == ')' and top != '(':
                    return False
        return len(instack) == 0
        