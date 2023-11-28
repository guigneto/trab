#Aluno: Guilherme Gomes de Faria Neto

import pickle

def geraConexoes():

    with open("backup.bin", "rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
        historico = pickle.load(f)

    for user1, user2 in historico:

        gostou1, gostaram1, mutuos1 = conexoes[user1]
        gostou2, gostaram2, mutuos2 = conexoes[user2]

        if user2 not in gostou1:
            gostou1.append(user2)

        if user1 not in gostaram2:
            gostaram2.append(user1)

        if user1 in gostaram2 and user2 in gostaram1: #sempre vai fazer
            gostaram2.remove(user1)
            gostaram1.remove(user2)
            mutuos1.append(user2)
            mutuos2.append(user1)

    with open("dados.bin","wb") as j:
        pickle.dump(usuarios,j)
        pickle.dump(conexoes,j)

geraConexoes()

def main():
    geraConexoes()
    return 0
if __name__ == '__main__':
    main()