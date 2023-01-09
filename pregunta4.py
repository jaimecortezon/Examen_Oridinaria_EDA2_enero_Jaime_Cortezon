## Crea una clase llamada artefactosvaliosos.py que tenga los atributos peso, nombre, precio y fecha de caducidad.
class artefactos_valiosos:
  def __init__(self, peso, nombre, precio, fecha_caducidad):
    self.peso = peso
    self.nombre = nombre
    self.precio = precio
    self.fecha_caducidad = fecha_caducidad

artefacto1 = artefactos_valiosos(1.5, "diamante", 500000, "2023-1-27")

## Crea el constructor de la clase. Añade en el constructor un print para informar de que la conserva se ha creado con éxito
class artefactos_valiosos:
  def __init__(self, peso, nombre, precio, fecha_caducidad):
    self.peso = peso
    self.nombre = nombre
    self.precio = precio
    self.fecha_caducidad = fecha_caducidad
    print("Se ha creado una nueva instancia de artefactos_valiosos")

## Crea el método __str__ para visualizar por pantalla la información de los productos
class artefactos_valiosos:
  def __init__(self, peso, nombre, precio, fecha_caducidad):
    self.peso = peso
    self.nombre = nombre
    self.precio = precio
    self.fecha_caducidad = fecha_caducidad

  def __str__(self):
    return "Nombre: {}, Peso: {}, Precio: {}, Fecha de caducidad: {}".format(self.nombre, self.peso, self.precio, self.fecha_caducidad)
artefacto1 = artefactos_valiosos(1.5, "diamante", 500000, "2023-1-27")
print(artefacto1)

## Crea algunos artefactos valiosos
artefacto1 = artefactos_valiosos(1.5, "diamante", 500000, "2023-1-27")
artefacto2 = artefactos_valiosos(2.8, "Collar de diamantes", 10000000, "2023-1-28")
artefacto3 = artefactos_valiosos(1.2, "anillo de oro", 1500, "2023-1-29")


artefactos = [artefacto1, artefacto2, artefacto3]

# Ordena la lista de artefactos por fecha de caducidad
artefactos_ordenados = sorted(artefactos, key=lambda x: x.fecha_caducidad)

# Imprime la información de cada artefacto ordenado por fecha de caducidad
for artefacto in artefactos_ordenados:
  print(artefacto)

# Para modificar el precio
artefacto1.precio = 600000
