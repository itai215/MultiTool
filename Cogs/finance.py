import sqlite3
import time

def main():
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute("SELECT user_name, balance FROM users")
    result = c.fetchall()
    accounts = {row[0]: row[1] for row in result}
    
    print("What account you want to open? \n \n ", "\n".join([f"{i+1}. {name}" for i, (name, _) in enumerate(sorted(accounts.items()))]))
    print("Enter 'new' to create new account")
    
    while True:
        user_input = input()
        if user_input.lower() == "new":
            print("Welcome to new account creator!")
            print("Please enter your name: ")
            user_name = input()
            print("Please enter your initial balance: ")
            balance = int(input())
            c.execute("INSERT INTO users (user_name, balance) VALUES (?, ?)", (user_name, balance))
            conn.commit()
            print("Account created successfully!")
            break
        elif user_input.isdigit() and 1 <= int(user_input) <= len(accounts):
            user_name = sorted(accounts.keys())[int(user_input) - 1]
            balance = accounts.get(user_name)
            break
        else:
            print("Invalid username. Please try again.")
    
    print(f"Hello {user_name}")
    print(f"Your balance is {balance}")
    print("What do you want to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    
    choose = input()
    
    if choose == "1":
        print("How much do you want to deposit?")
        amount = int(input())
        c.execute("UPDATE users SET balance = ? WHERE user_name = ?", (balance + amount, user_name))
        conn.commit()
        print("Deposit successful!")
    elif choose == "2":
        print("How much do you want to withdraw?")
        amount = int(input())
        if amount > balance:
            print("Not enough balance")
            time.sleep(3)
            return
        c.execute("UPDATE users SET balance = ? WHERE user_name = ?", (balance - amount, user_name))
        conn.commit()
        print("Withdraw successful!")
    elif choose == "0":
        return print("Goodbye!")
    else:
        print("Invalid choice. For security reasons you will be logged out to menu.")
        time.sleep(3)
        return


if __name__ == "__main__":
    main()