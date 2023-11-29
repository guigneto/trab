#Aluno: Guilherme Gomes de Faria Neto

import pickle

def verificaMutuos(conexoes,user1,user2):
    gostou1, gostaramDele1, mutuos1 = conexoes[user1]
    gostou2, gostaramDele2, mutuos2 = conexoes[user2]

    if user1 in gostaramDele2 and user1 in gostou2:
        return True
    if user2 in gostaramDele1 and user2 in gostou1:
        return True


def juntaMutuos(conexoes,user1,user2):
    gostou, gostaram, mutuos = conexoes[user1]
    gostou2, gostaram2, mutuos2 = conexoes[user2]

    gostaram.remove(user2)
    gostou.remove(user2)

    gostaram2.remove(user1)
    gostou2.remove(user1)

    mutuos.append(user2)
    mutuos2.append(user1)


def geraConexoes():

    with open("backup.bin", "rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
        historico = pickle.load(f)
    f.close()

    for (user1,user2) in historico:

        gostou1, gostaram1, mutuos1 = conexoes[user1]
        gostou2, gostaram2, mutuos2 = conexoes[user2]

        if user2 not in gostou1:
            gostou1.append(user2)
        if user1 not in gostaram2:
            gostaram2.append(user1)

        if verificaMutuos(conexoes,user1,user2):
            juntaMutuos(conexoes,user1,user2)

    with open("dados.bin","wb") as j:
        pickle.dump(usuarios,j)
        pickle.dump(conexoes,j)
    j.close()

def main():
    geraConexoes()
    return 0
if __name__ == '__main__':
    main()