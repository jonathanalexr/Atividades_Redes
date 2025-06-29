# Criar e inicializar o dicionário 'alunos'
alunos = {
    "Ana": 8.5,
    "Pedro": 7.0,
    "Maria": 9.2
}
print(f"Dicionário de alunos inicial: {alunos}")

# Adicionar o aluno "Carlos"
alunos["Carlos"] = 6.5
print(f"Após adicionar 'Carlos': {alunos}")

# Atualizar a nota da aluna "Ana"
alunos["Ana"] = 9.0
print(f"Após atualizar a nota de 'Ana': {alunos}")

# Remover o aluno "Pedro"
del alunos["Pedro"]
print(f"Após remover 'Pedro': {alunos}")

# Calcular a média das notas
if alunos: # Verifica se o dicionário não está vazio para evitar divisão por zero
    soma_notas = sum(alunos.values())
    media_notas = soma_notas / len(alunos)
    print(f"A média das notas dos alunos é: {media_notas:.2f}")
else:
    print("Não há alunos no dicionário para calcular a média.")

# Verificar se o aluno "Maria" está presente
if "Maria" in alunos:
    print("O aluno 'Maria' está presente no dicionário.")
else:
    print("O aluno 'Maria' NÃO está presente no dicionário.")