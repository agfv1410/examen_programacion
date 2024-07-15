from os import system
from random import randint
system("cls")
trabajadores=["Juan perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
sueldos=[]
sueldo=[]
trabajadores_sueldo=[]
trabajadores_total=[]
menor=0
medio=0
mayor=0
i=0
def asignar():
    sueldos=[]
    trabajadores_total=[]
    trabajadores_sueldo=[]
    for i in range(10):
        sueldo=0
        sueldo=randint(300000,2500000)
        sueldos.append(sueldo)
        trabajadores_sueldo.append(trabajadores[i])
        trabajadores_sueldo.append(sueldo)
        trabajadores_total.append(trabajadores_sueldo)
        trabajadores_sueldo=[]
    print(trabajadores_total)

    print(sueldos)
    
    return sueldos,trabajadores_total,trabajadores_sueldo,sueldo

def clasificar():
    for i, trabajadores_sueldo in enumerate(trabajadores_total,1):
        if trabajadores_total[1]<=800000:
            menor=menor+1
            print("Sueldos menores a $800.000\n ","TOTAL: ",menor)
            print("nombre del empleado","         ","sueldo\n ",trabajadores_sueldo[0],"         ",trabajadores_total[1])
        elif trabajadores_total[1]>800000 and trabajadores_total[1]<2000000:
            medio=medio+1
            print("Sueldos entre  $800.000 y $2.000.000\n","TOTAL: ",medio)
            print("nombre del empleado","         ","sueldo\n ",trabajadores_sueldo[0],"         ",trabajadores_total[1])
        else:
            mayor=mayor+1
            print("Sueldos superiores a $2.000.000\n ","TOTAL: ",mayor)
            print("nombre del empleado","         ","sueldo\n ",trabajadores_sueldo[0],"         ",trabajadores_total[1])


def estadisticas():
    sueldo_max=1
    sueldo_min=9999999999999
    promedio=0

    for a in range(len(sueldos)):
        print(a)
        if sueldo_max<sueldos[a]:
            sueldo_max=sueldos
            
    print("el sueldo mas alto es:",sueldo_max)

    for a in range(len(sueldos)):
        if sueldo_min<sueldos[a]:
            sueldo_min=sueldo
    print("el sueldo mas bajo es:",sueldo_min)
    
    for a in range(len(sueldos)):
        print(a)
        promedio=promedio+sueldo
    print("el promedio es:",promedio/10)

        
