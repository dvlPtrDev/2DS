class BankAccount:
    def __init__(self, balance, user):
        self.balance = balance
        self.user = user
        self.agency = "0001"

    def check_info(self):
        print(f"Olá, {self.user}, a agência do seu banco é a {self.agency} e você tem R${self.balance} na conta\n")
    
    def receive(self, amount):
        self.balance += amount
        print(f"Saldo de {self.user} incrementado em {amount}\n")
        print(f"Seu novo saldo é de {self.balance}\n")

    def transfer(self, amount):
        if amount > self.balance:
            print("Saldo insuficiente!\n")
        else: 
            self.balance -= amount
            print(f"Novo saldo para user {self.user}: {self.balance}\n")

user1 = BankAccount(350, "Izar")
user2 = BankAccount(200, "Enzo")
user3 = BankAccount(150, "Valentina")

user1.check_info()
user2.receive(250)
user2.transfer(100)
user3.check_info()
user3.receive(5000)
user3.transfer(10000)
