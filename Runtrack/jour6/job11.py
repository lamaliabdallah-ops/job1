L = [7, 11, 42, 39, 2]

def augmenter_par_1(liste):
    for i in range(len(liste)):
        liste[i] += 1

augmenter_par_1(L)
print(L)  
