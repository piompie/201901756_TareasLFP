#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    lista=[]
    for _ in range(int(input())):
        name = input()
        score=float(input())
        lista.append([score,name])
    quitar=0
    for x in range(len(lista)):
        if lista[x][0]==min(lista)[0]:
            quitar=quitar+1 
    noprimeros=sorted(lista,reverse=False)[quitar:]
    quitar=0
    for x in range(len(noprimeros)):
        if noprimeros[x][0]!=noprimeros[0][0]:      
            quitar=quitar+1
    if quitar!=0:
        noprimeros=noprimeros[:-quitar]
    noprimeros=sorted(noprimeros,key=lambda x:x[1],reverse=False)
    for persona in noprimeros:
        print(persona[1])

