#fazer um codigo que receba quantos numeros o usuario quiser e faça a media deles
print ('Maquina de fabricar a media de quantos numeros quiser')
X = float(input('Insira o primeiro numero:'))
Y = float(input('Insira o segundo numero:'))
num1 = X + Y
cont = 2
while True:
    resposta = int(input('Deseja inserir outro numero? (Digite 1 para sim e 2 para não)'))
    if resposta == 1:
        A = float(input('Escolha o proximo numero:'))
        cont += 1
        num1 += A       
    elif resposta == 2:
        print("a media dos numeros é", num1 / cont)
        

        