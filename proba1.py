import pymongo

from  pymongo import MongoClient

client = MongoClient("mongodb+srv://vismyt:sex123456@cluster0.n9fsoha.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client["NewDB"]#создаем новую базу данніх м именем NewDB

user = db["user"]#Зтворюємо колекцію в базі данних(таблиця->user)

#данные колекции(таблицы)++++++++++++++++++++++
# data={"name":"YYYYYYYYY",
#       "age": 30,
#       "citi": "оывраловырлаорылвоа",
#       "company": object
       
#       }

# user.insert_one(data)#запись ------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<,
#данные колекции(таблицы)----------------------- 

# зробити багато записів в колекцію++++++++++++++++++++++++++++++++++++++++
#ВНИМАНИЕ ЗАПИСЬ В КЛЮЧ 'age' может быть и литерной!!!!!!!!!!
# manyUsers = [
#     {
#         "name": "Ostin",
#         "age": 36,
#         "city": "Tokio"
#     },
#     {
#         "name": "Maria",
#         "age": 19,
#         "city": "Sidney"
#     }
# ]

# user.insert_many(manyUsers) # insert_many - зробити багато записів в колекцію---------------------------------

result=user.find_one({"name":"jshgdfjsjdf"}) #Поиск одного участника (если нет - None)
# kjahdkjshdkajhdkahsdk
#100000
# дістати записи з колекції()+++++++++++++++++++
# result = user.find()
# for i in result:
#     print(i)
# дістати записи з колекції()--------------------
    
# result=user.find({"age":25})#поиск по выборке
# result=user.find({"age":30, "citi":"оывраловырлаорылвоа"})#поиск по выборке
# дістати записи з колекції()+++++++++++++++++++
# result = user.find()
# for i in result:
#     print(i)
# дістати записи з колекції()--------------------


#user.remove() удаление всей колекции(таблицы)-очистка
# db.drop_collection("имя колекции") #- удаляет колекцию(таблицу)

# user.update_one( { "name":"GOPA" } , { "$inc" : {"age": "310" } } )

# user.update_one({"age":25},{"$set":{"age":31}}) #замена
# user.update_one({"name":"GOPA"},{"$set":{"famili":"noga"}}) #замена (если нет 'famili' - добавит)
# user.update_one({"name":"GOPA"},{"$set":{"famili":"GOPA", "age": "310"}}) #замена

print(100)
