lista=list()
maior=0
menor=9999999999999
i=0
for i in range(0,5):
     lista.append(int(input("Digite um valor: ")))
print(lista)

print(f'O maior numero é {maior} com posição: ',end='')
for i in range(0,5):
    if lista[i]==max(lista):
         print(i,end='')

print(f'\nO menor numero é {maior} com posição: ',end='')
for i in range(0,5):
    if lista[i]==min(lista):
         print(i,end='')
        




