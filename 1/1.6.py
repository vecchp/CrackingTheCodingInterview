def compress_1(s):
    out_string = []
    if len(s) == 0:
        return None

    prev_c = s[0]
    count = 1
    
    for c in s[1:]:
        if c == prev_c:
            count += 1
        else:
            out_string.append(prev_c)
            out_string.append(str(count))
            count = 1
            prev_c = c

    out_string.append(prev_c)
    out_string.append(str(count))

    if len(out_string) < len(s):
        return ''.join(out_string)

    return s


print(compress_1('acccccccrrrc'))