print ('Maquina de fabricar a media de quantos numeros quiser')
X = float(input('Insira o primeiro numero:'))
Y = float(input('Insira o segundo numero:'))
num1 = X + Y
cont = 2
while True:
    resposta = str(input('Deseja inserir outro numero?')).lower()
    if resposta == 'sim':
        A = float(input('Escolha o proximo numero:'))
        cont += 1
        num1 += A       
    elif resposta == 'nao':
        print("a media dos numeros é", num1 / cont)
        
