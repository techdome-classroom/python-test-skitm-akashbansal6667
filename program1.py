def isValid(s: str) -> bool:
    
    leftSymbols = []

    for c in s:
        
        if c in ['(', '{', '[']:
            leftSymbols.append(c)
    
        elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
            leftSymbols.pop()
        elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
            leftSymbols.pop()
        elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
            leftSymbols.pop()
        # If none of the valid symbols is encountered
        else:
            return False
    return leftSymbols == []
    



  

