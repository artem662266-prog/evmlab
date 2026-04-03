class Solution:
    def isValid(self, s):
        stack = []  #стек для открытых скобок

        for char in s:
            if char in "({[":
                stack.append(char)  #кладем открывающую скобку
            else:  
                if not stack:
                    return False 
                top = stack.pop() 
                if (top == '(' and char != ')') or \
                   (top == '[' and char != ']') or \
                   (top == '{' and char != '}'):
                    return False  

        return not stack
