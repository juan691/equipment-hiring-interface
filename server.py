#Juan Schoeman JHVCK9ZD4
#Question 3
import mysql.connector
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="mydatabase"
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM users")
for x in mycursor:
    print(x)
clientsocket, address = s.accept()





mycursor.execute("CREATE TABLE IF NOT EXISTS users(name VARCHAR(50), password VARCHAR(30))")
mycursor.execute("CREATE TABLE IF NOT EXISTS equipment(eqtype VARCHAR(30), eqnumber SMALLINT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS rented(renter VARCHAR(50), eqtype VARCHAR(30), eqnumber SMALLINT) ")



while True:
    loginname = clientsocket.recv(30)
    loginname = loginname.decode("utf-8")
    loginpass = clientsocket.recv(30)
    loginpass = loginpass.decode("utf-8")

    mycursor.execute("SELECT * from users WHERE name=%s and password=%s", (loginname, loginpass))
    for x in mycursor:
        print(x)
        if x == (loginname, loginpass):
            print("Correct Login")
            clientsocket.send(bytes("Granted", "utf-8"))



        mycursor.execute("SELECT * FROM users")
        for x in mycursor:
            print(x)
        mycursor.execute("SELECT * FROM equipment")
        for x in mycursor:
            print(x)
        mycursor.execute("SELECT * FROM rented")
        for x in mycursor:
            print(x)


        while True:

            choice = clientsocket.recv(32)
            choice = choice.decode("utf-8")

            if choice == "1":
                name = clientsocket.recv(32)
                name = name.decode("utf-8")
                print(name)
                password = clientsocket.recv(32)
                password = password.decode("utf-8")
                print(password)
                mycursor.execute("INSERT INTO users (name, password) Values (%s,%s)", (name, password))
                db.commit()
                mycursor.execute("SELECT * FROM users")
                for x in mycursor:
                    print(x)

            elif choice =="2":
                eqtype = clientsocket.recv(32)
                eqtype = eqtype.decode("utf-8")
                print(eqtype)
                eqnumber = clientsocket.recv(32)
                eqnumber = eqnumber.decode("utf-8")
                print(eqnumber)
                mycursor.execute("INSERT INTO equipment (eqtype, eqnumber) Values (%s,%s)", (eqtype, eqnumber))
                db.commit()
                mycursor.execute("SELECT * FROM equipment")
                for x in mycursor:
                    print(x)


            elif choice =="3":

                mycursor.execute("SELECT * FROM equipment")

                for x in mycursor:
                    print(x)
                    clientsocket.send(bytes(str(x), "utf-8"))



                keuse = clientsocket.recv(3)
                keuse = keuse.decode("utf-8")
                print(keuse)
                mycursor.execute("DELETE FROM equipment WHERE eqnumber=%s",(keuse,))
                db.commit()
                print("Equipment rented")

            elif choice =="4":
                eqtype = clientsocket.recv(32)
                eqtype = eqtype.decode("utf-8")
                print(eqtype)
                eqnumber = clientsocket.recv(32)
                eqnumber = eqnumber.decode("utf-8")
                print(eqnumber)
                mycursor.execute("INSERT INTO equipment (eqtype, eqnumber) Values (%s,%s)", (eqtype, eqnumber))
                db.commit()
                mycursor.execute("SELECT * FROM equipment")
                for x in mycursor:
                    print(x)

            elif choice == "x":
                s.close()
                clientsocket.close()
                break





    print("Incorrect Login try again")
    clientsocket.send(bytes("Denied", "utf-8"))




