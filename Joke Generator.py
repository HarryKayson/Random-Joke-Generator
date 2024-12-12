#1. Random Joke Generator 🤣
#Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
import random

def random_joke():
    # List of the random jokes
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my computer I needed a break, and now it won't stop sending me Kit-Kats!",
        "Why did the math book look sad? It had too many problems."
    ]

    # Randomly select a joke from the above set
    joke = random.choice(jokes)

    # Displaying the joke
    print("Here is a joke for you to lighten up your day G!")
    print(joke)

# Run the program
if __name__ == "__main__":
    random_joke()

