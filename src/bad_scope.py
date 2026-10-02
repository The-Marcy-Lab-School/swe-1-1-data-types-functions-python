mood = "happy"


def describe_mood():
    global mood

    print("Hello " + their_name + ", are you feeling " + mood + " today?")

    their_name = "Zo"
    mood = "sad"

    print("Oh no, I'm sorry you're feeling " + mood + " today.")
