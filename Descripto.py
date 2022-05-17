key = input("Digite a chave para descriptografar a mensagem: ")

with open('mensagem.txt', 'r', encoding = 'utf-8') as arquivo:
    MsgCripto = arquivo.read()

MsgCripto = MsgCripto.split(',')
MsgCripto.pop()

MsgTexto = []

posKey = 0

for posChar in range(len(MsgCripto)):

    if(posKey == len(key)):
        posKey = 0
         
    MsgTexto.append(chr(int(MsgCripto[posChar])-ord(key[posKey])))
    
    posKey+=1

print(''.join(MsgTexto))