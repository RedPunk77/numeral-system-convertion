print("convert numeral to required num.system OR convert numeral to decimal num.system:")
first_or_second = input("choose - write '1' to choose 1st and '2' to choose 2nd accordingly: ")
if int(first_or_second) == 1:
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
        print(tmp1, "(10) = ", *A, "(", m, ")", sep='')                                 //Code changes are continued! ;
                                                                                        //Conact me: makarkosenko77@gmail.com or write on Telegram - https://t.me/kosenko_makaron

    n = int(input("numeral in decimal numeral system: "))
    k = int(input("this numeral in required numeral system: "))
    if k > 26:
        exit()
    convert_to_another_num_system(n, k)

elif int(first_or_second) == 2:

    def from_num_system_to_decimal_num_system(s, k):
        s = [s for s in list(s)]
        special_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_list = list(special_list)
        sum = 0
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = special_list.index(s[i])
            sum += int(s[i]) * (k ** (len(s) - 1 - i))
        for i in range(len(s)):
            if int(s[i]) >= 10:
                s[i] = special_list[s[i]]
        print(*s, "(", n, ") = ", sum, "(10)", sep='')


    num = input("convert num: ")
    print("from ", end='')
    n = int(input())
    print("numeral system to decimal numeral system: ")
    from_num_system_to_decimal_num_system(num, n)

else:
    exit()
