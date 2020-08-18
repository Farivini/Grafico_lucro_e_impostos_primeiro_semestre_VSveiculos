import matplotlib.pyplot as plt

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
vendas = [981541.34

    , 708132.14, 867426.64, 898153.92, 791040.55, 1348925.25]

plt.bar(meses, vendas)
plt.grid(True)
plt.ylabel('Lucro bruto R$')
plt.xlabel('mes')
plt.title('primeiro semestre')
plt.show()
