class DatabaseConnection:
    def __init__(self, hostname, username, password, port):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def show_connection_string(self):
        print(f"Hostname: {self.hostname}\nPort: {self.port}\nUsername: {self.username}\nPassword: {self.password}")


connection_info = DatabaseConnection("stark-industries.database.com","Harry","SnapeIsTheBest!",5432)

connection_info.show_connection_string()