from datetime import datetime

def chatbot():
    print("=" * 40)
    print("🤖 Welcome to Smart ChatBot")
    print("=" * 40)

    name = input("Before we start, what's your name? ")

    print(f"\nHello {name}! 😊")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user = input(f"{name}: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great. Thanks for asking!")

        elif user == "what is your name":
            print("Bot: My name is Smart ChatBot.")

        elif user == "time":
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current time is {current_time}")

        elif user == "date":
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's date is {current_date}")

        elif user == "help":
            print("\nYou can ask:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- time")
            print("- date")
            print("- bye\n")

        elif user == "bye":
            print(f"Bot: Goodbye, {name}! Have a nice day. 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")

chatbot()