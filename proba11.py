
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://vismyt:8BeyLsaeeEjGgxIJ@cluster0.ugygzy3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient(uri)


# db=client["NewDB"]#создаем новую базу данніх м именем NewDB
# user = db["user"]#Зтворюємо колекцію в базі данних(таблиця->user)
# exit()

db=client['testdata']#открываем базу данных
col=db["testcol"]#открываем таблицу

a=col.find()
print(a)

# print(col.find_one({"Year": "2016"}))#поиск первого вхождения
# db.drop_collection("test_colection")#удаление колекции(базы?)
exit()
# записываем данные в таблицу+++++++++++++++++++
# movie_ = {
# "title": "Mr. Robot2sdfs",
# "Starring": "Rami Malek, Christian Slater, Carly Chaikin",
# "created": "Sam Esmail",
# "Year": "2016"
# }
# id = col.insert_one(movie_).inserted_id
# записываем данные в таблицу---------------------------

print(col.find_one({"Year": "2016"}))#поиск первого вхождения
# print(col.find_one({"Year": "2016"}))#поиск первого вхождения

# a="kjhkjh"
# while a!=None:
#     a=col.find_one({"Year": "2016"})#поиск первого вхождения
#     if a!=None:
#         print(a)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Get list of databases
# databases = client.list_database_names()
# if not databases:
#     print("No databases found")

# # Does database exist?
# DB_NAME = "testdata"
# if DB_NAME in databases:
#     print("est")
# else:
#     print("net")

# # Get list of databases
# # databases = client.list_database_names()

# # Loop through databases
# for db in databases:
#     print("Database: {}".format(db))

#     # Get list of collections
#     collections = client[db].list_collection_names()

#     # Loop through collections
#     for col in collections:
#         print("\tCollection: {}".format(col))

#         # Get document count
#         doc_count = client[db][col].count_documents({})
#         print("\tDocument count: {}".format(doc_count))    

#----------------------------------------------------------------------------