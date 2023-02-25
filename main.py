# Questão do 'Unknown User' - Grupo Estácio EAD 2023.1
# 'Digamos que eu pego 5.000 emprestado, divido em 48 parcelas com o juros de 3% ao mês.
#  Qual o valor da parcela?'

# github.com/diegocorredeira

valor = float(input('Informe o valor que deseja solicitar: '))
taxa_juros = float(input('Informe a taxa de juros: '))
meses = int(input('Informe a quantidade de vezes em que deseja pagar: '))
decisao = str(input('O juros é simples ou composto? S ou C: ')).lower()

JuroSimples = valor * ((taxa_juros / 100) * meses)
parcelaS = (valor + JuroSimples) / meses
valorJuroSimples = JuroSimples + valor
#############################################
jurosComposto = valor * ((1 + taxa_juros / 100) ** meses - 1)
parcelaC = (valor + jurosComposto) / meses
valorJurosComposto = jurosComposto + valor

if decisao == 's':
    print(f'O juros simples do plano contratado é de R${JuroSimples:.2f}, somando {valorJuroSimples:.2f} e o valor '
          f'parcelado em {meses}x é de R${parcelaS:.2f} por mês ')
if decisao == 'c':
    print(f'O juros composto do plano contratado é de R${jurosComposto:.2f}, somando {valorJurosComposto:.2f} e o '
          f'valor parcelado em {meses}x é de R${parcelaC:.2f} por mês')
if decisao not in ['s', 'c']:
    print('Entrada incorreta.')
