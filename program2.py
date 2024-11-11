def decode_message(s: str, p: str) -> bool:
    s_index = 0
    p_index = 0
    star_index = -1
    match_index = -1

    while s_index < len(s):
        # If current characters match or pattern has a '?'
        if p_index < len(p) and (p[p_index] == s[s_index] or p[p_index] == '?'):
            s_index += 1
            p_index += 1
        # If pattern has a '*' (match any sequence)
        elif p_index < len(p) and p[p_index] == '*':
            star_index = p_index
            match_index = s_index
            p_index += 1
        # If there was a previous '*' and current character doesn't match
        elif star_index != -1:
            p_index = star_index + 1
            match_index += 1
            s_index = match_index
        else:
            return False

    # Check if remaining pattern is all '*'
    while p_index < len(p) and p[p_index] == '*':
        p_index += 1

    return p_index == len(p)

