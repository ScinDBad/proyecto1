#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Adrian!
# 
# Mi nombre es Ezequiel Ferrario, soy code reviewer en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberá hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión.
# </div>
# 
# ¡Empecemos!

# Una empresa de comercio electrónico, Store 1, recientemente comenzó a recopilar datos sobre sus clientes. El objetivo final de Store 1 es comprender mejor el comportamiento de sus clientes y tomar decisiones basadas en datos para mejorar su experiencia online.
# 
# Como parte del equipo de análisis, tu primera tarea es evaluar la calidad de una muestra de datos recopilados y prepararla para futuros análisis.

# # Cuestionario
# 
# Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. Te han pedido que revises los datos recopilados y propongas cambios. A continuación verás datos sobre un usuario o una usuaria en particular; revisa los datos e identifica cualquier posible problema.

# In[ ]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# **Opciones:**
# 
# 1. El tipo de datos para `user_id` debe cambiarse de una cadena a un número entero.
#     
# 2. La variable `user_name` contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
#     
# 3. El tipo de datos de `user_age` es incorrecto.
#     
# 4. La lista `fav_categories` contiene cadenas en mayúsculas. En su lugar, deberíamos convertir los valores de la lista a minúsculas.

# Escribe en la celda Markdown a continuación el número de las opciones que has identificado como problemas. Si has identificado varios problemas, sepáralos con comas. Por ejemplo, si crees que los números 1 y 3 son correctos, escribe 1, 3.

# **Escribe tu respuesta y explica tu argumentación:**
# 2, 3, 4 
# - **[2]** Un nombre de usuario no debería tener espacios en blanco ya que dificultan la gestión de datos como por ejemplo en la búsqueda e interpretación. El subguión intermedio dificulta la separación o diferenciación entre el nombre y apellido.
# 
# 
# - **[3]** Aunque la variable user_age corresponde a un número, sería mejor que fuera de tipo `int` en lugar de `float` ya que no es convencional representar la edad con decimales.
# 
# 
# - **[4]** La lista `fav_categories`al tener su elementos `strings`en mayúsculas puede dificultar la lectura y comprensión ya que visualmente ocupan más espacio. Es una convención que las cadenas de caracteres estén en minúsculas para facilitar su gestión y procesamiento.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente Adrian,</div>

# # Ejercicio 1
# 
# Vamos a implementar los cambios que identificamos. Primero, necesitamos corregir los problemas de la variable `user_name`. Como vimos, tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido; tu objetivo es eliminar los espacios y luego reemplazar el guion bajo con el espacio.

# In[3]:


user_name = ' mike_reed '
user_name = user_name.strip() # eliminar los espacios en la cadena original con el método strip()
user_name = user_name.replace("_"," ") # reemplazar el guion bajo con el espacio en blanco para seprar nombre del apellido

print(user_name) #imprimir la variable user_name 
#----------------------------------------------------------------------------------------------------------------
#para verificar visualmente la correcta limpieza, se puede invocar la variable user_name simplemente
#de esta manera cuando se ejecute se observan las comillas que definen los límites de la cadena de caracteres.


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien.</div>

# # Ejercicio 2
# 
# Luego, debemos dividir el `user_name` (nombre de usuario o usuaria) actualizado en dos subcadenas para obtener una lista que contenga dos valores: la cadena para el nombre y la cadena para el apellido.

# In[7]:


user_name = 'mike reed'
name_split = user_name.split(" ") # divide aquí el string user_name con el método split()

print(name_split) # se imprime la lista que contiene las cadenas correspondientes a nombre y apellido.


# # Ejercicio 3
# 
# ¡Genial! Ahora debemos trabajar con la variable `user_age`. Como ya mencionamos, esta tiene un tipo de datos incorrecto. Arreglemos este problema transformando el tipo de datos y mostrando el resultado final.

# In[12]:


user_age = 32.0
user_age = int(user_age)# cambia el tipo de datos para la edad de un usuario o usuaria a tipo integer

print(user_age)# se imprime el valor convertido a tipo integer.
#----------------------------------------------------------------------------------------------
#↓ Se puede verificar el tipo de dato de la variable user_age con la función type() ↓
print(type(user_age))# se imprime el tipo de dato


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien!.</div>

# # Ejercicio 4
# 
# Como sabemos, los datos no siempre son perfectos. Debemos considerar escenarios en los que el valor de `user_age` no se pueda convertir en un número entero. Para evitar que nuestro sistema se bloquee, debemos tomar medidas con anticipación.
# 
# Escribe un código que intente convertir la variable `user_age` en un número entero y asigna el valor transformado a `user_age_int`. Si el intento falla, mostramos un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: `Please provide your age as a numerical value.` (Proporcione su edad como un valor numérico.)

# In[21]:


user_age = 'treinta y dos' # aquí está la variable que almacena la edad como un string.

#↓ Se escribe un código que intente transformar 'user_age' en un entero y si falla, imprime el mensaje especificado ↓
user_age_int = 0 #se inicializa la variable `user_age_int` para almacenar el dato convertido a integer

try: #segmento de código de prueba
    user_age_int = int(user_age) #se almacena el valor convertido a integer en la variable `user_age_int`
    print(user_age_int) # se muestra la edad formateada a integer
    
except: #En caso de no ser posible realizar al conversión:
    print("Proporcione su edad como un valor numérico.") #Se muestra un mensaje notificando la falla


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Perfecto. Buenos comentarios en la celda.
# </div>

# # Ejercicio 5
# 
# Finalmente, considera que todas las categorías favoritas se almacenan en mayúsculas. Para llenar una nueva lista llamada `fav_categories_low` con las mismas categorías, pero en minúsculas, itera los valores en la lista `fav_categories`, modifícalos y agrega los nuevos valores a la lista `fav_categories_low`. Como siempre, muestra el resultado final.

# In[3]:


fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS'] #variable que contiene la lista de categorías en mayúsculas
fav_categories_low = [] #se inicializa variable que contendrá la lista de categorías en minúsculas

#↓ Se inicia la iteración de elementos string dentro de la lista de categorías en mayúsculas 'fav_categories' ↓
for category in fav_categories:
    fav_categories_low.append(category.lower()) #cada categoría se convierte en minúsculas 
                                                #y se añade a la lista fav_categories_low
        
print(fav_categories_low) #Se imprime la lista fav_categories_low que contiene las categorías en minúsculas


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien Adrian.</div>

# # Ejercicio 6
# 
# Hemos obtenido información adicional sobre los hábitos de gasto de nuestros usuarios y usuarias, incluido el importe gastado en cada una de sus categorías favoritas. La gerencia está interesada en las siguientes métricas:
# 
# - Importe total gastado por el usuario o la usuaria.
# - Importe mínimo gastado.
# - Importe máximo gastado.
# 
# Vamos a calcular estos valores y mostrarlos en la pantalla:

# In[12]:


fav_categories_low = ['electronics', 'sport', 'books'] #variable de lista que contiene categorías en minúsculas
spendings_per_category = [894, 213, 173] #variable de lista que contiene importes gastados en cada categoría

total_amount = sum(spendings_per_category) #se calcula la suma de todos los gastos 
max_amount = max(spendings_per_category)   # se calcula el máximo gasto realizado
min_amount = min(spendings_per_category)   #se calcula el mínimo gasto realizado
                
#↓ Se imprimen las métricas requeridas ↓
print('Total gastado:',total_amount)  #importe total gastado por usuario o usuaria
print('Máximo gastado:', max_amount)  #importe máximo gastado
print('Mínimo gastado:', min_amount)  #importe mínimo gastado


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien agregando el texto.</div>

# # Ejercicio 7
# 
# La empresa quiere ofrecer descuentos a sus clientes leales. Los clientes y las clientas que realizan compras por un importe total mayor a $1500 se consideran leales y recibirán un descuento.
# 
# Nuestro objetivo es crear un bucle `while` que compruebe el importe total gastado y se detenga al alcanzarlo. Para simular nuevas compras, la variable `new_purchase` genera un número entre 30 y 80 en cada iteración del bucle. Esto representa el importe de dinero gastado en una nueva compra y es lo que hay que sumar al total.
# 
# Una vez que se alcance el importe objetivo y se termine el bucle `while`, se mostrará la cantidad final.

# In[32]:


from random import randint #Importamos la función randint de la librería random para generar números enteros
#Para mejorar el código se sugiere añadir un contador de compras, definido como 'purchase_count'

total_amount_spent = 1280 #Monto total de gasto inicial
target_amount = 1500 #Monto objetivo para ofrecer descuento
purchase_count = 0 #Variable para contar las compras realizadas

#↓ bucle condicional para comprobar el importe total gastado ↓
while total_amount_spent <= target_amount: # El monto acumulado de compras debe sea menor al monto objetivo
    new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80 para simular nuevas compras
    total_amount_spent += new_purchase # acumulamos el monto total de compras sobre el monto inicial
    purchase_count += 1 #contador para determinar el número de compras después del monto inicial
#----------------------------------------------------------------------------------------------
#↓ Se imprimen las métricas de compra ↓
print('Monto total gastado:',total_amount_spent) # monto total gastado
print('No. Compras realizadas:', purchase_count) # número de compras realizado


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente vuelta le diste Adrian agregando el numero de compras realizadas.</div>

# # Ejercicio 8
# 
# Ahora tenemos toda la información sobre un cliente o una clienta de la forma que queremos que sea. La gerencia de una empresa nos pidió proponer una forma de resumir toda la información sobre un usuario o una usuaria. Tu objetivo es crear una cadena formateada que utilice información de las variables `user_id`, `user_name` y `user_age`.
# 
# Esta es la cadena final que queremos crear: `User 32415 is mike who is 32 years old.` (El usuario 32415 es Mike, quien tiene 32 años).

# In[59]:


user_id = '32415'             # Id del usuario
user_name = ['mike', 'reed']  # Nombre de usuario (nombre y apellido)
user_age = 32                 # Edad del usuario

caps_user_name  = [] #lista para capitalizar el nombre y apellido (caps: Capitals)
user_full_name = ""  #variable para asignar el nombre y apellido en formato string

for name_key in user_name: #bucle para iterar en la lista que contiene nombre y apellido del usuario
    caps_user_name.append(name_key.capitalize()) # Pone en mayúsculas la primera letra del nombre y apellido
                                                 #y los añade a la lista "capitalized_user_name"
        
user_full_name = " ".join(caps_user_name) #Se unen los elementos de la lista "caps_user_name" en una cadena    

#↓Se arma la cadena formateada con los datos del usuario ↓
user_info = f"El usuario {user_id} es {user_full_name}, quien tiene {user_age} años" 

print(user_info) #Se imprime la cadena con información del usuario


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy bien.</div>

# Como sabes, las empresas recopilan y almacenan datos de una forma particular. Store 1 desea almacenar toda la información sobre sus clientes y clientas en una tabla.
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# En términos técnicos, una tabla es simplemente una lista anidada que contiene una sublista para cada usuario o usuaria.
# 
# Store 1 ha creado una tabla de este tipo para sus usuarios y usuarias. Se almacena en la variable `users`. Cada sublista contiene el ID del usuario o la usuaria, nombre y apellido, edad, categorías favoritas y el importe gastado en cada categoría.

# # Ejercicio 9
# 
# Para calcular los ingresos de la empresa, sigue estos pasos.
# 
# 1. Utiliza `for` para iterar sobre la lista `users`.
# 2. Extrae la lista de gastos de cada usuario o usuaria y suma los valores.
# 3. Actualiza el valor de los ingresos con el total de cada usuario o usuaria.
# 
# Así obtendrás los ingresos totales de la empresa que mostrarás en la pantalla al final.

# In[1]:


users = [
    # este es el inicio de la primera sublista
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
        [894, 213, 173]
    ], # este es el final de la primera sublista

    # este es el inicio de la segunda sublista
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'],
        [439, 390]
    ] # este es el final de la segunda sublista
]

revenue = 0 #Se inicializa la variable para asignar los ingresos de la empresa

for user in users:
    spendings_list = [] #Se inicializa la lista de gastos de usuario
    
    spendings_list.append(sum(user[-1]))  # extrae la lista de gastos de cada usuario o usuaria y suma los valores
    total_spendings = sum(spendings_list) # suma los gastos de todas las categorías para obtener el total de un usuario o una usuaria en particular
    revenue += total_spendings # actualiza los ingresos
    
# se imprimen los ingresos totales de la empresa
print("Ingresos:", revenue)


# # Ejercicio 10
# 
# Recorre la lista de usuarios y usuarias que te hemos proporcionado y muestra los nombres de la clientela menor de 30 años.

# In[12]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

user_name_list = [] # Se inicializa lista que contendrá los clientes menores de 30 años
age = 30 # edad umbral de usuarios

for user in users: #Recorrer cada usuario de la lista 
    if user[2] < age: # verificar que los usuarios sean menores al umbral de "age"
        user_name = user[1] #Obtener la sublista que contiene el nombre/apellido del usuario
        user_name_list.append(user_name) #Agregar la sublista de nombre/apellido a la lista de clientes filtrados

print(user_name_list)

#Para mostrar los clientes de forma vertical se puede usar la siguiente sentencia:
#for user in user_name_list:
#    print(user)


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Nuestro objetivo es mostrar los nombres de los clientes de menos de 30 años. Por lo que una opcion mas eficiente seria solo mostrarlo y no agregar una nueva lista para mostrar.
# Imprimir directamente los resultados es preferible ya que es más eficiente en uso de memoria, el código es más simple, se utilizan menos recursos y mejora la legibilidad, evitando la creación de una lista separada.
# Para esto deberias manterner el if y luego realizar el print de lo que quieras mostrar (Indicando la posicion del nombre)
# 
# 
# 
# 
# </div>

# # Ejercicio 11
# 
# Juntemos las tareas 9 y 10 e imprimamos los nombres de los usuarios y las usuarias que tengan menos de 30 años y un gasto total superior a 1000 dólares.

# In[14]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

user_name_list = [] # Se inicializa lista que contendrá los clientes menores de 30 años
age = 30 # edad umbral de usuarios
spending_mount = 1000 #monto umbral de gasto

for user in users: #Recorrer cada usuario de la lista
    if user[2] < age and sum(user[-1]) > spending_mount : # verificar que la edad sea menor a "age" 
                                                          # y gastos superen el umbral "spending_mount"
        user_name = user[1] #Obtener la sublista que contiene el nombre/apellido del usuario
        user_name_list.append(user_name) #Agregar la sublista de nombre/apellido a la lista de clientes filtrados

print(user_name_list)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien!. Tene en cuenta lo que te marque en el anterior punto.
# 
# 
# 
# 
# </div>

# # Ejercicio 12
# 
# Ahora vamos a mostrar el nombre y la edad de todos los usuarios y todas las usuarias que han comprado ropa. Imprime el nombre y la edad en la misma declaración print.

# In[11]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

filtered_users = []  # inicializar lista de consulta de usuarios filtrados
category = 'clothes' # categoría de filtro 

for user in users: #Recorrer cada usuario de la lista original
    if category in user[3]: # verificar que el usuario haya comprado en la categoría consultada
        
        obtained_user = []  # Lista temporal para obtener la sublista de nombres de usuarios y edad
        user_name = user[1] # Obtener la sublista que contiene el nombre/apellido del usuario
        user_age = user[2]  # obtener la edad del usuario
        
        obtained_user.append(user_name) #Agregar la sublista de nombre/apellido a la lista de clientes filtrados
        obtained_user.append(user_age)  #Agregar la edad a la lista de clientes filtrados
        filtered_users.append(obtained_user) #agregar el cliente filtrado a la lista de consulta


print(filtered_users) #imprimir la lista de usuarios con sus edades, que han comprado en la categoría consultada

#Se puede usar un bucle for para imprimir los usuarios filtrados de forma más legible
#for user in filtered_users:
#    print(user)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho. La proxima podrias mostrarlo de forma mas estetica (llamando por posicion a cada cosa de la lista o haciendo lo que te explicaba en el punto 9)
# 
# 
# 
# 
# </div>

# # Discusión
# *En términos generales es importante y necesario que el analista de datos sepa exactamente los requerimientos de la empresa, debe haber una buena comunicación para garantizar la calidad del análisis de datos y optimizar el tiempo de trabajo. La comunicación debe ser constante, por lo que el analista debe desarrollar habilidades blandas asertivas para una correcta comunicacion y advertir posibles cambios en los requerimientos de la empresa, además de ser proactivo para mejorar la calidad del análisis.*
# 
# Entre las *tareas realizadas* en este proyecto, están:
# 
# - **Limpieza básica de datos** (conversión de tipo de datos, eliminación de espacios y caracteres innecesarios, conversión a minúsculas) para reducir el espacio visual y facilitar la legibilidad.
# - **Procesamiento y gestión de datos** definido por la segmentación de cadenas, manipulación y recorrido de listas, filtros, uso de excepciones.
# - **Presentación de información** mediante impresión de datos, formateo de cadenas
# 
# 
# ***Realizado por:*** *Adrián Vinueza Palacios*

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente observaciones Adrian.
# 
# 
# 
# 
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario general</b> <a class="tocSkip"></a>
# 
# 
# Adrian. Realizaste un trabajo completo de principio a fin. Me encanto leer tus argumentaciones y conclusiones generales.
# 
# Te deje simplemente un comentario en el ejercicio 9 a mejorar a futuro (Recorda que si hubieses tenido varios amarillos podria haber no aprobado, como esta solo es un consejo de mejora no pasa nada).
#     
# Los comentarios realizados al codigo fueron muy descriptivos y aportaron mucho, muy bien.
#     
# 
#     
# Te felicito por tu gran trabajo, me gusto mucho.
#     
#     
# Exitos en lo que viene. Saludos
#     
# 
# 
# 
# 
# </div>
