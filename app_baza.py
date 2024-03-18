# class Goods:
    
#     def __init__(self, name, country, category, price, discount=0):
#         self.name = name
#         self.country = country
#         self.category = category
#         self.price = price
#         self.discount = discount

#     def showPrice(self):
#         print(self.price - (self.price * self.discount) / 100)

#     def getPrice(self):
#         return (self.price - (self.price * self.discount) / 100)

#     def changeDiscount(self, newValue):
#         self.discount = newValue

# class Shop:
    
#     def __init__(self, name, address, *products):
#         self.name = name
#         self.address = address
#         self.productsList = []

#         for item in products:
#             self.productsList.append(item)

#     def add(self, *products):
#         count = 0
#         for item in products:
#             self.productsList.append(item)
#             count+=1
#         print(f"До магазину {self.name} додано {count} товарів")

#     def changeDisc(self, name):
#         for item in self.productsList:
#             if name == item.name:
#                 newDisc = int(input("Введіть нову знижку у відсотках: "))
#                 item.changeDiscount(newDisc)
#                 return

#     def delProduct(self, name):
#         for item in self.productsList:
#             if name == item.name:
#                 self.productsList.remove(item)
#                 return

#     def showProducts(self):
#         for item in self.productsList:
#             print(f"{item.name}, country - {item.country}, price - {item.getPrice()}")

# prod1 = Goods("Umbrella", "China", "first", 400)
# prod2 = Goods("Shoes", "Nepal", "second", 4000, 30)
# shop1 = Shop("Rozetka", "ADDRESS", prod1, prod2)
# shop1.showProducts()
# shop1.changeDisc("Shoes")
# prod3 = Goods("T-shirt", "USA", "third", 2400, 15)
# shop1.add(prod3)
# shop1.delProduct(prod1.name)
# shop1.showProducts()



# NoSQL база данних MongoDB

# from sqlite3 import connect
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://oleh:1234@cluster0.zgzo8gg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # підключаємось до кластеру

# db = client["NewDB"] # створюємо нову базу данних з назвою NewDB

# user = db["User"] #Створюємо колекцію в базі данних з назвою User (колекція = таблиця)


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

# user.insert_many(manyUsers) # insert_many - зробити багато записів в колекцію

# post = user.insert_one({"name": "Kate", "age": 28, "city": "Otava"})

# print(post) 

# data = {
#     "name": "Mike",
#     "age": 25,
#     "city": "California"
# }

# user.insert_one(data) # insert_one - зробити один запис в колекцію

# result = user.find_one({"age": {"$lt": 25}}) # find_one - дістати один записи з колекції
# print(result)

# result = user.find().sort("name") # find - дістати записи з колекції

# for item in result:
#     print(item["name"])

# user.insert_one({"name": "Dana", "hight": 150, "country": "Litva", "languages": ["Eng", "Spanish", "Italian"]})

# data = user.delete_one({"name": "Dana"}) # видалення одного запису з таблиці, delete_many - видалити декілька записів одразу
# print(data)

# user.update_one({"name": "Kate"}, {"$set": {"age": 37, "city": "Toronto"}}) # update_one - оновити дані для одного запису
# user.update_many({"age": {"$lt": 30}}, {"$set": {"city": "Washington"}}) # update_many - оновити дані для багатьох записів


# Регістрація Користувачів , Зареєстрований користувач має можливість замовити товар , Реалізувати Користувача - Адміністратора
# Створити класси: User, Product, Admin, Order
# Підключити базу данних , створити відповідні таблиці
# Реалізувати необхідні методи

from pymongo import MongoClient
import datetime

currentUser = None #

#connect = MongoClient("mongodb+srv://root:root@cluster0.zzgdurg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
connect = MongoClient("mongodb+srv://vismyt:sex123456@cluster0.n9fsoha.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# db = connect["firstTest"]
db=connect["NewDB"]

# userData = db["user"]
userData = db["user1"]#Все пользователи

productData = db["product"]

orderData = db["order"]

class User:
    
    def __init__(self, mail, password, bithDate, permission=False, data=datetime.date.today()):
        self.mail = mail
        self.__password = password
        self.bithDate = bithDate
        self.data = data
        self.permission = permission
        data = userData.find_one({"mail": mail})
        try:
            self.bucket = data["bucket"]
        except:
            self.bucket = []

#Запись нового пользователя в базу+++++++++++++++++++++++++++++++++
    def addUserToDB(self):
        userData.insert_one({
            "mail": self.mail,
            "password": self.__password,
            "bithDate": self.bithDate,
            "data": str(self.data),
            "permission": self.permission,
        })
#Запись нового пользователя в базу-----------------------------------

#Замена почты++++++++++++++++++++++++        
    def setMail(self, newMail):
        userData.update_one({"mail": self.mail}, {"$set": {"mail": newMail}})
        self.mail = newMail
        print("Почту успішно змінено")
#Замена почты-------------------------

#Замена пароля+++++++++++++++++++++++++++++++        
    def setPassword(self, newPass):
        userData.update_one({"mail": self.mail}, {"$set": {"password": newPass}})
        self.__password = newPass
        print("Пароль успішно змінено")
#Замена пароля---------------------------------
        
# Вывод инфо о пользователе++++++++++++++++++++++++++++++        
    def showInfo(self):
        print(f"Mail - {self.mail}, bithDate - {self.bithDate}, Date of registrate - {self.data}")
# Вывод инфо о пользователе------------------------------

# Показать список товаров++++++++++++++++++++++++++++++++++++++        
    def showAllProduct(self):
        print(" ")
        result = productData.find()
        for item in result:
            prod = Product(item['name'], item['price'], item['discount'])
            prod.showInfo()
        print()
# Показать список товаров----------------------------------------
    # Bucket method

    def addProductToBucket(self):
        name = input("Введіть назву товару: ")
        count = productData.count_documents({"name": name})
        if count == 0:
            print("Не вірно обраний товар, не вдалося знайти такого")
            startMenu()
            return
        try:
            data = productData.find_one({"name": name})
            productCount = int(input("Введіть скільки одиниць товару ви хочете замовити: "))
            if productCount < 1:
                raise Exception

            self.bucket.append({
                "name": name,
                "price": data['price'],
                "discount": data['discount'],
                "count": productCount
            })

            self.addBucketToDB()

        except Exception:
            print("Ви ввели некоректне значення")
            startMenu()
            return

    def addBucketToDB(self):
        userData.update_one({"mail": self.mail}, {"$set": {"bucket": self.bucket}})

    def getTotalPrice(self):
        total = 0
        for item in self.bucket:
            prod = Product(item['name'], item['price'], item['discount'])
            total+=prod.showPrice() * item['count']
        return total

    def showBucket(self):
        print(" ")
        for prod in self.bucket:
            obj = Product(prod['name'], prod['price'], prod['discount'])
            print(f"{obj.getInfo()} x {prod['count']}")
        print("Total Price: ", self.getTotalPrice(), " \n")

    def deleteProductFromBucket(self):
        self.showBucket()
        prodName = input("Введіть назву товару який хочете видалити: ")
        for item in self.bucket:
            if item["name"] == prodName:
                self.bucket.remove(item)
                print("Товар успішно видалено")
                self.addBucketToDB()
                return
        print("Некоректна назва товару")

    def clearBucket(self):
        self.bucket = []
        self.addBucketToDB()
        print("Корзина порожня")

class Product:
    
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def addProductToDB(self):
        productData.insert_one({
            "name": self.name,
            "price": self.price,
            "discount": self.discount
        })

    def showPrice(self):
        return (self.price * (1 - self.discount/100))
    
    def showInfo(self):
        print(f"{self.name} - {self.showPrice()} grn")

    def getInfo(self):
        return f"{self.name} - {self.showPrice()} grn"
        
class Admin(User):

    def __init__(self, mail, password, bithDate, data):
        super().__init__(mail, password, bithDate, True, data)

    # users methods:

    def showUsers(self):
        users = userData.find()
        for user in users:
            print(f"{user['mail']}  {user['data']}")

#даем права администратора+++++++++++++
    def givePermission(self, userMail):
        userData.update_one({"mail": userMail}, {"$set": {"permission": True}})
        print(f"Користувачу {userMail} надані права адміністратора")
#даем права администратора-------------
        
#удалить права админа+++++++++++++++++++++++++++++        
    def takeOffPermission(self, userMail):
        userData.update_one({"mail": userMail}, {"$set": {"permission": False}})
        print(f"Користувача {userMail} позбавлено прав адміністратора")
#удалить права админа------------------------------
        
    # products methods: 
# Добавить товар(ввод название и цены)+++++++++++++++++++++++++++++++++++++++++++
    def addProduct(self):
        name = input("Введіть назву товару: ")
        price = float(input("Введіть ціну товару: "))
        discount = int(input("Введіть знижку на товар: "))
        prod = Product(name, price, discount)
        prod.addProductToDB()
# Добавить товар(ввод название и цены)--------------------------------------------
        
    def deleteProduct(self):
        self.showAllProduct()
        print(" ")
        prodName = input("Введіть назву товару який видаляємо: ")
        productData.delete_one({"name": prodName})
        print("Товар успышно видалено \n")

class Order:
    
    def __init__(self, userID, address, data, *products):
            self.userID = userID
            self.address = address
            self.data = data
            self.products = list(products)
            self.totalPrice = 0
            for item in products:
                self.totalCount+=item.price

def logOut():
    global currentUser
    currentUser = None
    print("Ви вийшли з аккаунту")
    startMenu()

#регистрация(Ввод данных)++++++++++++++++++++++++++++++++++++++
def registr():
    global currentUser
    mail = input("Введіть вашу почту: ")
    password = input("Введіть ваш пароль: ")
    bithDate = input("Введіть дату народження в такому вигляді: Рік-Місяць-День: ")
    data = userData.find_one({"mail": mail})
    if data != None:
        print("Користувач з такою почтою вже зареєстрований , введіть іншу почту")
        registr()
    currentUser = User(mail, password, bithDate)
    currentUser.addUserToDB()
    print("Ви успішно зареєстровані")
    startMenu()
#регистрация(Ввод данных)--------------------------------------
    
def logIn():
    global currentUser
    mail = input("Введіть вашу почту: ")
    password = input("Введіть ваш пароль: ")
    data = userData.find_one({"mail": mail, "password": password})
    if data == None:
        print("Невірний пароль або почта, введіть корректні данні")
        logIn()
        return

    if data["permission"] == True:
        currentUser = Admin(data['mail'], data['password'], data['bithDate'], data['data'])

    else:
        currentUser = User(data['mail'], data['password'], data['bithDate'], data['permission'], data['data'])
    print("Ви успішно увійшли в свій аакаунт")
    startMenu()

#меню входа++++++++++++++++++++++++++++++++++++++++++++
def startMenu():
    global currentUser

    if currentUser == None:
        temp = input("Введіть 1 - щоб Зареєструватися, введіть 2 - щоб авторизуватися, введіть 0 щоб вийти: ")
        if temp == "1":
            registr()
        elif temp == "2":
            logIn()
        elif temp == "0":
            print("Good Bye")
        else:
            print("Вибрана операція не корректна спробуйте ще раз")
            startMenu()

    elif currentUser.permission == False:
        print(f"Вітаємо {currentUser.mail}")
        temp = input("Введіть 1 - змінити почту, 2 - змінити пароль, 3 - переглянути інформацію, 4 - переглянути товари, "
                     "\n 5 - додати товар до корзини, 6 - переглянути корзину, 7 - видалити товар з корзини \n"
                     "8 - очистити корзину, 0 щоб вийти з аккаунту: ")
        if temp == "0":
            logOut()
        elif temp == "1":
            mail = input("Введіть нову почту: ")
            currentUser.setMail(mail)
            startMenu()
        elif temp == "2":
            password = input("Введіть новий пароль: ")
            currentUser.setPassword(password)
            startMenu()
        elif temp == "3":
            currentUser.showInfo()
            startMenu()
        elif temp == "4":
            currentUser.showAllProduct()
            startMenu()
        elif temp == "5":
            currentUser.addProductToBucket()
            startMenu()
        elif temp == "6":
            currentUser.showBucket()
            startMenu()
        elif temp == "7":
            currentUser.deleteProductFromBucket()
            startMenu()
        elif temp == "8":
            currentUser.clearBucket()
            startMenu()
        else:
            print("Вибрана операція не корректна спробуйте ще раз")
            startMenu()

    elif currentUser.permission == True:
        print("Вітаємо Адміністратор")
        temp = input("Введіть 1 - Переглянути усіх користувачів, 2 - надати права, 3 - додати товар, 4 - переглянути товари "
                     "\n 5 - видали товар, 0 - вихід: ")
        if temp == "1":
            currentUser.showUsers()
            startMenu()
        elif temp == "0":
            logOut()
        elif temp == "2":
            mail = input("Введіть почту користувача: ")
            currentUser.givePermission(mail)
            startMenu()
        elif temp == "3":
            currentUser.addProduct()
            startMenu()
        elif temp == "4":
            currentUser.showAllProduct()
            startMenu()
        elif temp == "5":
            currentUser.deleteProduct()
            startMenu()
        else:
            print("Вибрана операція не корректна спробуйте ще раз")
            startMenu()
#меню входа---------------------------------------------
            
startMenu()
# print(100)