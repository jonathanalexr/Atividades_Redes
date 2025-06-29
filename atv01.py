def calcular_imc():
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura informados
    pelo usuário e exibe o resultado na tela.
    """
    print("--- Calculadora de IMC ---")

    try:
        peso = float(input("Digite seu peso em kg (ex: 70.5): "))
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números para peso e altura.")
        return

    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser valores positivos.")
        return

    imc = peso / (altura ** 2)

    print(f"\nSeu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    elif 30 <= imc < 34.9:
        print("Classificação: Obesidade Grau I")
    elif 35 <= imc < 39.9:
        print("Classificação: Obesidade Grau II")
    else:
        print("Classificação: Obesidade Grau III (Mórbida)")

# Chama a função para executar o cálculo do IMC
if __name__ == "__main__":
    calcular_imc()