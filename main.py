# entrada
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

nota1 = float(input('Digite sua nota1: '))
nota2 = float(input('Digite sua nota2: '))

# processamento
media = (nota1 + nota2) / 2

print('Olá', nome)
print('Sua média é', media)

# condição = operadores de comparação
# se <condição>:
if idade >= 18:
    print('Você é maior de idade')
    print()
else:
    print('Você é menor de idade')

if media >= 7:
    print('Aprovado')
elif media >= 5:
    # media é menor do que 7 e maior ou igual do 5
    print('Recuperação')
else:
    # menor do que cinco
    print('Reprovado')

# snake case
print('Você quer verificar de outra pessoa?')
is_continue = input('Digite s (sim) ou n (não): ')

while is_continue == 's':
    nome = input('Digite o nome: ')
    idade = int(input('Digite o idade: '))

    nota1 = float(input('Digite a nota1: '))
    nota2 = float(input('Digite a nota2: '))
    # condição = operadores de comparação
    # se <condição>:
    if idade >= 18:
        print('É maior de idade')
        print()
    else:
        print('É menor de idade')

    if media >= 7:
        print('Aprovado')
    elif media >= 5:
        # media é menor do que 7 e maior ou igual do 5
        print('Recuperação')
    else:
        # menor do que cinco
        print('Reprovado')

    is_continue = input('Digite s (sim) ou n (não): ')