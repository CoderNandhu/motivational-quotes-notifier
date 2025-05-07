from plyer import notification
import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initial quote list
quotes = [
    "Believe you can and you're halfway there. Theodore Roosevelt",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn't just find you. You have to go out and get it.",
    "Dream it. Wish it. Do it.",
    "Great things never come from comfort zones.",
    "Don't watch the clock; do what it does. Keep going. Sam Levenson",
    "It's going to be hard, but hard does not mean impossible.",
    "Sometimes later becomes never. Do it now.",
    "You don't need to be perfect, just consistent.",
    "The future depends on what you do today. Mahatma Gandhi"
]

# Load additional quotes
if os.path.exists("my_quotes.txt"):
    with open("my_quotes.txt", "r") as file:
        file_quotes = [line.strip() for line in file if line.strip()]
        quotes.extend(file_quotes)

def show_quote():
    quote = random.choice(quotes)  # ✅ SINGLE STRING, not a list
    clear_screen()
    print("\n🧠 MOTIVATION BOOST 🔥\n")
    print(f"{quote}\n")
    print("Next quote coming soon... Stay sharp!\n")

    # DEBUG: Confirm the type is str
    #print(f"DEBUG: Type of quote = {type(quote)}")  # Should be <class 'str'>

    notification.notify(
        title="🧠 Motivation Boost",
        message=quote,
        timeout=10
    )

interval = 10

while True:
    show_quote()
    time.sleep(interval)

    # users_input = input("Do you want to enter your own Quote? Y for Yes or N for No: \n")
    # if users_input.lower() == "y":
    #     users_quote = input("Enter Your Quote.....! \n").strip()
    #     if users_quote:
    #         with open("my_quotes.txt", "a") as file:
    #             file.write(users_quote + "\n")
    #         quotes.append(users_quote)
    #         print("Your quote has been saved!")
