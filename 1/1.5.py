
def check_off_one(a,b):
    diff_size = abs(len(a) - len(b))
    if diff_size > 1:
        return False

    b_idx = 0
    diff_chars = 0
    for c in a:
        cur_b = b[b_idx] if b_idx < len(b) else cur_b
        if diff_chars > 1:
            return False
        if c != cur_b:
            diff_chars += 1
        else:
            b_idx += 1
    return True

print(check_off_one('px', 'pxsc'))