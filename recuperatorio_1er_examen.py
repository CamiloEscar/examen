from jurassic_park import dinosaurs
from lista import Lista
from cola import Cola

def busquedas_dino(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['named_by']

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']

class Jurasic:
    def __init__(self, time, zona, numero_dinosaurio, nivel_alerta, nombre):
        self.time = time
        self.zona = zona
        self.numero_dinosaurio = numero_dinosaurio
        self.nivel_alerta = nivel_alerta
        self.nombre= nombre

    def __str__(self):
        return f"{self.time} | {self.zona} | {self.numero_dinosaurio} | {self.nivel_alerta} | {self.nombre}"


file = open('/home/wr/Escritorio/uader/ALGORITMO/examen/alerts.txt')

lineas = file.readlines()
lineas.pop(0)
lista_jurasic=Lista()
lista_jurasic2=Lista()
for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    lista_jurasic.insertar(Jurasic(dato[0],
                             dato[1],
                             dato[2],
                             dato[3],
                             dato[4]),
                        campo='time')   #lista ordenada por el campo time
    lista_jurasic2.insertar(Jurasic(dato[0],
                             dato[1],
                             dato[2],
                             dato[3],
                             dato[4]),
                        campo='nombre') # lista ordenada por el campo nombre

#lista_jurasic.barrido()

# for nombre in dinosaurs:
#     lista_jurasic.insertar(nombre,'name')

# for i in range(0, lista_jurasic.tamanio()):
#     lista_jurasic.obtener_elemento(i)['name'] = lista_jurasic[i]

# def barridoDino(lista):
#     for i in range (0,lista_jurasic.tamanio()):
#         elemento=lista_jurasic.obtener_elemento(i)
#         print ('nombre: ',elemento['name'])

# lista_jurasic.ordenar('especie')
# barridoDino(lista_jurasic)

# ordenados = sorted(dato['name'])
# print(ordenados)

# #a. listado ordenado por nombre y por especie;
# print('Listado ordenado por nombre:')
# for i in range(lista_jurasic.tamanio()):
#     mostrar_elemento(lista_jurasic, i)

# print()

# # print(dato)
# dato = lista_jurasic.busqueda('hervivoro', 'name')
# if dato:
#     print(f'el dino {dato.info}')
# else:
#     print('el dino no esta en la lista')

'''
Claire Dearing: Ok, encárgate urgente de conseguir a la persona que necesitas, no me importa de
dónde lo saques. Necesito que proceses urgente este archivo con información del parque y esté
disponible en mi monitor de informes. Y no olvide determinar cual de nuestro dinosaurios fuel el
ultimo en ser descubierto y quien lo hizo. [actividad para resolver]'''
print()
print('Claire Dearing: determinar cual de nuestro dinosaurios fue el ultimo en ser descubierto y quien lo hizo')
print()
aux=0
for dino in dinosaurs:
    aux2=int(dino['named_by'][-4:])
    if aux2 > aux:
        aux=int(dino['named_by'][-4:])
for dino in dinosaurs:
    if dino['named_by'][-4:]== str(aux):
        print(f"El ultimo dinosaurio en ser descubierto fue: {dino['name']} y lo hizo: {dino['named_by'][:-6]}")
print()


# def busquedas_ultimo(buscado):
#     for dato in lista_jurasic:
#         if(int(buscado) == dato['named_by']):
#             return dato['1995']
#         print(f'el ultimo dinosaurio fue descubierto en {dato}')

'''Lowery Cruthers: Hola new developer, lamento que no te podamos hacer un presentación formal,
pero necesito que resuelvas esto de inmediato. Por favor debes hacer un scripts que procese el
archivo en esta USB llamado “alerts.txt”, necesito los datos ordenados por fecha para Claire y otro
ordenado por nombre de dinosaurio para cruzarlo con los datos del sistema de incidentes. Por favor
date prisa lo necesito urgente poder listar esta información. Recuerda agregar el nombre del
dinosaurio de acuerdo a su número. [actividad para resolver]'''

print('Lowery Cruthers: datos ordenados por fecha para Claire y otro ordenado por nombre de dinosaurio.')

print('Listado ordenado por hora: ')   
lista_jurasic.barrido()
print()

print('Listado ordenado por dinosaurio: ')
lista_jurasic2.barrido()
print()

# lista_jurasic.barrido_ultima_descubrimiento()
# print()

# lista_jurasic.barrido_coria()

# def citerio(item):
#     return item.nombre

# dinosaurs.sort(key=citerio)

# for dino in dinosaurs:
#     print(dino)

# # # dato = lineas.busqueda('Coria & Salgado, 1995'.title(), 'named_by')
# # # if dato:
# # #     print(f'el ultimo dinosaurio fue descubierto en {dato.info.named_by}')

'''
Dr. Wu: Les dije explícitamente que debemos mantener anónima toda la información respecto de las
zonas WYG075, SXH966 y LYF010 por favor eliminen en este momento toda esa información de los
datos procesados previamente. Ah casi me olvidaba de decirles modifiquen el registro de la zona
HYD195 el nombre correcto del dinosaurio es Mosasaurus. [actividad para resolver]'''

print('Dr. Wu: Eliminar las zonas WYG075, SXH966 y LYF010 y cambiar el registro HYD195 del dino a Mosasaurus')

pos=lista_jurasic.busqueda('WYG075', 'zona')
lista_jurasic.eliminar(pos.info)
pos=lista_jurasic.busqueda('SXH966', 'zona')
lista_jurasic.eliminar(pos.info)
pos=lista_jurasic.busqueda('LYF010', 'zona')
lista_jurasic.eliminar(pos.info)
pos=lista_jurasic.busqueda('HYD195', 'zona')
pos.info.nombre='Mosasaurus'

pos=lista_jurasic2.busqueda('WYG075', 'zona')
lista_jurasic2.eliminar(pos.info)
pos=lista_jurasic2.busqueda('SXH966', 'zona')
lista_jurasic2.eliminar(pos.info)
pos=lista_jurasic2.busqueda('LYF010', 'zona')
lista_jurasic2.eliminar(pos.info)
pos=lista_jurasic2.busqueda('HYD195', 'zona')
pos.info.nombre='Mosasaurus'


# dato = lista_jurasic.eliminar('WYG075'.title(), 'named_by')
# if dato:
#     print(f'el superheroes {dato.named_by} fue eliminado')


#dato.pop(busquedas(dato[int('WYG075')]))
#lineas.remove(int('WYG075'))
#lineas.pop(1)
# lineas.pop(int('SXH966'))
# lineas.pop(int('LYF010'))
#print(dato)

# def eliminarEnLista(lineas):
#     n=str("WYG075")
#     try:
#         lineas.remove(n)
#         dato = linea.split(';')
#         dato[3] = dato[3][:-1]
#         print(lineas)
#     except ValueError:
#         print('{} no se encuentra en la lista'.format(n))
# eliminarEnLista(lineas) 

'''
Simon Masrani: Oigan donde rayos se encuentra Claire, necesito que se encargue de la presentación
de la nueva atracción del parque, además el teléfono de emergencias no para de sonar. Oye tu amigo,
si tú el developer no recuerdo tu nombre pero debes ser el nuevo podrías atender el teléfono parece
ser algo importante y no veo a Lowery por ningún lado. Necesito urgente un listado filtrado de los
datos que solo incluya datos de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con
nivel  ́critical" o "high". [actividad para resolver]'''

print('Simon Masrani: Listado de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel critical o high: ')
lista_jurasic.barrido_tyrano_spino_giga()
print()

#print(lista1)

# dato = dato[3]
# if (dato[3] == 'critical' or dato[3] == 'high' and dato[4] =='Tyrannosaurus Rex'):
#     print('jeje')

# if (dato[3] == 'critical' or dato[3] == 'high' and dato[4] =='Spinosaurus'):
#     print('hola')

# if (dato[3] == 'critical' or dato[3] == 'high' and dato[4] =='Giganotosaurus'):
#     print('beob')



'''Victor Hoskins: Pero que está pasando llevo un tiempo intentando comunicarme, las alarmas de
incidentes están como locas, no sé a qué lugar debo ir primero con mi equipo de contención. Necesito
que tomes toda la información de alertas, y las insertes en dos colas, una con los datos de dinosaurios
carnívoros y otra con los herbívoros, descarten las de nivel "low" y "medium". [actividad para resolver]'''

cola_carnivoros=Cola()
cola_herbivoros=Cola()
for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    if dato[3] != 'low' and dato[3] != 'medium':
        aux=dato[4]
        for dinosaurio in dinosaurs:
            if aux==dinosaurio['name'] and dinosaurio['type']=='carnívoro ':
                cola_carnivoros.arribo(Jurasic(dato[0],
                                        dato[1],
                                        dato[2],
                                        dato[3],
                                        dato[4]))
            else:
                if aux==dinosaurio['name'] and dinosaurio['type']=='herbívoro ':
                    cola_herbivoros.arribo(Jurasic(dato[0],
                                            dato[1],
                                            dato[2],
                                            dato[3],
                                            dato[4]))

# cola0=Cola()
# cola1= Cola()
# cola2 = Cola()
# cola3 = Cola()

# for (a, b, c, d, e) in dinosaurs:
#     personaje = Jurasic(a, b, c, d, e)
#     cola0.arribo(personaje)

# while not cola0.cola_vacia():
#     x = cola0.atencion()
#     if (x.type =='carnívoro' or x.type =='herbívoro'):
#         cola1.arribo(x)
#     if (x.alert_level == 'low' or x.alert_level == 'medium'):
#         cola2.arribo(x)
#     else:
#         cola3.arribo(x) 

# while (not cola2.cola_vacia()):
#     print (cola2.atencion().alert_level)    



# # # def eliminarEnLista(lineas):
# # #     n=str("low")
# # #     try:
# # #         lineas.remove(n)
# # #         dato = linea.split(';')
# # #         dato[3] = dato[3][:-1]
# # #         print(lineas)
# # #     except ValueError:
# # #         print('{} no se encuentra en la lista'.format(n))
# # # eliminarEnLista(lineas) 

# # # from collections import deque
# # # print(dato[2])
# # # if dato[4] == 'carnivoros':

# # #     data = [lineas]
# # #     carniv = deque(data)
# # #     print(carniv)



'''Agente de Contención: Atención centro de monitoro no podemos acceder al sistema de colas de
alertas por un aparente problema de conexión, atiendan las alertas en la cola de carnívoros y muestren
en la pantalla (para que se publiquen en el canal de alerta de banda segura) la información pero
descarten las provenientes de la zona EPC944, ya se encuentra una unidad de respaldo ahí. [actividad
para resolver]'''

print()
print('Agente de Contención: Carnívoros exceptuando los de nivel low o medium y los provenientes de la zona EPC944: ')
while not cola_carnivoros.cola_vacia():
    dato=cola_carnivoros.atencion()
    if dato.zona!= 'EPC944':
        print(dato)
print()

#print('Herbívoros: ')
#while not cola_herbivoros.cola_vacia():
#    dato=cola_herbivoros.atencion()
#    print(dato)

# print ('DInosaurios carnivoros:')
# while (not cola1.cola_vacia()):
#     if dato[1] != 'EPC944':
#         print (cola1.atencion())



'''Owen Grady: Oigan perdón que los molestes, pero no consigo que el sistema me funcione en mi
notebook, podrían pasarme un listado de toda la información que tienen procesada del archivo, pero
solo de los dinosaurios Raptors y Carnotaurus; y los códigos de las zonas donde puedo encontrar
dinosaurios Compsognathus. Que sea lo antes posible hoy es un día muy agitado.'''

print('Owen Grady: Listado de los dinosaurios dinosaurios Raptors y Carnotaurus y los códigos de las zonas donde puedo encontrar Compsognathus: ')
print()
lista_jurasic.barrido_raptors_carno()
print()

# print('Compsognathus:')
# for i in range (lista_jurasic.tamanio()):
#     dino = lista_jurasic.obtener_elemento(i)
#     if ('Compsognathus' in dino['name']):
#         print(dino['name'], '- en zona:', dino['zone_alert'])
# print()

# dato = lista_jurasic.busqueda('Compsognathus')
#     print(f'Dinosaurios Compsognathus se encuentra en :', dato[1])


# dato = lista_jurasic.busqueda('Raptors', 'Carnotaurus')
# if dato:
#     print(f'Dinosaurios: {dato.info}')
# else:
#     print('el dino no esta en la lista')



'''Lowery Cruthers: Oye amigo sé que es tu primer día y has hecho un excelente trabajo, pero tengo una
tarea más para ti, el viejo analista de Jurassic Park, Nedry, si el que causo todos los problemas, oculto
una imagen del lugar donde escondió una USB con información muy valiosa para nosotros; pero la
imagen está protegida y no conseguimos descifrar la clave. Lo único que tenemos son algunas
anotaciones que estaban en su terminal de trabajo, quizás podrías darle una mirada y ver si se te
ocurre algo que nos permita obtener la contraseña.'''

'''Dennis Nedry (anotaciones): desde que Jurassic Park arranco la calve a ha sido 'mosquito' pero que
significa esto realmente, si lo consideramos como si fueran números estas serian las situaciones:
1. si el número está entre 33 y 47 su valor alfanumérico esta ok.
2. caso contrario
si número es divisible por 3 entonces (número // 2) + 9 (es tu nuevo valor alfanumérico)
sino número -14 (es tu nuevo valor alfanumérico)
en cualquiera de los casos debes continuar procesandolo, es una solución parcial.
3. al final obtendrás la clave si sabes cómo hacer las cosas, pero recuerda 'mosquito' es la clave
de todo.
Suerte intentado descifrar la contraseña. [actividad para resolver]'''

# def mosqui (numero):
#     mosquito = {'M':1,'O':5,'S':4, 'Q':6, 'U':3, 'I':12, 'T':1, 'O':3, 
#     'A':1,'B':5,'C':4, 'D':6, 'E':3, 'F':12, 'G':1, 'H':3, 'N':3,
#     'J':1,'K':5,'L':4, 'P':6, 'R':3, 'U':12, 'W':1, 'X':3, 'Y':12, 'Z':1}
#     if (numero == 'M'):
#         return 1
#     elif numero in mosquito: 
#         return mosquito[numero]
#     elif mosquito[numero[0]]>=mosquito[numero[1]]: 
#         return mosquito[numero[:1]] + mosqui(numero[1:])
#     else:
#         return mosquito[numero[:1]] + mosqui(numero[1:]) 


# numero = input('ingrese contrasena: ')
# numero = numero.upper()
# print (numero, 'en decimal es', mosqui(numero))

def mosqui (numero):
    mosquito = {'M':1,'O':5,'S':4, 'Q':6, 'U':3, 'I':12, 'T':1, 'O':3, 
    'A':1,'B':5,'C':4, 'D':6, 'E':3, 'F':12, 'G':1, 'H':3, 'N':3,
    'J':1,'K':5,'L':4, 'P':6, 'R':3, 'U':12, 'W':1, 'X':3, 'Y':12, 'Z':1}
    if len(mosquito):
        return print(mosquito) 
    elif mosquito % 3 == 0:
        mosquito=(mosquito//2) + 9
    else:
        mosquito=mosquito - 14
    if 33 <= mosquito <= 47:
        mosqui(mosquito)
    #print(f'La clave es: {mosquito}')

numero = input('ingrese contrasena: ')
numero = numero.upper()
print ('en decimal es', mosqui(numero))

# palabra='mosquito'
# vec=[]
# for i in range(len(palabra)):
#     aux= ord(palabra[i])
#     vec.append(aux)

# indice=0
# def obtener_clave(vector, ind):
#     if ind==len(vector):
#         return print(vector) 
#     elif vector[ind] % 3 == 0:
#         vector[ind]=(vector[ind]//2) + 9
#     else:
#         vector[ind]=vector[ind] - 14
#     if 33 <= vector[ind] <= 47:
#         obtener_clave(vector, ind+1)
#     else:
#         obtener_clave(vector, ind)
# print(f'La clave es: {obtener_clave(vec, indice)}')




# def contra(intento=1):
#     respuesta = (" ")
#     if respuesta != "33":
#         if intento < 3:
#             print ("\nFallaste! Inténtalo de nuevo")
#             intento += 1
#             contra(intento) # Llamada recursiva 
#         else:
#             print ("perdiste!")
#     else:
#         print ("Ganaste!")

# numero.contra()



