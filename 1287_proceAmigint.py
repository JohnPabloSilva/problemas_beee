while True:
    try:
        n = list(input())
        print(n)
        if n[0]=='-':
            print('error')
        else:
            num, nao = '', False
            for i in n:
                if i.isdigit():
                    num += i
                elif i in 'Oo':
                    num += '0'
                elif i == 'l':
                    num += '1'
                elif i not in ' ,':
                    nao = True
                    break
            if nao or num == '':
                print('error')
            else:
                print(int(num))      
    except EOFError:
        break