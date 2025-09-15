#Un instituto de inglés necesita un programa que le permita, cada día procesar observaciones sobre las clases
#de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases un dia de la semana
#diferente: los lunes se dicta nivel inicial, los martes nivel intermedio, los miércoles el nivel avanzado, los jueves
#son para práctica hablada y los viernes se dicta inglés para viajeros.
# Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM" donde [día] es un día de la 
# semana, DD es el número de día y MM es el número del mes. Si el usuario ingresa un día de la semana inexistente o una fecha
# cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error.
# Debe permitirse que ingrese el dia de la semana en minúsculas o mayúsculas indistintamente. Como condición se tiene 
# que lo ingresado por el usuario tendrá la forma<[alfenumérico],[numérico]/[numérico]>.
# Una vez indicada la fecha por el usuario necesita poder indicar si ese dia se tomaron los exámenes, pero eso solo si se trata
# de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés viajero no tienen examenes
#el usuario ingresara cuántos alumnos aprobaron y cuantos no, y el programa le mostrará el porcentaje de alumnos aprobados
#Si el dia fue el correspondiente a la práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase
#y el programa indicará asistío la mayoria en caso de que la asistencia sea mayor al 50% o no asistío la mayoria si no es asi
#Si se trata del inglés para viajeros y la fecha actual corresponde a la del día 1 del mes 1 o del mes 7, se deberá imprimir
#comienzo de nuevo ciclo y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada
#alumno, para luego imprimir el ingreso total en $.


#1)_ Se solicitan los datos del dia:

dia_semana=input("Ingrese el dia de la semana(Lunes,Martes,Miercoles,Jueves,Viernes):").lower()
fecha_actual_ddmmyy=input("Ingrese la fecha actual en formato DDMmYY:")
dia_mes=int(fecha_actual_ddmmyy[0:2])
mes=int(fecha_actual_ddmmyy[2:4])
anio=int(fecha_actual_ddmmyy[4:6])

#2)_Validación de la fecha y el dia de la semana

fecha_valida=True
if mes>12 or mes<1:
    print("Error: El mes es incorrecto.")
    fecha_valida=False
elif dia_mes>31 or dia_mes<1:
    print("Error: El día es incorrecto.")
    fecha_valida=False
elif dia_semana not in ["Lunes","Martes","Miercoles","Jueves","Viernes"]:
    print("Error:El dia de la semana no existe en el programa.")
    fecha_valida=False

#3)_Continuar sólo si el día y la fecha son válidos 

if fecha_valida:
    print(f"\n Procesando las observaciones para el dia {dia_semana.capitalize()}...")

#4)_Lunes,Martes y miercoles: clases inicial, intermedio y avanzado

if dia_semana=="lunes" or dia_semana=="martes" or dia_semana=="miercoles":
    print("\n Se porcesarán los exámenes del día.")
    cantidad_examenes=int(input("Ingrese la cantidad de examenes tomados:"))
    examenes_aprobados=0
    examenes_desaprobados=0

#5)_ Aca es donde ¡NO! debo usar el bucle while :(

i=1
if i<= cantidad_examenes:
    aprobado=input(f"¿El examen{i} fue aprobado?(si/no):").lower()
    if aprobado=="si":
        examenes_aprobados=examenes_aprobados+1
        i=i+1
        if i<= cantidad_examenes:
            aprobado=input(f"¿El examen{i} fue aprobado?(si/no):").lower()
            if aprobado=="si":
               examenes_aprobados=examenes_aprobados+1
               i=i+1
               if i<= cantidad_examenes:
                  aprobado=input(f"¿El examen{i} fue aprobado?(si/no):").lower()
                  if aprobado=="si":
                     examenes_aprobados=examenes_aprobados+1
                     i=i+1
                     if i<= cantidad_examenes:
                        aprobado=input(f"¿El examen{i} fue aprobado?(si/no):").lower()
                        if aprobado=="si":
                            examenes_aprobados=examenes_aprobados+1
                            i=i+1
                     else:
                      porcentaje_aprobados=(examenes_aprobados/cantidad_examenes)*100
                      print(f"\n El porcentaje de alumnos aprobados es:{porcentaje_aprobados}%")
            else:
               porcentaje_aprobados=(examenes_aprobados/cantidad_examenes)*100
               print(f"\n El porcentaje de alumnos aprobados es:{porcentaje_aprobados}%")

        else:
             porcentaje_aprobados=(examenes_aprobados/cantidad_examenes)*100
             print(f"\n El porcentaje de alumnos aprobados es:{porcentaje_aprobados}%")
else:
    porcentaje_aprobados=(examenes_aprobados/cantidad_examenes)*100
    print(f"\n El porcentaje de alumnos aprobados es:{porcentaje_aprobados}%")
        

        



#6)_Jueves: clase de oratoria

if dia_semana=="jueves":
    print("\n Se procesarán las clases de oratoria.")
    porcentaje_asistencia=float(input("Ingrese el porcentaje de asistencia a la clase:"))
    if porcentaje_asistencia>50:
        print("¡Asistió la mayoria!")
    else:
        print("No asistió la mayoria")

#7)_Viernes: práctica para viajeros
elif dia_semana=="viernes":
    print("\n Se procesaran las clases de inglés para viajeros.")

#8)_Lógica del calculo del precio

if mes==1 or mes==7:
    print("Se procesará un nuevo ciclo de práctica para viajeros.")
    alumnos_nuevos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo:"))
    arancel_nuevo_ciclo=int(input("Ingrese el monto que abonarán los ingresantes del nuevo ciclo:"))
    total_recaudado=alumnos_nuevos*arancel_nuevo_ciclo
    print(f"EL ingreso total del nuevo ciclo es de:${total_recaudado}")
else:
    print("No se procesan nuevos cursos para viajeros este mes.")

