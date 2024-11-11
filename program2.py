
                return False
        elif p[p_index] == '?':
            s_index += 1
            p_index += 1
        else:
            if s_index >= len(s) or s[s_index] != p[p_index]:
                return False
            s_index += 1
            p_index += 1
    
    return s_index == len(s)