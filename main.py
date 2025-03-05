import os
import subprocess
import sys

libraries = ["disnake", "keyboard", "g4f", "db-sqlite3"]

for library in libraries:
    subprocess.check_call([sys.executable, "-m", "pip", "install", library])

import sqlite3

def create_database():
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_name TEXT,
        balance INTEGER, 
        earnings INTEGER,
        expenses INTEGER
        )""")
    conn.commit()
    conn.close()
    print("✅")

def show_menu():
    print("——————————————————————————————————")
    print("Welcome to the Multi-Tool Console!")
    print("1. MorseCode Conventer")
    print("2. Timer Pomodoro")
    print("3. Finance")
    print("4. Chat with AI")
    print("0. Exit")
    print("——————————————————————————————————")

def run_tool(tool_number):
    tools = {
        1: "Cogs/translate.py",
        2: "Cogs/timer.py",
        3: "Cogs/finance.py",
        4: "Cogs/ai.py"
    }

    if tool_number in tools:
        tool_path = tools[tool_number]
        if os.path.exists(tool_path):
            os.system('cls' if os.name == 'nt' else 'clear')
            subprocess.run(["python", tool_path])
        else:
            print(f"Error: {tool_path} not found.")
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    print("Validating database.....")
    create_database()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Exiting....")
            break

        run_tool(choice)

if __name__ == "__main__":
    main()
