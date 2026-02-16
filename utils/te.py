from random import random, choice


choice_ = ["sim", "não", "nao", "nao"]
time = 0
limit = 5000


print("A probabilidade de cair no 0,005% vai nos dizer se vamos dar certo juntos.")
ch = choice(choice_)
while time < limit:
    time += 1
    if round(random(),3) == 0.015:
        print("Caiu nos 0,005%. Mas será que o destino quer isso?")
        if ch == 'nao':
            print(ch)
            print("SIM! O DESTINO QUER QUE A GENTE FIQUE JUNTOS")
            break
        else:
            print("NÃO! O DESTINO NÃO QUER QUE A GENTE FIQUE JUNTOS!")
    print(ch)
    print("NÃO VAMOS FICAR JUNTOS!")