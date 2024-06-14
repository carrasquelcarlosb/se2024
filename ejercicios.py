# Description: Este archivo contiene las clases de los ejercicios propuestos en el enunciado del trabajo práctico. 

# Autor: Carlos Carrasquel 14/06/2024 
# Version: 1.0 
# Licencia MIT 

# MACROS para ejercicio 2 
NUMERO_PERSONAS = 50

# Ejercicio 1

# Esta clase permite leer un número y determinar si es par o impar, 
# ademas de imprimir los números pares o impares descendientemente desde el número ingresado hasta el cero o uno respectivamente.

class Ejercicio1:
    def __init__(self):
        self.numero = 0

    def leer_numero(self):
        self.numero = int(input("Ingrese un número: "))     
    def par_o_impar(self):
        if self.numero % 2 == 0:
            for i in range(self.numero, -1, -2):
                print(i)
        else:
            for i in range(self.numero, -1, -2):
                print(i)
    

# Ejercicio 2

# Esta clase permite leer los datos de 50 personas y mostrar una clasificación de las mismas según edad y sexo.
# Ademas, muestra los siguientes resultados:
# a. Cantidad de personas mayores de edad (18 años o más).
# b. Cantidad de personas menores de edad.
# c. Cantidad de personas masculinas mayores de edad.
# d. Cantidad de personas femeninas menores de edad.
# e. Porcentaje que representan las personas mayores de edad respecto al total de personas.
# f. Porcentaje que representan las mujeres respecto al total de personas.

class Ejercicio2:
    def __init__(self):
        self.personas = []

    def leer_personas(self):
        for i in range(NUMERO_PERSONAS):
            sexo = input("Ingrese el sexo de la persona: ")
            # check si la vaiable sexo es valida 
            while sexo.lower() not in ["m", "f", "otro"]:
                print("Sexo invalido. Ingrese M,F u Otro")
                sexo = input("Ingrese el sexo de la persona: ")
                
            edad = int(input("Ingrese la edad de la persona: "))
            #check si la variable edad es valida 
            while edad < 0:
                print("Edad invalida. Ingrese una edad válida")
                edad = int(input("Ingrese la edad de la persona: "))
            self.personas.append({"sexo": sexo, "edad": edad})

    # a.
    def mayores_de_edad(self):
        mayores = 0
        for persona in self.personas:
            if persona["edad"] >= 18:
                mayores += 1
        return mayores
    # b. 
    def menores_de_edad(self):
        menores = 0
        for persona in self.personas:
            if persona["edad"] < 18:
                menores += 1
        return menores
    # c.
    def masculinos_mayores(self):
        masculinos = 0
        for persona in self.personas:
            if persona["sexo"].lower() in ["m", "masculino"] and persona["edad"] >= 18:
                masculinos += 1
        return masculinos
    # d.
    def femeninos_menores(self):
        femeninos = 0
        for persona in self.personas:
            if persona["sexo"].lower() in ["f", "femenino"] and persona["edad"] < 18:
                femeninos += 1
        return femeninos
    # e.
    def porcentaje_mayores(self):
        return self.mayores_de_edad() / 50 * 100
    # f. 
    def porcentaje_mujeres(self):
        mujeres = 0
        for persona in self.personas:
            if persona["sexo"].lower() in ["f", "femenino"]:
                mujeres += 1
        return mujeres / 50 * 100

# Ejercicio 3

# Esta clase permite calcular el salario de un trabajador en base a las horas trabajadas y la tarifa.
# El importe liquidado (sueldo) depende de una tarifa o precio por hora establecida y de un condicionante sobre las horas trabajadas:
# si la cantidad de horas trabajadas es mayor a 40 horas, la tarifa se incrementa en un 50% para las horas extras.
# Las horas extras se calculan a partir de las 40 horas trabajadas. Todas las horas trabajadas se pagan a la tarifa normal hasta las 40 horas. 
# Las horas extras se pagan a la tarifa incrementada. 
# Calcular el sueldo recibido por el trabajador en base las horas trabajadas y la tarifa.
class Ejercicio3:
    def __init__(self):
        self.horas_trabajadas = 0
        self.tarifa = 0
    def leer_horas_trabajadas(self):
        self.horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
    def leer_tarifa(self):
        self.tarifa = int(input("Ingrese la tarifa: "))
    def calcular_sueldo(self):
        if self.horas_trabajadas > 40:
            return (self.horas_trabajadas * self.tarifa) + ((self.horas_trabajadas - 40) * self.tarifa * 1.5)
        else:
            return self.horas_trabajadas * self.tarifa


    