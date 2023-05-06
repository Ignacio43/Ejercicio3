import funciones3
from clases3 import Registro


#Ej 1/2
matriz= AlmacenarMatriz()


if __name__=='__main__':
   
    # Ej 3
    menu=input("1. Mostrar para cada variable el día y hora de menor y mayor valor.\n 2. Indicar la temperatura promedio mensual por cada hora.\n3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.\n0. Salir\n")  
    while(menu!=0):
        if menu==1:
            mayor_valor_temperatura(matriz)
            menor_valor_temperatura(matriz)
            mayor_valor_huemedad(matriz)
            menor_valor_humedad(matriz)
            mayor_valor_presion(matriz)
            menor_valor_presion(matriz)
        elif menu==2:
            print(f"la temperatura mensual promedio por cada hora es de {prom_mensual_horas(matriz)}  ")
        elif menu ==3:
            listar(matriz)  
        menu=input("1. Mostrar para cada variable el día y hora de menor y mayor valor.\n 2. Indicar la temperatura promedio mensual por cada hora.\n3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.\n0. Salir\n")