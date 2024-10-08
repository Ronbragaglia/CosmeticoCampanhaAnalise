# -*- coding: utf-8 -*-
"""CosméticoCampanhaAnálise

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10FAU88OuQBNLQcZVyA62ANmodWt9YZyo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

data = {
    'Idade': [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    'Interesse': ['Maquiagem', 'Cuidado com a Pele', 'Maquiagem', 'Perfumes', 'Cuidado com a Pele',
                  'Cabelo', 'Maquiagem', 'Cabelo', 'Perfumes', 'Cuidado com a Pele'],
    'Gênero': ['Feminino', 'Feminino', 'Feminino', 'Feminino', 'Masculino',
               'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino'],
    'Vendas': [200, 150, 250, 300, 100, 200, 400, 250, 300, 150],
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
sns.barplot(x='Idade', y='Vendas', hue='Interesse', data=df)
plt.title('Vendas por Faixa Etária e Interesse')
plt.xlabel('Idade')
plt.ylabel('Vendas')
plt.legend(title='Interesse')
plt.show()

investimento_total = 5000
vendas_totais = df['Vendas'].sum()
roi = (vendas_totais - investimento_total) / investimento_total * 100

print(f"O ROI da campanha é de {roi:.2f}%")

aumento_vendas = 0.30 * vendas_totais
print(f"Com o aumento de 30%, as vendas se tornam: {vendas_totais + aumento_vendas:.2f}")