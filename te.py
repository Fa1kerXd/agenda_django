def separate(string):
    texto = []

    for s in range(0, len(string), 2):
        par = string[s:s+2]
        print(par)
        if len(par) == 1:
            par += "_"
        texto.append(par)
    return texto 
     







def separate_not_slice(string):
    resultado = []
    par = ""

    for s in string:
        par += s

        if len(par) == 2:
            resultado.append(par)
            par = ""
    if len(par) == 1:
        resultado.append(par + "_")
    return resultado



print(separate("Augusto"))
print(separate_not_slice("Augusto"))