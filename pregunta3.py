
## Del ejercicio anterior:
class Stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"Stormtrooper {self.nombre} de rango {self.rango} creado con éxito")

trooper = Stormtrooper("TS-1135", "Cabo")
print(trooper.nombre)  
print(trooper.rango)  




## Implementa el método str y haz que muestre el nombre y el rango del Stormtropper
class Stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        
    def calificacion(self):
        if self.rango == "Sargento":
            return "Alto"
        elif self.rango == "Cabo":
            return "Medio"
        else:
            return "Bajo"
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Rango: {self.rango}, Calificación: {self.calificacion()}"

trooper = Stormtrooper("TS-1135", "Cabo")
print(trooper)

## Crea una lista con un numero arbitrario de objetos tipo Stormtropper.
stormtrooper_lista = []

for i in range(5):
    trooper = Stormtrooper(f"TS-{i}", "Cabo")
    stormtrooper_lista.append(trooper)

print(stormtrooper_lista)

## Recorre los elementos de la lista, y utiliza el método print de esos objetos para visualizar por pantalla la información del str
for trooper in stormtrooper_lista:
    print(trooper) 
