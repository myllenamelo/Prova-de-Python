'''
[Questão criada por Myllena Laís (adaptada)] Um novo funcionário de supermercado quer saber em qual corredor se 
encontra um produto. No sistema existem os seguintes produtos: Arroz - corredor 1, Feijão - corredor 1, Óleo de 
soja - corredor 2, Sal - corredor 3, Açúcar - corredor 3, Café- corredor 4, Molho de tomate -corredor 5, 
Macarrão- corredor 6. O funcionário precisa encontrar em qual corredor está o produto para ajudar o cliente em 
sua compra. Use tupla para criar esse programa. 
'''

i=0
itens = ('ARROZ',1,'FEIJÃO ',1,'ÓLEO DE SOJA',2,'SAL',3,'AÇUCAR',3,
'CAFÉ',4,'MOLHO DE TOMATE',5,'MACARRÃO',6)

produto = str(input('qual produto?')).upper()

for i in range(0, len(itens)):
    if itens[i] == produto:
        print(f'o produto {produto} está no corredor {itens[i+1]}')
    if itens[i] != produto:
        print(f'não há o produto {produto} no supermercado ')