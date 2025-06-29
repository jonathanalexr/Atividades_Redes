# 1. Importe o módulo statistics e crie uma lista com 14 elementos em ordem crescente.
import statistics

# Lista com 14 elementos em ordem crescente
numeros = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 6pe5, 70, 75]
print(f"Lista de números: {numeros}\n")

# 2. Calcule a média e a mediana dos valores usando o módulo completo (import statistics).
media_completo = statistics.mean(numeros)
mediana_completo = statistics.median(numeros)
print(f"Usando 'import statistics':")
print(f"  Média: {media_completo}")
print(f"  Mediana: {mediana_completo}\n")

# 3. Use um alias (apelido) para o módulo statistics e refaça os cálculos.
import statistics as st

media_alias = st.mean(numeros)
mediana_alias = st.median(numeros)
print(f"Usando 'import statistics as st':")
print(f"  Média: {media_alias}")
print(f"  Mediana: {mediana_alias}\n")

# 4. Importe apenas as funções mean e median do módulo statistics e refaça os cálculos.
from statistics import mean, median

media_funcoes = mean(numeros)
mediana_funcoes = median(numeros)
print(f"Usando 'from statistics import mean, median':")
print(f"  Média: {media_funcoes}")
print(f"  Mediana: {mediana_funcoes}\n")

# 5. Por fim, importe todas as funções do módulo statistics e calcule novamente a média e a mediana da lista.
from statistics import *

media_todas_funcoes = mean(numeros)
mediana_todas_funcoes = median(numeros)
print(f"Usando 'from statistics import *':")
print(f"  Média: {media_todas_funcoes}")
print(f"  Mediana: {mediana_todas_funcoes}\n")