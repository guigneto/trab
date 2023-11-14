import pickle

def printUsers(): #Motra usuarios no arquivo "teste.txt"
    with open("backup.bin", "rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
        d3 = pickle.load(f)
        d4 = pickle.load(f)
    with open("teste.txt","wt") as g:
        for user in usuarios:
            g.write(f'{user}:{usuarios[user]}\n')
        g.write("\n\n\n")
        for conex in conexoes:
            g.write(f'{conex}:{conexoes[conex]}\n')
        g.write("\n\n\n")
        g.write(f'{d3}')
        g.write(f'{d4}')
printUsers()
