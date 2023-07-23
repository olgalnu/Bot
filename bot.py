import nltk
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pymysql
from nltk.stem.lancaster import LancasterStemmer

nltk.download('punkt')

stemmer = LancasterStemmer()

# Cargar el archivo de intenciones
with open("intents.json") as file:
    data = json.load(file)

# Preprocesar los datos
palabras = []
tags = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pat in intent["patterns"]:
        # Tokenizar cada palabra en el patrón
        wrds = nltk.word_tokenize(pat)
        # Agregar palabras al corpus
        palabras.extend(wrds)
        # Agregar el patrón y su tag correspondiente al corpus
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
    # Agregar tag al corpus de tags
    if intent["tag"] not in tags:
        tags.append(intent["tag"])

# Listar y ordenar
palabras = sorted(list(set(palabras)))
tags = sorted(tags)

# Crear datos de entrenamiento
training = []
output = []
# Array de salida con ceros en todas las posiciones excepto en la posición correspondiente al tag
out_empty = [0 for _ in range(len(tags))]

for x, doc in enumerate(docs_x):
    bag = []
    # Stemming de cada palabra en el patrón
    wrds = [stemmer.stem(w.lower()) for w in doc]
    # Crear un array de palabras
    for w in palabras:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    # Crear un array de salida con el tag correspondiente
    output_row = out_empty[:]
    output_row[tags.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

# Convertir en arrays de numpy
training = np.array(training)
output = np.array(output)

# Construir modelo
tf.compat.v1.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

# Entrenar el modelo
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("modelo.tflearn")

# Función para clasificar la entrada del usuario
def clasificar_palabras(entrada):
    # Tokenizar y stemming de las palabras en la entrada
    wrds = [stemmer.stem(w.lower()) for w in nltk.word_tokenize(entrada)]
    # Crear un array de entrada
    bag = [0 for _ in range(len(palabras))]
    for w in wrds:
        for i, word in enumerate(palabras):
            if word == w:
                bag[i] = 1

    # Predecir el tag correspondiente
    results = model.predict([np.array(bag)])
    results_index = np.argmax(results)
    tag = tags[results_index]

    return tag

# Establecer conexión con la base de datos
conn = pymysql.connect(host='localhost', port=3306, user='root', password='12345', database='luna_baby')
cursor = conn.cursor()

# Función para ejecutar una consulta en la base de datos
def ejecutar_consulta(consulta):
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

# Función para generar una respuesta aleatoria
def generar_respuesta(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            respuesta = random.choice(intent["responses"])
            break
    else:
        respuesta = "Lo siento, no entiendo lo que quieres decir"
    return respuesta

while True:
    # Obtener entrada del usuario
    entrada = input("Tú: ")
    # Clasificar la entrada
    tag = clasificar_palabras(entrada)

    if tag == "consulta":
        # Ejecutar la consulta en la base de datos
        consulta = "SELECT * FROM tabla"
        resultados = ejecutar_consulta(consulta)
        respuesta = str(resultados)
        print("Bot: " + respuesta)
    else:
        # Generar una respuesta
        respuesta = generar_respuesta(tag)
        print("Bot: " + respuesta)
