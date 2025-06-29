# 1. Crie uma função chamada boas_vindas() que imprima a mensagem "Bem-vindo(a) à disciplina ALLP"
def boas_vindas():
    print("Bem-vindo(a) à disciplina ALLP")

# 2. Crie uma função chamada quadrado(numero) que receba um número como parâmetro e retorne o quadrado dele.
def quadrado(numero):
    return numero ** 2

# 3. Crie uma função chamada somar(a, b) que receba dois números, some-os e retorne o resultado.
def somar(a, b):
    return a + b

# 4. Crie uma função chamada contagem(inicio=1, fim=5) que imprima uma contagem de inicio até fim (use range).
def contagem(inicio=1, fim=5):
    print(f"Contagem de {inicio} até {fim}:")
    for i in range(inicio, fim + 1):
        print(i)

# 5. Crie uma função chamada calcula_imc(peso=70, altura=1.75) que retorne o valor do IMC.
def calcula_imc(peso=70, altura=1.75):
    # Evita divisão por zero ou altura inválida
    if altura <= 0:
        return "Erro: Altura deve ser maior que zero."
    imc = peso / (altura ** 2)
    return imc

# 6. Crie uma função chamada par_ou_impar(numero) que informe se o número é par ou ímpar.
def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

# 7. Crie uma função chamada saudacao(nome="Visitante") que exiba uma mensagem de saudação com o nome passado.
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}! Tenha um ótimo dia.")


# --- Exemplos de uso das funções ---

print("--- Testando a função boas_vindas() ---")
boas_vindas()
print("-" * 30 + "\n")

print("--- Testando a função quadrado(numero) ---")
num = 7
print(f"O quadrado de {num} é: {quadrado(num)}")
num = 10
print(f"O quadrado de {num} é: {quadrado(num)}")
print("-" * 30 + "\n")

print("--- Testando a função somar(a, b) ---")
n1, n2 = 15, 23
print(f"A soma de {n1} e {n2} é: {somar(n1, n2)}")
print("-" * 30 + "\n")

print("--- Testando a função contagem(inicio=1, fim=5) ---")
# Sem parâmetros
contagem()
print("\n")
# Com parâmetros
contagem(inicio=3, fim=8)
print("-" * 30 + "\n")

print("--- Testando a função calcula_imc(peso, altura) ---")
print(f"IMC padrão (70kg, 1.75m): {calcula_imc():.2f}")
print(f"IMC de 85kg e 1.80m: {calcula_imc(peso=85, altura=1.80):.2f}")
print(f"IMC de 55kg e 1.60m: {calcula_imc(peso=55, altura=1.60):.2f}")
print("-" * 30 + "\n")

print("--- Testando a função par_ou_impar(numero) ---")
par_ou_impar(4)
par_ou_impar(7)
par_ou_impar(0)
print("-" * 30 + "\n")

print("--- Testando a função saudacao(nome) ---")
# Sem parâmetro
saudacao()
# Com parâmetro
saudacao("Alice")
saudacao("Roberto")
print("-" * 30 + "\n")