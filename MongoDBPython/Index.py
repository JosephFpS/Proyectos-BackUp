from pymongo import MongoClient

#Coneccion a Mongo
uri = "mongodb+srv://jossolan:mongodb@cluster0.qiwgmtd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["DB2"]
collection = db["Estudiantes"]

try:
    client.admin.command('ping')
    print("Conectado")
except Exception as e:
   print(e)




# Lista de todas las bases de datos disponibles

database_names = client.list_database_names()
print("Las bases de datos disponibles son: ")
for db_name in database_names :
    print(db_name)

# Lista de todas las colecciones 


print("Las Coleeciones disponibles son: ")
collection_names = db.list_collection_names()
for db_collection in collection_names:
    print(db_collection)

#Encontrar primer documento
primer_documento = db.ESTUDIANTE.find_one()

print("Primer Documento: ",primer_documento)

#Crear nuevo documento

registro = {"Id": 4, "Nombre": "Eladio", "Apellido": "Carrion", "Edad": 25, "Semestre": 9}
aux = db.ESTUDIANTE.insert_one(registro)

print("ID insertado: ", aux.inserted_id)

#Cambiar Nombre de la coleccion ESTUDIANTE Se comenta linea ya que no perminte cambios identicos de colecciones ya existentes

  #new_name = db.ESTUDIANTE.rename("Estudiantes")

#Insertar nuevos estudiantes
registro= {"Id": 5, "Nombre": "Juan", "Apellido": "Calderon", "Edad": 19, "Semestre": 1}
aux = db.Estudiantes.insert_one(registro)
print("ID insertado: ", aux.inserted_id)

registro = {"Id": 6, "Nombre": "Tego", "Apellido": "Fernandez", "Edad": 21, "Semestre": 3}
aux= db.Estudiantes.insert_one(registro)
print("ID insertado: ", aux.inserted_id)


#Obtner documentos de una coleccion


result = collection.find()
print("Los documentos de la coleccion estuciantes son: ")
for document in result:
    print(document)

#Funciones Para Filtar Documentos

query = {"Nombre": "Angelika"}
result = collection.find(query)
print("Informacion del estudiante llamado Angelika: ")
for document in result:
    print(document)


query = {"$or": [{"Nombre": "Estudiante"}, {"Edad": 23}]}
result = collection.find(query)
print("Informacion del los estudiantes llamados Angelika o con una edad de 23 : ")
for document in result:
    print(document)


query = {"$and": [{"Nombre": "Juan"}, {"Apellido": "Calderon"}]}
result = collection.find(query)
print("Informacion del estudiante llamado Juan Calderon : ")
for document in result:
    print(document)

#Funciones para actualizar documentos
query = {"Id": 3}
new_data = {"$set": {"Nombre": "Maria"}}
a = collection.update_one(query, new_data)

print("Documento Modificado: ", a.modified_count)

query = {"Nombre": "Angelika"}
new_data = {"$set": {"Edad": 25, "Semestre": 9}}
result = db.Estudiantes.update_many(query, new_data)

print("Documentos Modificados: ", result.modified_count)

query = {"Nombre": "Maria", "Id": 3}
new_data = {"$set": {"Edad": 12, "Semestre": 0}}
result = db.Estudiantes.update_one(query, new_data)

print("Documento Modificado: ", result.modified_count)

#Funciones para eliminar documentos 
query = {"Id": 6}
result = db.Estudiantes.delete_one(query)

print("Documento Eliminado: ", result.deleted_count)









