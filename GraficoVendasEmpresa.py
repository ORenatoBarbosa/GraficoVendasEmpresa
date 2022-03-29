# Grafico de Vendas de uma empresa nos anos de 2018,2019 e 2020 durante os seis primeiros meses dos anos, e o impacto da pandemia nas vendas.
import matplotlib.pyplot

#Dados que colocaremos no grafico
meses2018 = ['jan', 'fev', 'mar','abr','mai','jun']
dados2018 = [3750, 15000, 2500, 2800, 2620, 4270 ]
meses2019 = ['jan', 'fev', 'mar','abr','mai','jun']
dados2019 = [1825, 13006, 750, 480, 350, 1450 ]
meses2020 = ['jan', 'fev', 'mar','abr', 'mai','jun']
dados2020 = [1500, 10500, 500, 620, 564, 1675 ]

#Plotando os dados no grafico
#Linha normal
matplotlib.pyplot.plot(meses2018, dados2018, color='red')
#k: Linha pontilhada
matplotlib.pyplot.plot(meses2019, dados2019,'k:', color='orange')
#k--: Linha tracejada
matplotlib.pyplot.plot(meses2020, dados2020,'k--', color='black')

#Lista que irá para a legenda
#Deve ser colocado na mesma ordem
anos = [2018, 2019, 2020]
#Criando a caixa de legenda externa(lista de nomes, titulo, localização)
matplotlib.pyplot.legend(anos, title="Anos", loc="center left")

#Definindo limites para a coluna y
# só valores positivos
matplotlib.pyplot.ylim(0, 20000)

#Titulo
matplotlib.pyplot.title('Faturamento')

#Nome do eixo horizontal x
matplotlib.pyplot.xlabel('Meses')
#Nome do eixo vertical y
matplotlib.pyplot.ylabel('Faturamento em R$')

matplotlib.pyplot.show()

# Renato Barbosa
