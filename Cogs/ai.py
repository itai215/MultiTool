import g4f
from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello"}],
    web_search=False
)
print(response.choices[0].message.content)

def main():
    print("Welcome to AI bot. Here you can ask me anything. If you want to exit, type '0'.")
    while True:
        question = input()
        
        if question == "0":
            break
        elif question == "":
            continue
        else:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": question}],
                web_search=False
            )
            print(response.choices[0].message.content)

if __name__ == "__main__":
    main()