import mysql.connector
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


auth = "Denied"
while auth=="Denied":
    loginname = input("Enter login")
    loginpass = input("Enter Password")

    s.send(bytes(loginname, "utf-8"))
    s.send(bytes(loginpass, "utf-8"))
    auth = s.recv(32)
    auth = auth.decode("utf-8")
    if auth == "Granted":

        print("=" * 52 +
              "\n" + "|" + " " * 20 +"Hire Store" + " " * 20 + "|" +
              "\n" + "=" * 52 +
              "\n| 1. Register Customer" + " " * 29 + "|" +
              "\n| 2. Register Equipment" + " " * 28 + "|" +
              "\n" + "=" * 52 +
              "\n| 3. Hire Out Equipment" + " " * 28 + "|" +
              "\n| 4. Return Equipment" + " " * 30 + "|" +
              "\n" + "=" * 52 +
              "\n| x. Exit" + " " * 42 + "|" +
              "\n" + "=" * 52)
        choice = input("Choice:")

        if choice == "1":
            s.send(bytes("1", "utf-8"))
            name = input("Name:")
            password = input("Password:")
            s.send(bytes(name, "utf-8"))
            s.send(bytes(password, "utf-8"))

        elif choice == "2":
            s.send(bytes("2", "utf-8"))
            eqtype = input("Equipment Type:")
            eqnumber = input("Equipment Number")
            s.send(bytes(eqtype, "utf-8"))
            s.send(bytes(eqnumber, "utf-8"))

        elif choice =="3":
            s.send(bytes("3", "utf-8"))


            x=0
            while x<3:

                equipment = s.recv(60)
                equipment = equipment.decode("utf-8")
                print(equipment)
                x = x+1

            keuse = input("Choose equipment number")
            s.send(bytes(str(keuse), "utf-8"))
            print("Equipment rented")

        elif choice == "4":
            s.send(bytes("4", "utf-8"))
            eqtype = input("Equipment Type:")
            eqnumber = input("Equipment Number")
            s.send(bytes(eqtype, "utf-8"))
            s.send(bytes(eqnumber, "utf-8"))

        elif choice =="x":
            s.send(bytes("4", "utf-8"))




