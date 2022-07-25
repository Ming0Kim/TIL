#220725

def dec_to_bin2(n):
    if n < 2:
        return str(n)
    return dec_to_bin2( n // 2 ) + dec_to_bin2( n % 2 )