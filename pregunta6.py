## ¿Cuál es el valor máximo de los artículos que se pueden agregar a la mochila de manera que el peso no exceda el límite de peso W?
def mochila(precio, pesos, peso_maximo):
  n = len(precio)
  dp = [[0 for _ in range(peso_maximo + 1)] for _ in range(n + 1)]
 
  for i in range(1, n + 1):
    for j in range(1, peso_maximo + 1):
      if j >= pesos[i - 1]:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - pesos[i - 1]] + precio[i - 1])
      else:
        dp[i][j] = dp[i - 1][j]
 
  return dp[n][peso_maximo]
 
precio = [103, 60, 70, 5, 15]
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100
 
print(mochila(precio, pesos, peso_maximo))