
def m_into_n(m,n, i, j):
    msk = ~(~0 << (j-i)) << i
    n &= ~msk
    n |= m << i
    return n


N = int('1111111111', base=2)
N_bin = bin(N)

M = int('0000', base=2)
M_bin = bin(M)

result_bin = bin(m_into_n(M,N,2,6))

print('N: {},{} M: {},{} Out: {},{}'.format(N_bin, len(N_bin), M_bin, len(M_bin), result_bin, len(result_bin)))