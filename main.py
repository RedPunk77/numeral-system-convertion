def convert_to_another_num_system(n, m):
    s = '0123456789ABCDEFGHKLMNOPQRSTVWXYZ'
    alphabet = list(s)
    this_alphabet = alphabet[:m]
    tmp1 = n
    A = list()
    while n >= m:
        tmp2 = n % m
        if m > 10:
            tmp2 = this_alphabet[tmp2]
        A.append(tmp2)
        n //= m
    if n < m:
        if m > 10:
            n = this_alphabet[n]
        A.append(n)
    A.reverse()
    print(tmp1, "(10) = ", *A, "(", m, ")", sep='')


n = int(input("numeral in decimal numeral system: "))
k = int(input("this numeral in required numeral system: "))
if k > 26:
    exit()
convert_to_another_num_system(n, k)
