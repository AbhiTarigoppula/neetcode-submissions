class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {')' : '(', ']' : '[', '}' : '{'}


        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                else:
                    top_element = stack.pop()
                    if top_element != map[c]:
                        return False

        return len(stack) == 0        