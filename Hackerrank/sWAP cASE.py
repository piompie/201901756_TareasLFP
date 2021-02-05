#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    invertido=''
    for caracter in s:
        if caracter.upper()==caracter:
            invertido=invertido + caracter.lower()
        else:
            invertido=invertido + caracter.upper()
    return invertido

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
