## Crea una clase llamada stormtrooper.py que tenga los atributos nombre y rango
## Crea el constructor de la clase. Añadir en el constructor un print para informar de que el stormtrooper se ha creado con éxito.

class Stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"Stormtrooper {self.nombre} de rango {self.rango} creado con éxito")

trooper = Stormtrooper("TS-1135", "Cabo")
print(trooper.nombre)  
print(trooper.rango)  

## Crea una lista con un numero arbitrario de objetos tipo Stormtropper.
troopers = [Stormtrooper("Finn", "Cabo"), Stormtrooper("Phasma", "Capitán"), Stormtrooper("Rey", "Cabo")]   

## Recorre los elementos de la lista, y prueba a ejecutar el método calificación de cada objeto que has creado.
class Stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"Stormtrooper {self.nombre} de rango {self.rango} creado con éxito")
    
    def calificación(self):
        if self.rango == "Capitán":
            return "Excelente"
        elif self.rango == "Coronel":
            return "Bueno"
        else:
            return "Regular"
            
trooper = Stormtrooper("TS-1135", "Cabo")
print(trooper.calificacion())