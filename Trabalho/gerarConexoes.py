import pickle

def geraConexoes():

    with open("backup.bin", "rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
        historico = pickle.load(f)
    f.close()

    for i in historico:
        deuLike = i[0]
        recebeuLike = i[1]
        # print(deuLike)
        # print(recebeuLike)
        gostou1, gostaram1, mutuos1 = conexoes[deuLike]
        gostou2, gostaram2, mutuos2 = conexoes[recebeuLike]

        if recebeuLike not in gostou1:
            gostou1.append(recebeuLike)
        if deuLike not in gostaram2:
            gostaram2.append(deuLike)

    for users in conexoes:
        gostou, gostaram, mutuos = conexoes[users]
        for i in gostou:
            if i in gostaram:
                gostou.remove(i)
                gostaram.remove(i)
                mutuos.append(i)

    with open("dados.bin","wb") as j:
        pickle.dump(usuarios,j)
        pickle.dump(conexoes,j)
    j.close()
geraConexoes()

def main():
    geraConexoes()
    return 0
if __name__ == '__main__':
    main()