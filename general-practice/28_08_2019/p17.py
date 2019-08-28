def modpow(b, e, m):
    r = 1
    while e > 0:
        if e & 1:
            r = (r * b) % m
        b = (b * b) % m
        e = e >> 1
    return r

def powersum(n, m):
    s = 0
    for i in range(1, n + 1):
        s+= modpow(i, i, m)
        s%= m
    return s

if __name__ == '__main__':
    modulo = 10000000000
    number = int(input())
    
    print(powersum(number, modulo))
