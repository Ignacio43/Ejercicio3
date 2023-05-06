from clases3 import Registro
import csv
import main3

def crear_lista():
    matriz=[]
    for dia in range(30):
        fila=[]
        matriz.append(fila)
        for hora in range(24):
            fila.append([])
    return matriz
    
def AlmacenarMatriz():
    p=[]
    p=crear_lista()
    with open("archi.txt","r")as archivo:
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader: 
            dia=int(fila[0])-1
            hora=int(fila[1])
            temperatura=float(fila[2])
            humedad=float(fila[3])
            presion=float(fila[4])
            registro=Registro(temperatura,humedad,presion)
            p[dia][hora].append(registro)
    return p

# Opcion 1

def mayor_valor_temperatura(p):
    max=-1
    for dia in range(30):
        for hora in range(24):
            if p[dia][hora].get_temperatura()>max:
                max=p[dia][hora].get_temperatura()
                j=p[dia][hora].get_temperatura()
    print(f"en el dia {dia+1} a las {hora} horas alcanzo la maxima temperatura que es {j} \n")

def menor_valor_temperatura(p):    
    min=10000
    for dia in range(30):
        for hora in range(24):
            if p[dia][hora].get_temperatura()<min:
                min=p[dia][hora].get_temperatura()
                j=p[dia][hora].get_temperatura()
    print(f"en el dia {dia+1} a las {hora} horas alcanzo la minima temperatura que es {j} \n")
    
def mayor_valor_humedad(p):
    max=-10
    for dia in range(30):
        for hora in range(24):
            if p[dia][hora].get_humedad()>max:
                max=p[dia][hora].get_humedad()
                j=p[dia][hora].get_humedad()
    print(f"en el dia {dia+1} a las {hora} horas alcanzo la maxima humedad que es {j} \n")

def menor_valor_humedad(p):  
    min=10000
    for dia in range(30):
        for hora in range(24):
            if p[dia][hora].get_humedad()<min:
                min=p[dia][hora].get_humedad()
                j=p[dia][hora].get_humedad()
    print(f"en el dia {dia+1} a las {hora} horas alcanzo la minima humedad que es {j} \n")
    
def mayor_valor_presion(p):
    max=-10
    for dia in range(30):
        for hora in range(24):
            if p[dia][hora].get_presion()>max:
                max=p[dia][hora].get_presion()
                j=p[dia][hora].get_presion()
    print(f"en el dia {dia+1} a las {hora} horas alcanzo la maxima presion que es {j} \n")

def menor_valor_presion(p):  
    min=10000
    for dia in range(30):
        for hora in range(24):
            if p[dia][hora].get_presion()<min:
                min=p[dia][hora].get_presion()
                j=p[dia][hora].get_presion()
    print(f"en el dia {dia+1} a las {hora} horas alcanzo la minima presion que es {j} \n")
    
    #Opcion 2
    
def prom_mensual_horas(p):
    h=0
    for dia in range(30):
        for hora in range(24):
            h=h+p[dia][hora].get_temperatura()
    return h/720

    #Opcion 3
    
def listar(p):
    dia=input("ingrese el dia a listar")    
    for hora in range(24):
        print(f"{hora:5} {p[dia][hora].get_temperatura():5} {p[dia][hora].get_humedad():5} {p[dia][hora].get_presion():5} \n ")