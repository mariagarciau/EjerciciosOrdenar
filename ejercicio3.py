def minMax(lista):
    list_ord=[]
    list_rev=[]
    for numero in sorted(lista):
        list_ord.append(numero)
    min_=list_ord[0]
    for numero in reversed(list_ord):
        list_rev.append(numero)
    max_=list_rev[0]
    return min_,max_
