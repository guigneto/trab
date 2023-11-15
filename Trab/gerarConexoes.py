import pickle

def printUsers(): #Motra usuarios no arquivo "teste.txt"
    with open("backup.bin", "rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
        l = pickle.load(f)
        cont = 0
    with open("teste.txt","wt") as g:
        for user in usuarios:
            g.write(f'{user}:{usuarios[user]}\n')
        g.write("\n\n\n")
        for conex in conexoes:
            g.write(f'{conex}:{conexoes[conex]}\n')
        g.write("\n\n\n")
        g.write(f'{l}\n')
        for i in l:
            if i[0] == "u00000000":
                cont += 1
        g.write(f"len(l):{len(l)}\n")
        g.write(f"{cont}")
#printUsers()

def verificaConexoes(d):
    for user in d:
        for i in d[user][0]:
            if i not in d[user][1]:
                return True
    return False

def geraConexoes():
    with open("backup.bin", "rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
        historico = pickle.load(f)

    for likes in historico:
        deuLike = likes[0]
        recebeLike = likes[1]
        if recebeLike not in conexoes[deuLike][0] and recebeLike not in conexoes[deuLike][0]:
            conexoes[deuLike][0].append(recebeLike)
            conexoes[recebeLike][1].append(deuLike)
    
    for user in conexoes:
        gostou = conexoes[user][0]
        gostaram = conexoes[user][1]
        mutuos = conexoes[user][2]
        for i in gostou:
            if i in gostaram:
                mutuos.append(i)
                gostou.remove(i)
                gostaram.remove(i)
    print(verificaConexoes(conexoes))
    with open("teste.txt","wt") as g:
        g.write(f"{usuarios}")
        g.write(f"{conexoes}")
    with open("dados.bin","wb") as b:
        pickle.dump(usuarios,b)
        pickle.dump(conexoes,b)
geraConexoes()
