
Hire Store Application
The Hire Store application is a client-server program that allows users to register customers, register equipment, hire out equipment, and return equipment. It uses a socket-based communication mechanism to establish a connection between the client and the server.

Server Code
The server code is responsible for handling client requests and managing the database operations. It performs the following tasks:

Imports the necessary modules: mysql.connector for connecting to the MySQL database and socket for socket communication.
Creates a socket and binds it to the server's hostname and port 1234.
Listens for incoming connections from clients.
Connects to the MySQL database using the provided credentials.
Executes SQL statements to create three tables (users, equipment, rented) if they don't already exist.
Enters a loop to handle client requests indefinitely.
Authenticates the client by receiving the login name and password from the client, querying the users table for a matching record, and sending the authentication result back to the client.
If the authentication is successful, the server presents a menu to the client and performs the selected operation.
The server continuously listens for choices from the client and performs the requested actions accordingly. These actions include registering customers, registering equipment, hiring out equipment, returning equipment, and exiting the program.
Client Code
The client code is responsible for interacting with the server by sending requests and receiving responses. It performs the following tasks:

Imports the necessary modules: mysql.connector for connecting to the MySQL database and socket for socket communication.
Creates a socket and connects it to the server's hostname and port 1234.
Prompts the user to enter their login name and password.
Sends the login name and password to the server for authentication.
Waits for the authentication result from the server. If authentication is granted, the client proceeds to the next step; otherwise, it prompts the user to enter the login name and password again.
If authentication is granted, the client displays a menu to the user.
The user selects an option from the menu, and the client sends the corresponding choice to the server.
Based on the user's choice, the client performs operations such as registering customers, registering equipment, hiring out equipment, returning equipment, or exiting the program.
The client continues to interact with the server until the user chooses to exit the program.
How to Use the Application
Set up the MySQL database:

Make sure you have MySQL installed on your machine.
Create a database named "mydatabase".
Modify the server code's database connection details if necessary (e.g., host, user, password, port).
Run the server code:

Execute the server code using a Python interpreter (e.g., python server.py).
The server will start listening for incoming client connections.
Run the client code:

Execute the client code using a Python interpreter (e.g., python client.py).
Enter your login name and password when prompted.
If authentication is successful, you will see the menu of available options.
Select an option by entering the corresponding number or character.
Interact with the application:

Follow the prompts and enter the required information based on the chosen operation.
The server will process your request and provide appropriate responses.
Continue interacting with the application until you choose to exit.
Note: The code provided here assumes that the client and server are running on the same machine. If they are running on different machines, make sure to update the server code's binding address and the client code's connection address accordingly.

Remember to properly handle exceptions, input validations, and ensure the security of the application when using it in a production environment.
