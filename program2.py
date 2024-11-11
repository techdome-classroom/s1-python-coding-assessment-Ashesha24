def decode_message(s: str, p: str) -> bool:
    s_index = 0
    p_index = 0
    
    while p_index < len(p):
        if p[p_index] == '*':
            p_index += 1
            if p_index == len(p):
                return True
            while s_index < len(s) and (s[s_index] != p[p_index] or p[p_index] == '?'):
                s_index += 1
            if s_index == len(s):
                return False
        elif p[p_index] == '?':
            s_index += 1
            p_index += 1
        else:
            if s_index >= len(s) or s[s_index] != p[p_index]:
                return False
            s_index += 1
            p_index += 1
return False
