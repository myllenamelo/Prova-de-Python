'''
[Questão criada por Pedro Vinicius (adaptada)] Crie um programa que leia o nome de n jogadores, o time que joga, 
a quantidade de partidas que eles jogaram, a quantidade de gols feitos em cada partida e o total de gols. 
Essas informações serão armazenadas em um dicionário. O programa apresentará no final todas as informações dos 
jogadores e um ranking com os top 3 com mais gols. 
'''

time = list()
jogador = dict()
partidas = list()



while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do(a) Jogador(a): '))
    jogador['Time'] = str(input('Nome do seu time: '))
    quant = int(input(f'Quantas partidas {jogador ["Nome"]} jogou '))
    partidas.clear()
    for p in range(0, quant):
        partidas.append(int(input('Quantos gols na partida ' + str(p+1) + ' ? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        decisao=str(input('Continua (s/n)?')).upper()
        if decisao in 'SN':
            break
        print('erro')
    if decisao == 'N':
        break

print()  
print('-'*60)
print(f'{"Nome":<15}{"Time":<15}{"Total":<9}{"Gols":<9}')
for k, v in enumerate(time):
    print(f'{v["Nome"]:<15}{v["Time"]:<15}{v["Total"]:<9}{v["Gols"]}')
print('-'*60)


