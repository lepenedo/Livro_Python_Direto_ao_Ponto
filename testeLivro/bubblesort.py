'''Bubblesort é um algoritimo clássico de ordenação de sequência. O Bubblesort parte do principio de 
que se uma sequência está desordenada, deve conter dois elementos adjacentes que estão fora de ordem,
com isso em conta, o algoritimo repetidamente passa pela sequência trocando a posição de elementos
fora de ordem, até que não haja mais nenhum elemento fora de desordenado '''


valores = [2,3,7,4,1,6,5,8,9,0]

desordenado = True

while desordenado:
    desordenado = False
    for i in range(len(valores)-1):
        if valores[i] > valores[i+1]:
            valores[i], valores[i+1] = valores[i+1],valores[i]
            desordenado = True
            print(valores)