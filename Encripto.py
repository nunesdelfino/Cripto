MsgCripto = []

posKey = 0

Calc = 0

while(True):
    
    key = input("Digite uma chave com no mínimo 8 Caracteres contendo letras Maiuscula, Minusculas e Número: ")

    if(len(key) < 8):
        print("Senha inválida pois contém menos de 8 Caracteres")
    elif(not any(map(str.isdigit, key)) or not any(map(str.isdigit, key))):
        print("Senha inválida pois não contém números")
    elif(not any(map(str.isupper, key))):
        print("Senha inválida pois não contém letras maiusculas")
    elif(not any(map(str.islower, key))):
        print("Senha inválida pois não contém letras minusculas")
    else:
        break

PALAVRA = input("Digite uma mensagem para ser criptografada: ")

for posChar in range(len(PALAVRA)):

    if(posKey == len(key)):
        posKey = 0
         
    MsgCripto.append(ord(PALAVRA[posChar])+ord(key[posKey]))
    
    posKey+=1

with open('mensagem.txt', 'w', encoding = 'utf-8') as arquivo:
    for cod in MsgCripto:
        arquivo.write(str(cod) + ",")

