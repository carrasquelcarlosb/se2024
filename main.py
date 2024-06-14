from ejercicios import *

# Ejercicio 1
ejercicio1 = Ejercicio1()
ejercicio1.leer_numero()
ejercicio1.par_o_impar()

#Ejercicio 2
ejercicio2 = Ejercicio2()
ejercicio2.leer_personas()
print("Cantidad de personas mayores de edad: ", ejercicio2.mayores_de_edad())
print("Cantidad de personas menores de edad: ", ejercicio2.menores_de_edad())
print("Cantidad de personas masculinas mayores de edad: ", ejercicio2.masculinos_mayores())
print("Cantidad de personas femeninas menores de edad: ", ejercicio2.femeninos_menores())
print("Porcentaje que representan las personas mayores de edad respecto al total de personas: ", ejercicio2.mayores_de_edad() / 5 * 100)
print("Porcentaje que representan las mujeres respecto al total de personas: ", ejercicio2.femeninos_menores() / 5 * 100)
## Ejercicio 3

ejercicio3 = Ejercicio3()
ejercicio3.leer_horas_trabajadas()
ejercicio3.leer_tarifa()
print("El salario total es: ", ejercicio3.calcular_sueldo())
