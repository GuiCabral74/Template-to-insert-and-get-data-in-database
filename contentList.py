arr = []

def retorna_dados():
  with open("dados.txt", "r+t", encoding="utf8") as arquivo:
    linhas = arquivo.readlines()
    arr = [x.strip().title() for x in linhas]

    print(arr)
    return(arr)
    
