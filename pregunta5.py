
## sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila
def usar_la_fuerza(nivel_de_fuerza, mochila):
  if nivel_de_fuerza > 0 and len(mochila) > 0:
    # Sacar el primer objeto de la mochila
    objeto = mochila.pop(0)
    # Si el objeto es un sable de luz:
    if objeto == "sable de luz":
    # Llamar recursivamente a la función con un nivel de fuerza disminuido y la mochila actualizada
        usar_la_fuerza(nivel_de_fuerza - 1, mochila)
  else:
    # cuando el nivel de fuerza es 0 o menor o la mochila está vacía:
    pass

## Determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo
def usar_la_fuerza(nivel_de_fuerza, mochila):
  if nivel_de_fuerza > 0 and len(mochila) > 0:
    # Sacar el primer objeto de la mochila
    objeto = mochila.pop(0)
    # Si el objeto es un sable de luz:
    if objeto == "sable de luz":
      # Imprimir el número de objetos sacados hasta encontrar el sable de luz
      print(f"Se sacaron {len(mochila)} objetos antes de encontrar el sable de luz")
      # No hacer nada más, ya que el sable de luz fue encontrado
      return
    # Llamar recursivamente a la función con un nivel de fuerza disminuido y la mochila actualizada
    usar_la_fuerza(nivel_de_fuerza - 1, mochila)
  else:
    # cuando el nivel de fuerza es 0 o menor o la mochila está vacía:
    pass

# Si se llegó a este punto, es porque no se encontró un sable de luz en la mochila
print("No hay un sable de luz en la mochila de Obi-Wan Kenobi")

# Crear la lista que representa la mochila de Obi-Wan Kenobi
mochila = ["radio", "blaster", "cantimplora", "sable de luz"]

# Llamar a la función "usar la fuerza" con un nivel de fuerza de 10 y la mochila creada anteriormente
usar_la_fuerza(5, mochila)