#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

lista = []

for i in range(N):
    instr = input().split()
    if instr[0] == 'insert':
        lista.insert(int(instr[1]),int(instr[2]))
    elif instr[0] == 'append':
        lista.append(int(instr[1]))
    elif instr[0] == 'pop':
        lista.pop()
    elif instr[0]=='print':
        print(lista)
    elif instr[0]=='remove':
        lista.remove(int(instr[1]))
    elif instr[0]=='sort':
        lista.sort()
    else:
        lista.reverse()

