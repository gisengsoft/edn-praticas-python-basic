# =============================================
# Atividade 2 - Calculadora de Desconto
# Autor: Gilson Inacio
# =============================================

# Informações do produto
produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20  # %

# Cálculo do desconto
valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

# Exibição
print("2 - Calculadora de Desconto")
print(f"Produto: {produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
