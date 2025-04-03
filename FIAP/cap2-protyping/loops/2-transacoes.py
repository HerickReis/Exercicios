"""
2 - Observando o mercado de educação infantil, você e sua equipe decidem criar um aplicativo por meio do qual as crianças aprendam a controlar os seus gastos.
Como forma de validar um protótipo, foi solicitado que você crie um script simples,  em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia 
e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou. Seu programa deverá exibir, ao final, o valor total gasto pelo usuário, 
bem como a média do valor de cada transação.
"""
total_transacoes = int(input("Quantas transações foram realizadas hoje: "))
total = 0

for transacao in range(total_transacoes):
    valores = float(input(f"Valor da {transacao + 1} transação: "))
    total += valores

print(f"""O valor total gasto foi {total}.
      O valor médio por item é de {total / total_transacoes}""")
