import matplotlib.pyplot as plt

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
imposto = [65526.80

    , 46827.58, 57319.88, 59346.37, 51594.83, 88341.30]

plt.bar(meses, imposto)
plt.grid(True)
plt.ylabel('Total imposto R$')
plt.xlabel('mes')
plt.title('primeiro semestre')
plt.show()