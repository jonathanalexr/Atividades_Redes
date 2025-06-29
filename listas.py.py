# 1) Manipulação da lista 'animais'
animais = ['cachorro', 'gato', 'papagaio']
print(f"Lista inicial de animais: {animais}")

# Adicionar 'hamster' ao final da lista
animais.append('hamster')
print(f"Após adicionar 'hamster': {animais}")

# Inserir 'coelho' na posição 1
animais.insert(1, 'coelho')
print(f"Após inserir 'coelho' na posição 1: {animais}")

# Remover o último animal da lista
animais.pop()
print(f"Após remover o último animal: {animais}")

# Remover o animal na posição 2
animais.pop(2)
print(f"Após remover o animal na posição 2: {animais}")

# Alterar o animal na posição 0 para 'leão'
animais[0] = 'leão'
print(f"Após alterar o animal na posição 0 para 'leão': {animais}")

# 2) Acessando elemento em uma matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Para acessar o número 5, que está na segunda linha (índice 1) e segunda coluna (índice 1)
numero_5 = matriz[1][1]
print(f"\nO número 5 na matriz é: {numero_5}")

# 3) Comprimento de uma lista
exemplo = [10, 20, [30, 40], "hello"]
comprimento_exemplo = len(exemplo)
print(f"\nO comprimento da lista 'exemplo' é: {comprimento_exemplo}")

# 4) Acessando elementos em uma lista de frutas
frutas = ['morango', 'abacaxi', 'goiaba', 'jambo', 'banana']

# Primeiro elemento da lista
primeiro_elemento = frutas[0]
print(f"\nO primeiro elemento da lista 'frutas' é: {primeiro_elemento}")

# Terceiro elemento da lista
terceiro_elemento = frutas[2]
print(f"O terceiro elemento da lista 'frutas' é: {terceiro_elemento}")