class artefactos_valiosos:
    def __init__(peso, nombre, precio, fecha_de_caducidad):
        self.peso=peso
        self.nombre=nombre
        self.precio=precio
        self.fecha_de_caducidad=fecha_de_caducidad
        print(" la conserva se ha creado con éxito")
    def __str__ (self):
        a= "peso: "+ str(self.peso) + "nombre"+str(self.nombre)+"precio"+str(self.precio)+"fecha de caducidad"+str(self.fecha_de_caducidad)
        return a

artefacto1= artefactos_valiosos(1,"reloj",350,"01/09/2023")
artefacto2= artefactos_valiosos(3,"cuadro",500,"13/08/2024")

