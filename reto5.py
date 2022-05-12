from os import system                                                                         # se importa una libreria para limpiar pantalla con el metodo system
from time import sleep                                                                                  # se importa una libreria para controlar mediante tiempo lo que aparecera en pantalla 
from math import sin, cos, asin, radians, sqrt                                                          # se importa una libreria para ejecutar operaciones matematicas
id=51747                                                                                                # usuario guardado 
pw=74715                                                                                                #  contraseña guardada 
cont=0                                                                                                  # se inicia el contador en '0' para los intentos fallidos 
conf1=4                                                                                                 # respuesta de la primera adivinanza para validar la contraseña
conf2=7                                                                                                 # respuesta de la segunda adivinanza para validar la contraseña
term1=747                                                                                               # primer sumando del captcha
term2=int((5**2+7)/(5*2-2))                                                                             # segundo sumando del captcha
captcha=term1+term2                                                                                     # operación para obtener la suma que constituye el captcha
coords = []  
system('cls')                                                                                           # se iniciar una matriz vacía para las coordonadas de ubicaciones más frecuentes definidas por el usuario
print(" \3 Bienvenido al sistema de ubicación para zonas públicas WIFI \3 ")                                  # Se da la bienvenida al sistema cuando se inicia el código
login=int(input('Por favor, ingrese el Usuario:  '))                                                    # Se solicita el usuario  para inicio de sesión
if login==id:                                                                                           # Se valida el usuario    
    system('cls')                                                                                       # Se limpia pantalla
    pase=int(input('A continuación ingrese su contraseña:  '))                                          # Se solicita la contraseña
    if pase==pw:
        system('cls')                                                                                   # Se valida la contraseña
        verificacion=int(input(f'A continuación, resuelva la siguiente suma: {term1}+{term2}=  '))      # Solicitar captcha 
        if verificacion==captcha:                                                                       # Validación de captcha, si es correcta
            system('cls')                                                                               
            print('Sesión iniciada')                                                                    # Muestra mensaje de captcha aprobada
            print("Bienvenido a TicNet")                                                                 # Mensaje de Bienvenida
            opciones = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", \
"Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", \
"Elegir opción de menú favorita","Cerrar sesión"]                                                        # Lista de opciones de menú
            while cont<3:                                                                                # Se inicia el ciclo de oportunidades para ejecutar correctamente el menú.\
                for i in range(1,8):                                                                     # El usuario puede equivocarse 3 veces como máximo en la selección de las opciones
                    print(f"{i}. {opciones[i-1]}")                                                       # Se imprimen las opciones de menú de manera iterativa extrayendo el contenido de la lista opciones
                lula= input('Elija una opción:   ')                                                      # se almacena la opción de menú elegida
                if lula=='1':                                                                            # Se compara la opción elegida con la opcion 1 del menu
                    system("cls")
                    print(f'Usted ha elegido la opción {lula}')                                          # Se informa de la elección de menú realizada
                    verificacion = int(input("Confirmar contraseña actual : "))                          # Se solicita nuevamente contraseña actual para poder cambiarla
                    if verificacion == pw :                                                              # Se valida la contraseña actual
                        npw = int(input("Ingrese nueva contraseña : "))                                  # Se ingresa la nueva contraseña
                        pw = npw 
                        system("cls")
                        continue
                    else:
                        print("Error")
                        sleep(1)
                        exit()
                elif lula=='2':
                    print(f'Usted ha elegido la opción {lula}')
                    sleep(1)
                    system('cls')
                    latMay = 2.766
                    latMin = 2.548
                    lonMay = - 76.493
                    lonMin = - 76.879
                    if coords == []:
                        system('cls')
                        for i in range(3):
                            coords.append([])                      
                            for j in range(2):
                                coords[i].append(None)
                        for i in range(3):
                            for j in range(2):
                                if j == 0:
                                    datoCoord = input(f"Ingrese Latitud {i+1}: ")       
                                    try:                                                
                                        datoCoord = float(datoCoord)
                                    except:                                            
                                        print("Error coordenada")  
                                        sleep(1)                           
                                        exit()
                                    if datoCoord >= latMin and  datoCoord <= latMay:      
                                        coords[i][j]=datoCoord                         
                                    else:
                                        print("Error coordenada")
                                        sleep(1)
                                        exit()
                                elif j==1:
                                    datolong = input(f"Ingrese Longitud {i+1}: ")
                                    try:
                                        datolong = float(datolong)
                                    except:
                                        print("Error coordenada")
                                        sleep()
                                        exit()            
                                    if datolong >= lonMin and  datolong <= lonMay:
                                        coords[i][j]=datolong
                                    else:
                                        print("Error coordenada")
                                        sleep(1)
                                        exit()
                    else:
                        for i in range(3):
                            print(f"coordenada [latitud,longitud] {i+1} : {coords[i]}")
                        longs =[]
                        for i in range(3):                                                 
                            longs.append(coords[i][1])                  
                        masOrV = max(longs)                   
                        masOrI = longs.index(masOrV)          
                        masOccV = min(longs)                   
                        masOccI = longs.index(masOccV)
                        print(f"la coordenada {masOrI+1} es la que está más al oriente")
                        print(f"la coordenada {masOccI+1} es la que está más al occidente")
                        actualizar = int(input("Presione 1,2 o 3 para actualizar la respectiva coordenadas \
presione 0 para regresar al menu : "))
                        system("cls")
                        if actualizar == 0 :
                            pass
                        elif actualizar == 1 :
                            newLat = float(input("Ingrese latitud de trabajo : "))
                            if newLat >= latMin and  newLat <= latMay:
                                coords[0][0] = newLat
                                newLog = float(input("Ingrese longitud de trabajo : "))
                                if newLog >= lonMin and  newLog <= lonMay:    
                                    coords[0][1] = newLog
                                else:
                                    print("Error actualización")
                                    sleep()
                                    exit()
                                pass
                            else:
                                print("Error actualización")
                                sleep()
                                exit()
                                pass
                        elif actualizar == 2 :
                            newLat = float(input("Ingrese latitud de casa : "))
                            if newLat >= latMin and  newLat <= latMay:
                                coords[1][0] = newLat
                                newLog = float(input("Ingrese longitud de casa : "))
                                if newLog >= lonMin and  newLog <= lonMay:    
                                    coords[1][1] = newLog
                                else:
                                    print("Error actualización")
                                    sleep()
                                    exit()
                            else:
                                print("Error actualización")
                                sleep(1)
                                exit()
                        elif actualizar == 3 :
                            newLat = float(input("Ingrese latitud de parque : "))
                            if newLat >= latMin and  newLat <= latMay:
                                coords[2][0] = newLat
                                newLog = float(input("Ingrese longitud de parque : "))
                                if newLog >= lonMin and  newLog <= lonMay:    
                                    coords[2][1] = newLog
                                else:
                                    print("Error actualizaión")
                                    sleep(1)
                                    exit()
                            else:
                                print("Error actualización")
                                sleep(1)
                                exit()
                        else:
                            print('Error ubicación')
                            sleep(1)
                            exit()
                elif lula=='3':
                    system('cls')
                    print(f'Usted ha elegido la opción {lula}')
                    if coords == [] :
                        print("Error sin registro de coordenadas")
                        sleep(1)     
                        exit()
                    else :
                        for i in range(3):                                                  
                            print(f"coordenada [latitud,longitud] {i+1} : {coords[i]}")
                        ubi_actual = int(input("Elija su ubicación actual (1, 2 ó 3) para calcular la distancia a los puntos de conexión:  "))
                        system('cls')
                        zonas = [[2.698 , -76.680 , 63], 
                                [2.724 , -76.693 , 20],
                                [2.606 , -76.742 , 680],  # Esta matriz predeterminada corresponde a las ubicaciones de wifi dentro de rango solicitado
                                [2.698 , -76.690 , 15]] 
                        def calcDist(filaZona, filaCoords):
                                #punto 1: usuario; punto 2: zona WiFi o punto 2: usuario; punto 1: zona WiFi
                            R= (6372.795477598) * 1000.0
                            lat1 = radians(filaZona[0])
                            lat2 = radians(filaCoords[0])
                            lon1 = radians(filaZona[1])
                            lon2 = radians(filaCoords[1])
                            diflon =  lon2 - lon1      #delta de longitudes
                            diflat =  lat2 - lat1      #delta de latitudes
                            # calculo de formula de distancia segmentada
                            auxC = (sin(diflon/2))**2
                            auxC = auxC * cos(lat2)
                            auxC = auxC * cos(lat1)
                            auxC = auxC + (sin(diflat/2))**2
                            auxC = sqrt (auxC)
                            auxC = asin (auxC)
                            dist = auxC * 2 * R
                            return dist
                        if ubi_actual == 1 :
                            d1 = calcDist(zonas[0] , coords[0])
                            d2 = calcDist(zonas[1] , coords[0])
                            d3 = calcDist(zonas[2] , coords[0])
                            d4 = calcDist(zonas[3] , coords[0])
                        elif ubi_actual == 2 :
                            d1 = calcDist(zonas[0] , coords[1])
                            d2 = calcDist(zonas[1] , coords[1])
                            d3 = calcDist(zonas[2] , coords[1])
                            d4 = calcDist(zonas[3] , coords[1])
                        elif ubi_actual == 3 :
                            d1 = calcDist(zonas[0] , coords[2])
                            d2 = calcDist(zonas[1] , coords[2])
                            d3 = calcDist(zonas[2] , coords[2])
                            d4 = calcDist(zonas[3] , coords[2])
                        elif ubi_actual >= 4 or ubi_actual==0:
                            print("Error ubicación")
                            sleep(2)
                            exit()
                        dists = [d1,d2,d3,d4]               #listas con todas las distancias a los puntos WiFi
                        distsCopy = dists[:]
                        distsCopy.sort()
                        #primera distancia menor con su posición original
                        menor1Val = distsCopy[0]
                        menor1Pos = dists.index(menor1Val)
                        #segunda menor distancia con su posición original
                        menor2Val = distsCopy[1]
                        menor2Pos = dists.index(menor2Val)
                        #matriz con zonas wifi de menos usuarios
                        zonasMenosVis = []                                     
                        if zonas[menor2Pos][2] > zonas[menor1Pos][2]:         #pregunto si la menor1 tiene más usarios que la menor2      
                            zonasMenosVis.append(zonas[menor1Pos])              #dependiendo de eso se agregar las sublistas en un orden
                            zonasMenosVis[0].append(dists[menor1Pos])          #expansión de matriz con sus respectivas distancias 
                            zonasMenosVis.append(zonas[menor2Pos])
                            zonasMenosVis[1].append(dists[menor2Pos])          #expansión de matriz con sus respectivas distancias 
                        elif zonas[menor1Pos][2] > zonas[menor2Pos][2]:       #pregunto si la menor2 tiene más usarios que la menor1      
                            zonasMenosVis.append(zonas[menor2Pos])              #dependiendo de eso se agregar las sublistas en un orden contrario al anterior
                            zonasMenosVis[0].append(dists[menor2Pos])          #expansión de matriz con sus respectivas distancias 
                            zonasMenosVis.append(zonas[menor1Pos])
                            zonasMenosVis[1].append(dists[menor1Pos])
                        print("Zonas WiFi cercanas con menores usuarios")
                        print(f"La zona WiFi 1: ubicada en {zonasMenosVis[0][0],zonasMenosVis[0][1]} a \
    {round(zonasMenosVis[0][3],3)} metros tiene un promedio de {zonasMenosVis[0][2]} usuarios")
                        print(f"La zona WiFi 2: ubicada en {zonasMenosVis[1][0], zonasMenosVis[1][1]} a \
    {round(zonasMenosVis[1][3],3)} metros tiene un promedio de {zonasMenosVis[1][2]} usuarios")                   
                        destino = int(input("Elija 1 o 2 para recibir indicaciones de llegada:"))
                        if destino == 1 or destino == 2 :
                            direc=coords[ubi_actual-1][1]-zonasMenosVis[destino-1][1]
                            if destino == 1 :
                                tiempo_llegada = round((zonasMenosVis[0][3] / 0.483) / 60,2)
                                if direc<0:
                                    print(f"Vaya hacia el Este. El tiempo que tardara caminando son {tiempo_llegada} minutos")
                                elif direc>0:
                                    print(f"Vaya hacia el Oeste. El tiempo que tardara caminando son {tiempo_llegada} minutos")
                                tiempo_llegada = round((zonasMenosVis[0][3] /  20.83 ) / 60,2)
                                if direc<0:
                                    print(f"Vaya hacia el Este.El tiempo que tardara en auto son {tiempo_llegada} minutos")
                                elif direc>0:
                                    print(f"Vaya hacia el Oeste.El tiempo que tardara en auto son {tiempo_llegada} minutos")
                            elif destino==2:
                                tiempo_llegada = round((zonasMenosVis[1][3] / 0.483) / 60,2)
                                if direc<0:
                                    print(f"Vaya hacia el Este. El tiempo que tardara caminando son {tiempo_llegada} minutos")
                                elif direc>0:
                                    print(f"Vaya hacia el Oeste. El tiempo que tardara caminando son {tiempo_llegada} minutos")
                                tiempo_llegada = round((zonasMenosVis[1][3] / 20.83 ) / 60,2)
                                if direc<0:
                                    print(f"Vaya hacia el Este. El tiempo que tardara en auto son {tiempo_llegada} minutos")
                                elif direc>0:
                                    print(f"Vaya hacia el Oeste. El tiempo que tardara en auto son {tiempo_llegada} minutos")
                            salir=input('Presione 0 para salir: ')
                            if salir=='0':
                                system('cls')
                                continue
                        else:
                            print('Error zona wifi')    
                            sleep(2)
                            exit()
                elif lula=='4':
                    system('cls')
                    if coords == [] :
                        print("Error de alistamiento")
                        sleep(1)     
                        exit()
                    actual=[]
                    for i in range (3):
                        if ubi_actual == i+1:
                            actual.append(coords[i])
                            distancia_1=round(zonasMenosVis[i][3],2)
                            
                    informacion = {
                        "actual" : actual , 
                        "zonawifi1" : [ zonasMenosVis[0][0] , zonasMenosVis[0][1] , zonasMenosVis[0][2] ] , 
                        "recorrido" : [distancia_1 , '2' , tiempo_llegada ]}
                    print(informacion)
                    print( "¿Está de acuerdo con la información a exportar?" )
                    seleccion = int(input( "Presione 1 para confirmar, 0 para regresar al menú principal" ))
                    system("cls")
                    if seleccion == 1 :
                        mi_archivo = open("actualizar_info.txt","w",encoding="utf8")
                        for clave,valor in informacion.items(): 
                            svn=f'{clave} {valor}\n'
                            mi_archivo.write(svn)
                        mi_archivo.close()
                        print("Exportando archivo")
                        sleep(2)
                        exit()
                    if seleccion == 0 :
                        sleep(1)
                        system("cls")
                        continue
                elif lula=='5':
                    print(f'Usted ha elegido la opción {lula}')
                    pregunta_5 = int(input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal"))
                    if pregunta_5 == 0 :
                        sleep(2)
                        system('cls')
                        continue
                elif lula=='6':
                    cont=0
                    opcionesCopy = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", \
"Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", \
"Elegir opción de menú favorita","Cerrar sesión"]
                    system('cls')
                    for i in range(1,8):
                        print(f"{i}. {opciones[i-1]}")
                    lulafav=int(input('Seleccione opción favorita:'))
                    if lulafav>=1 and lulafav<6:
                        system('cls')
                        resp1=int(input('El doble y el cuadrado del numero 2 es:'))
                        if resp1==4:
                            system('cls')
                            resp2=int(input('El numero que sigue al 6 en forma ascendente es:'))
                            if resp2==7:
                                system('cls')
                                if lulafav == 1:
                                    pass
                                elif lulafav == 2:
                                    opciones[0] = opcionesCopy[1]
                                    opciones[1] = opcionesCopy[0]
                                elif lulafav== 3:
                                    opciones[0] = opcionesCopy[2]   
                                    opciones[1] = opcionesCopy[0]
                                    opciones[2] = opcionesCopy[1]
                                elif lulafav== 4:
                                    opciones[0] = opcionesCopy[3]
                                    opciones[1] = opcionesCopy[0]
                                    opciones[2] = opcionesCopy[1]
                                    opciones[3] = opcionesCopy[2]
                                elif lulafav== 5:
                                    opciones[0] = opcionesCopy[4]
                                    opciones[1] = opcionesCopy[0]
                                    opciones[2] = opcionesCopy[1]
                                    opciones[3] = opcionesCopy[2]
                                    opciones[4] = opcionesCopy[3]        
                            else:
                                system('cls')
                                print('Error')
                                sleep(1)
                        else:
                            system('cls')
                            print('Error')
                            sleep(1)
                    elif lulafav==6:
                        print('Error')
                        sleep(1)
                        exit()
                    elif lulafav== 7:
                        system('cls')
                        print('"Hasta pronto"')
                        sleep(1)
                        exit()
                elif lula=='7':
                    system('cls')
                    print('Hasta pronto')
                    sleep(1)
                    exit()
                else:
                    system('cls')
                    print('Error')
                    sleep(1)
                    cont+=1
        else:
            print('Error')
            exit()
    else:
        print('Error')
        exit()
else:
    print('Error')
    print('Usuario no válido')
    exit()  