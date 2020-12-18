'''
[Questão criada por Nicolas Mathias (adaptada)] Josemar trabalha numa revendedora de carros usados a cada carro 
vendido ele ganha 1,5 % de comissão. Utilizando lista composta guarde o nome e preço dos carros. Para vender o 
carro mostre uma tabela com os carros e os preços. Quando o carro for vendido deve modificar a lista de carros para 
vendido. A venda acaba quando os carros acabarem ou quando a pessoa não quiser continuar. No final mostre:
 quantidade de carros vendidos e quanto Josemar lucrou no final em reais. Para essa questão use pelo menos duas 
 funções. 
 '''

comissaojosemar=0
josemar= list() 
funcionario=0
vendeu=0

def saldofinal (total,vendidos):
    resultado=total-vendidos
    print ('Sobraram: ',resultado,' veículos.')

def comissao (preco,perc=1.5):
    com=((preco*perc)/100)
    return com

def vendidos (lst):
    print ('Vendeu:',len(lst))


carros = [['1-gol', 20000], ['2-palio', 15000],
          ['3-uno', 25000], ['4-golf', 10000]]

carrosvendidos = []



print('-'*5, 'Carros a venda', '-'*5)
for c in carros:
    print(f'{c[0]} ------- R$ {c[1]}')
while True:
    op = int(input('Qual carro irá levar? (Digite o código)'))
    if op == 1:
        funcionario += comissao(carros[0][1])
        josemar.append(funcionario)
        carrosvendidos.append(carros[0:])
        carros[0][0] = 'VENDIDO'
    if op == 2:
        funcionario += comissao(carros[1][1])
        josemar.append(funcionario)
        carrosvendidos.append(carros[1:])
        carros[1][0] = 'VENDIDO'
    if op == 3:
        funcionario += comissao(carros[2][1])
        josemar.append(funcionario)
        carrosvendidos.append(carros[2:])
        carros[2][0] = 'VENDIDO'
    if op == 4:
        funcionario +=comissao(carros[3][1])
        josemar.append(funcionario)
        carrosvendidos.append(carros[3:])
        carros[3][0] = 'VENDIDO'

    if len(carrosvendidos) == 4:
        break
    continua = str(input('Deseja continuar?(s/n)'))
    if continua == 'n':
        break
    for c in carros:
        print(f'{c[0]} ------- R$ {c[1]}')

vendidos(carrosvendidos)
saldofinal(len(carros),len(carrosvendidos))
comissaojosemar=sum(josemar)
print('A comissão de Josemar foi: R$',comissaojosemar)