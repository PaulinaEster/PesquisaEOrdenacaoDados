# Altere o Algoritmo Bolha, estudado na aula passada, para que o elemento desça ao invés de subir no vetor.


def bubbleSort(v):
    for i in range(len(v)-1,0,-1):
        for j in range(i):
            if v[j]>v[j+1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp
v = [71, 5, 14, 82]
bubbleSort(v, " Bubble invertido")
print(v)

def bubbleSortNormal(v): 
    for i in range(len(v)-1,0,-1):
        for j in range(i):
            if v[j]<v[j+1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp

v = [71, 5, 14, 82]
bubbleSortNormal(v)
print(v , " Bubble Normal")