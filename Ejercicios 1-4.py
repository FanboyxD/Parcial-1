def Combinaciones(lista1,lista2):
    if isinstance(lista1,list)and(lista2,list):
        return combinaciones_aux(lista1,lista2)
    else:return "Error"
def combinaciones_aux(lista1,lista2):
    if lista1==[]and lista2==[]:
        return []
    elif(lista1[0])and(lista2[0]):
        return([lista1[0]+lista2[0]]+combinaciones_aux(lista1[1:],
                lista2[1:]))
    else:return combinaciones_aux(lista1[1:],lista2[1:])

def std(lista,avg):
    if isinstance(lista,list)and(avg,int):
        return std_aux(lista,avg)**(1/2)
    else: return "Error"
def std_aux(lista,avg):
    if lista==[]:
        return 0
    elif(lista[0]):
        return ((lista[0]-avg)**2/len(lista)-1)+std_aux(lista[1:],avg)
    else: return std_aux(lista[1:],avg)

def zScore(lista,S,avg):
    if isinstance(lista,list)and(avg,int)and(S,int):
        return zscore_aux(lista,S,avg)
    else: return "Error"
def zscore_aux(lista,S,avg):
    if lista==[]:
        return []
    elif(lista[0]):
        return [(lista[0]-avg)/S]+zscore_aux(lista[1:],S,avg)
    else:return zscore_aux(lista[1:],S,avg)

def rScore(lista1,lista2):
    if isinstance (len(lista1)==len(lista2)):
        return rscore_aux(lista1,lista2)/len(lista1)-1
    else:return "Error"
def rscore_aux(lista1,lista2):
    if lista1==[] and lista2==[]:
        return 0
    elif (lista1[0])and(lista2[0]):
        return (lista1[0]*lista2[0])+rscore_aux(lista1[1:],lista2[1:])
    else:return rscore_aux(lista1[1:],lista2[1:])
