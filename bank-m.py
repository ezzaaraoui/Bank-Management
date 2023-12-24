import csv
import random

clients = {}
accounts = {}
client_accounts = {}
MPC = ""

def addClient(numCl, MPC, numC, SoldeC):
    clients[numCl] = MPC
    accounts[numC] = SoldeC
    client_accounts[numCl] = numC

def removeClient(numCl):
    if numCl in client_accounts:
        numC = client_accounts[numCl]  # Get the corresponding account number
        clients.pop(numCl)
        accounts.pop(numC)
        client_accounts.pop(numCl)
        print(f"Account removed successfully.")
    else:
        print("Account not found.")



def modifyPassword(clientNum, oldPass):
    global MPC
    if clientNum in clients and oldPass == clients[clientNum]:
        newPass = input("Enter new password: ")
        clients[clientNum] = newPass
        print("Password updated successfully.")
    elif clientNum not in clients:
        print("Client not found.")
    elif oldPass != clients[clientNum]:
        while True:
            print("Old password incorrect")
            oldPass = input("Enter old password: ")
            if oldPass == clients[clientNum]:
                newPass = input("Enter new password: ")
                print("Password updated successfully.")
                break

def checkBalance(clientNum):
    if clientNum in client_accounts:
        accountNum = client_accounts[clientNum]
        print(f"Balance for account : {accounts[accountNum]}")
    else:
        print("Client not found.")

def deposit(clientNum, amount):
    if clientNum in client_accounts:
        accountNum = client_accounts[clientNum]
        accounts[accountNum] += amount
        print(f"Amount {amount} deposited successfully. New balance: {accounts[accountNum]}")
    else:
        print("Client not found.")

def withdraw(clientNum, amount):
    if clientNum in client_accounts:
        accountNum = client_accounts[clientNum]
        if accounts[accountNum] >= amount:
            accounts[accountNum] -= amount
            print(f"Amount {amount} withdrawn successfully. New balance: {accounts[accountNum]}")
        else:
            print("Insufficient funds.")
    else:
        print("Client not found.")

generateAccountNumber = lambda clientNum: int(str(clientNum) + str(random.randint(0, 100)))

def writeToCSV():
    with open('client_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['Client Number', 'Password'])
        for clientNum, password in clients.items():
            writer.writerow([clientNum, password])

while True:
    print("\nBank Management System")
    print("1. Agent Menu")
    print("2. Client Menu")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print("\nAgent Menu")
        print("1. Add an Account")
        print("2. Remove an Account")

        agentChoice = input("Enter your choice (1/2): ")

        if agentChoice == '1':
            numCl = int(input("Enter client number: "))
            MPC = input("Enter client password: ")
            numC = generateAccountNumber(numCl)
            SoldeC = float(input("Enter initial balance: "))
            addClient(numCl, MPC, numC, SoldeC)

        elif agentChoice == '2':
            numC = int(input("Enter account number to remove: "))
            removeClient(numC)

    elif choice == '2':
        print("\nClient Menu")
        print("1. Modify Password")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")

        clientChoice = input("Enter your choice (1/2/3/4): ")
        clientNum = int(input("Enter your client number: "))

        if clientChoice == '1':
            oldPass = input("Enter old password: ")
            modifyPassword(clientNum, oldPass)

        elif clientChoice == '2':
            checkBalance(clientNum)

        elif clientChoice == '3':
            amount = float(input("Enter the amount to deposit: "))
            deposit(clientNum, amount)

        elif clientChoice == '4':
            amount = float(input("Enter the amount to withdraw: "))
            withdraw(clientNum, amount)

    elif choice == '3':
        print("Exiting the program.")
        writeToCSV()
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
