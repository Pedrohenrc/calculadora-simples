import math
import numexpr as ne

def medianormal():

    while True:
        try:
            nums = list(float(x) for x in input('Separados por espaços, digite os números com os quais será feito a média aritmética: ').strip().split())
            if not nums:
                raise ValueError("Nenhum número inserido.")
            resultado = sum(nums) / len(nums)
            return resultado
        except ValueError:
            print("Entrada inválida. Por favor, digite os números corretamente separados por espaço.")
def mediaponderada ():
    while True:
        try:
            entrada = list(input("Digite as notas no formato NOTA:PESO separadas por espaço (exemplo: 10:5 9:2):").split())

            notas = []
            pesos = []

            for item in entrada:
                nota, peso = item.split(':')
                notas.append(float(nota))
                pesos.append(float(peso))
            
            notasp = sum(nota*peso for nota, peso in zip(notas, pesos))
            somaponderada = sum(pesos)
            if somaponderada == 0:
                raise ValueError("A soma dos pesos não pode ser zero.")
            
            resultado = (notasp / somaponderada)
            return resultado
        except ValueError as e:
            
            print(f"Entrada inválida. Por favor, digite os dados no formato correto (10:5...).")

def expressoes(expressao):
    expressao = expressao.replace('.', '*')
    expressao = expressao.replace(':', '/')
    return expressao
def resultado_(resultado):
    return str(resultado).replace('.', ',')  
def calculadora():
    while True:
        try:
            calc = input('Digite uma expressão matemática: ').strip()

            calc = expressoes(calc)

            resultado = ne.evaluate(calc)

            resultado = resultado_(resultado)

            return resultado
        
        except (ValueError, SyntaxError, NameError):
            print(f"Entrada inválida. Por favor, digite uma expressão matemática válida.")
        except ZeroDivisionError:
            print('Não é possivel realizar divisões por zero, por favor, tente novamente.')

print('Seja bem vindo a Calculadora!')
print('Aqui é possivel fazer cálculo com as operações básicas, além da media de números (aritmética e ponderada)')
X = str(input('Deseja saber os comandos para cada cálculo? (sim ou não) ')).lower().strip()
if X == 'sim':
    print('Multiplicação: . ou *\n'
           'Divisão: / ou :\n'
           'Soma: +\n'
           'Subtração: -\n'
           'Potenciação: ** \n'
           'Radiciação: //')
while True:
    try:
        y = int(input('Insira para onde deseja seguir (Digite 1 para media aritmética, 2 para media ponderada e 3 para calculadora): '))
        if y < 1 or y > 3:
            raise ValueError
        print ('Entrada inválida, por favor escolha um número entre 1 e 3')
        if y == 1:
            resultado = medianormal()
            print (f'A média aritmética é {resultado}')
        elif y == 2:
            resultado = mediaponderada()
            print (f'A média ponderada é {resultado}')
        elif y == 3:
            resultado = calculadora()
            print (f'O Resultado da expressão é {resultado}')
        z = str(input('Deseja encerrar a calculadora?(Digite "sim" caso deseje) ')).lower().strip()
        if z == 'sim':
            break
    except ValueError:
        print ('Entrada inválida. Por favor, tente novamente')
