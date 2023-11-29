#Aluno: Guilherme Gomes de Faria Neto

import pickle

def anterior(tupla, pivot):
    users,likes,cidade = tupla
    users2,likes2,cidade2 = pivot

    if cidade < cidade2: return True
    if cidade > cidade2: return False

    if likes > likes2: return True
    if likes < likes2:return False

    if users < users2: return True
    if users > users2 : return False

def qsort(l):
    if len(l) > 1:
        pivot = l[0]
        menores = []
        maiores= []
        for i in range(1, len(l)):
            if anterior(l[i],pivot):
                menores.append(l[i])
            else:
                maiores.append(l[i])
        return qsort(menores) + [pivot] + qsort(maiores)
    else:
        return l 
    
def estatisticas():
    l = []
    maior = ""
    
    with open("dados.bin","rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
    f.close()

    with open("top.txt","wt") as g:

        for users in usuarios:
            nome, cidade, nasc = usuarios[users]
            gostei, gostaram, mutuos = conexoes[users]
            likes = len(gostaram) + len(mutuos)
            l.append((users,likes,cidade))
        l = qsort(l)

        for i in l:
            user = i[0]
            nome = usuarios[user][0]
            cidade = i[2]
            if cidade != maior:
                maior = cidade
                g.write(f'{maior} {nome}\n')
        
    g.close()

    
def main():
    estatisticas()
    return 0
main()