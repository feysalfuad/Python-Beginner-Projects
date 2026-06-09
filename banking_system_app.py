import json

print("🏦 Banking App")

try:
    with open("bank_data.json", "r") as file:
        data = json.load(file)
        
        balance = data["balance"]
        transactions = data["transactions"]
        
except FileNotFoundError:
    balance = 0
    transactions = []

def save_data():
    with open("bank_data.json","w") as file:
        json.dump(
            {
                "balance": balance,
                "transactions": transactions
            },
            file,
            indent=4
        )
              

while True:
    
    print("\nWhat would you like to do?")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Exit")
    
    choice = input("1-5: ").strip()
    
    if choice == "1":
        print (f"\n💰 Current Balance: £{balance:.2f}")
        
        amount = input("Enter deposit amount(or B to go back): ").strip().lower()
        
        if amount == "b":
            continue
        
        amount = float(amount)
        
        balance += amount
        
        print(f"✅ £{amount:.2f} deposited.")
        print(f"💰 New Balance: £{balance:.2f}")
        
        transactions.append(f"Deposit: £{amount:.2f}")
        
        save_data()
        
    elif choice == "2":
        
        print(f"\n💰 Current Balance: £{balance:.2f}")
        
        amount = input("Enter withdrawal amount (or B to go back): ").strip().lower()
        
        if amount == "b":
            continue
        
        amount = float(amount)
        
        if amount <= balance:
            
            balance -= amount
            
            print(f"✅ £{amount:.2f} withdrawn.")
            print(f"💰 New Balance: £{balance:.2f}")
            
            transactions.append(f"Withdraw: £{amount:.2f}")
            save_data()
        
        else:
            print("❌ Insufficient funds.")
        
        
    elif choice == "3":
        print(f"\n💰 Current Balance: £{balance:.2f}")
        
    elif choice == "4":
        print("\n📋 Transaction History:")
        
        if len(transactions) == 0:
            print("No transactions yet.")
            
        else:
            for i in range(len(transactions)):
                print(f"{i + 1}. {transactions[i]}")
                
        print(f"\n💰 Current Balance: £{balance:.2f}")
        
    elif choice == "5":
        print("👋 Goodbye!")
        break
    
    else:
        print("❌ Invalid choice.")
        
    
