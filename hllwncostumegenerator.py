# Step One: Introduction
print("Hi there! I'm here to help you decide on your Halloween costume.")
print("Do you want to be something scary or funny?")

# Step Two: Scary or Funny
choice = input("Type 'Scary' or 'Funny': ").lower()

# Scary Portion
if choice == "scary":
    print("Great choice! Now, let's choose a color.")
    print("What color do you want: Black, White, or Orange?")
    color = input("Type your choice: ").lower()

    if color == "black":
        print("You'll be a witch!")
    elif color == "white":
        print("You'll be a ghost!")
    elif color == "orange":
        print("You'll be a pumpkin!")
    else:
        print("Invalid color choice. Please choose Black, White, or Orange.")

# Funny Portion
elif choice == "funny":
    print("Smart choice! Now, let's choose a color.")
    print("What color do you want: Orange, Blue, Yellow, or Green?")
    color = input("Type your choice: ").lower()

    if color == "blue":
        print("You'll be a Dragon!")
    elif color == "yellow":
        print("You'll be an Alien!")
    elif color == "green":
        print("You'll be the Frog Prince!")
    elif color == "orange":
        print("You'll be a Clown!")
    else:
        print("Invalid color choice. Please choose Orange, Blue, Yellow, or Green.")

else:
    print("Invalid choice. Please type 'Scary' or 'Funny' to decide your Halloween costume.")