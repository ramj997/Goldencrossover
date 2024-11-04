def is_valid_parentheses(s):
    stack = []
    # Map of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # If it’s an opening bracket
            stack.append(char)
        elif char in bracket_map:  # If it’s a closing bracket
            if not stack or stack.pop() != bracket_map[char]:  # Check matching
                return False
        else:
            # Ignore other characters (or handle error if only brackets are expected)
            return False
    return not stack  # Valid if stack is empty
print(is_valid_parentheses("([{}])"))  # Output: True

# st=input("enter :")
# print(is_valid_parentheses(st))

# Test cases
# print(is_valid_parentheses("()"))  # Output: True
# print(is_valid_parentheses("()[]{}"))  # Output: True
# print(is_valid_parentheses("(]"))  # Output: False
# print(is_valid_parentheses("([{}])"))  # Output: True
# print(is_valid_parentheses("[(])"))  # Output: False
