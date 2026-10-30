# Exercicio Prático - Escolha de Condições de compra

Programa em Python que ajuda a decidir a melhor forma de pagar um bem (um carro fictício, o “XIMBICA-GLX”), comparando pagamento à vista e financiamentos com prestações fixas, usando o conceito de valor presente (VP) com juros compostos. A primeira prestação é paga no ato da compra, e o financiamento mais vantajoso é o de menor VP; em caso de empate, vence o de menos parcelas.

Para evitar erros de ponto flutuante, valores monetários são tratados em centavos e as taxas de juros em unidades por milhar, com truncamento do VP via int().

O programa tem 4 modos de operação:

Valor presente de um financiamento: dados prestação, taxa e número de parcelas, calcula o VP.
Prestação mínima: dados valor à vista, taxa e número de parcelas, encontra a menor prestação cujo VP cobre o valor à vista (corrigindo o truncamento somando 1 centavo quando necessário).
Comparação de opções: compara à vista, 12x e 24x para uma taxa e indica a melhor opção.
Tabela comparativa: gera uma tabela formatada com os VPs de cada opção para uma sequência de taxas (progressão aritmética), indicando a melhor decisão para cada taxa.

Conceitos praticados: operações aritméticas, condicionais (if/else), laços (while), entrada e saída (input/print), formatação de saída e matemática financeira (progressão geométrica e juros compostos).

Fórmula central:
VP = (Prestação / i) × (1 + i − 1/(1+i)^(n−1)), com i = taxa/1000
