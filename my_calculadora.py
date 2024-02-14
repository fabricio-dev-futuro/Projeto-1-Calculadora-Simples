print("\n******************* Calculadora em Python com Placeholders *******************")

print('Escolha um escolha matemático abaixo:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print()
# O usuário digita um número para que seja escolhido um operador mateático acima
escolha = int(input('Você escolheu o operador: '))

# Agora ele digita o Primeiro número para a conta
num1 = int(input('Digite um numero: '))

# Aqui ele digita o Segundo número para a conta
num2 = int(input('Digite outro número: '))
print()


# Tratando uma possivel divisão por zero
if num2 == 0 and escolha == 4:
    print('Não é permitido divisão por zero!\nPor favor, mude o valor do 2º número.')
else:
# Inicio da lógica:
        
    if escolha == 1:
        resultado = num1 + num2
        print('%a + %s = %r' %(num1, num2, resultado))

    elif escolha == 2:
        resultado = num1 - num2
        print('%a - %s = %r' %(num1, num2, resultado))

    elif escolha == 3:
        resultado = num1 * num2
        print('%a * %s = %r' %(num1, num2, resultado))

    elif escolha == 4:
        resultado = num1 / num2
        print('%a / %s = %r' %(num1, num2, resultado))

    else:
        print('Operador de escolha inexistente! Digite somente opções entre 1 a 4.')

    #Posto só para pular linha, deixando separado da mensagem do caminho do arquivo que aparece no terminal.
    print()
