import pandas as pd
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='<yourpassword>', database='<databasename>')
if conn.is_connected():
    print('successfully connected')

# menu
def menu():
    print()
    print("******AIRLINE RESERVATION SYSTEM*******")
    print("1.Create table passenger")
    print("2.Add new passenger detail")
    print("3. Show all Passenger Details")
    print("4.Create table Classtype")
    print("5.Add new Classtype detail")
    print("6.Create table food")
    print("7.Add food item detail")
    print("8.Show food menu")
    print("9.Create table luggage")
    print("10.Add new charges for more weights")
    print("11.Show type of seats passenger has chosen and it's ticket price")
    print("12.If extra luggage then show it's bill")
    print("13.If any food item ordered, then show it's bill")
    print("14. Exit")
    print("*********************")

#creates passenger table
def create_passenger():
    c1 = conn.cursor()
    c1.execute('create table if not exists passenger (name varchar(25),address varchar(25),source varchar(25), destination varchar(25))')
    print('table passenger created!')

#Add passengers detail
def add_passenger():
    c1 = conn.cursor()
    L = []
    name = input("Enter Name:")
    L.append(name)
    address = input("Enter Address:")
    L.append(address)
    source = input("Enter Source:")
    L.append(source)
    destination = input("Enter Destination:")
    L.append(destination)
    ps = (L)
    sql = "insert into passenger(name, address, source, destination)values(%s,%s,%s,%s)"
    c1.execute(sql, ps)
    conn.commit()

#show all passenger details
def passenger_detail():
    print("Passengers :")
    df = pd.read_sql("select * from passenger", conn)
    print(df)

#create classtype table
def create_classtype():
    c1 = conn.cursor()
    c1.execute('create table if not exists classtype (sno int(5), classtype varchar(25),rate int(11))')
    print('table classtype created')

#Add classtype detail
def add_classtype():
    c1 = conn.cursor()
    df = pd.read_sql("select * from classtype", conn)
    print(df)
    L = []
    sno = input("Enter the serial number:")
    L.append(sno)
    item_name = input("Enter name of class type:")
    L.append(item_name)
    rate = input("Enter rate per ticket:")
    L.append(rate)
    ct = (L)
    sql = "insert into classtype(sno, classtype, rate)values(%s,%s,%s)"
    c1.execute(sql, ct)
    conn.commit()
    print('record inserted in classtype')

#Create food table
def create_food():
    c1 = conn.cursor()
    c1.execute("create table if not exists food (sno int(5), item_name varchar(25), rate int(11))")
    print("Table food created")

#Add food details
def add_food():
    c1 = conn.cursor()
    df = pd.read_sql("select * from food", conn)
    print(df)
    L = []
    sno = input('Enter the serial number:')
    L.append(sno)
    item_name = input("Enter name of food item:")
    L.append(item_name)
    rate = input("Enter rate of food item per piece:")
    L.append(rate)
    f = (L)
    sql = "insert into food(sno, item_name, rate)values(%s,%s,%s)"
    c1.execute(sql, f)
    conn.commit()
    print('record inserted in food')

#show food menu
def showfoodmenu():
    print("All food items available:")
    df = pd.read_sql("select * from food", conn)
    print(df)

#create luggage tabble
def create_luggage():
    c1 = conn.cursor()
    c1.execute("create table if not exists luggage (sno int(5), weight varchar(25), rate int(11))")
    print("Table luggage created")

#add extra luggage rate and their detail
def add_luggage():
    c1 = conn.cursor()
    df = pd.read_sql("select * from luggage", conn)
    print(df)
    L = []
    sno = input('Enter the serial number:')
    L.append(sno)
    weight = input("Enter weight of luggage:")
    L.append(weight)
    rate = input("Enter the rate of Luggage:")
    L.append(rate)
    lug = (L)
    sql = "insert into luggage (sno, weight, rate)values(%s,%s,%s)"
    c1.execute(sql, lug)
    conn.commit()
    print('record inserted in luggage')

#ticket reservation
def ticketreservation():
    print("We have the following seat types for you")
    df = pd.read_sql('select * from classtype', conn)
    print(df)
    choice = input("Enter your choice of ticket:")
    n = int(input("How many tickets do you need?"))
    c1 = conn.cursor()
    sl = "select rate from classtype where sno="
    c1.execute(sl + choice)
    result = c1.fetchone()
    print("Your total ticket price = Rs",result[0]*n)

#show extra luggage bill
def luggage_bill():
    df = pd.read_sql('select * from luggage', conn)
    print(df)
    sno = input("Enter serial number of weight of extra luggage:")
    c1 = conn.cursor()
    sl = "select rate from luggage where sno="
    c1.execute(sl+sno)
    result = c1.fetchone()
    print("Your cost of extra luggage = Rs ",result[0])

#show food bill
def food_bill():
    print('All food items available')
    df = pd.read_sql('select * from food', conn)
    print(df)
    order = input("Order your item number:")
    quantity = int(input("Enter the quantity:"))
    c1 = conn.cursor()
    sl = "select rate from food where sno="
    sql=sl+order
    c1.execute(sql)
    result = c1.fetchone()
    rate = result[0] * quantity

    print("Total food bill = Rs", rate)

#Main Program
chi = "y"
while chi == "y":
    menu()
    opt = int(input("Enter your choice:"))
    if (opt == 1):
        create_passenger()
    elif (opt == 2):
        add_passenger()
    elif (opt == 3):
        passenger_detail()
    elif (opt == 4):
        create_classtype()
    elif (opt == 5):
        add_classtype()
    elif (opt == 6):
        create_food()
    elif (opt == 7):
        add_food()
    elif (opt == 8):
        showfoodmenu()
    elif (opt == 9):
        create_luggage()
    elif (opt == 10):
        add_luggage()
    elif (opt == 11):
        ticketreservation()
    elif (opt == 12):
        luggage_bill()
    elif (opt == 13):
        food_bill()
    elif (opt == 14) :
        exit()
    else:
        print("Wrong Choice")
    chi = input("Do you want to continue? y/n: \n")
