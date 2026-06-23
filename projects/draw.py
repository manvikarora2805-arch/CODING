# Step 1 & 2: Greet the user and ask for their name
print("Hello! I am your friendly chatbot assistant.")
name = input("What is your name? ")
print(f"It's nice to meet you, {name}!\n")

# Start a loop to allow the user to keep chatting
chatting = True

while chatting:
    # Step 3: Ask for their mood
    print("How are you feeling today?")
    mood = input("Please type 'good', 'bad', or 'neutral': ").lower().strip()
    
    # Step 4: Branching responses based on mood using conditional statements
    if mood == "good":
        print("That's awesome! I'm glad you're having a great day.")
    elif mood == "bad":
        print("I'm really sorry to hear that. I hope things look up for you soon!")
    else:
        print("A neutral day is a steady day. Thanks for sharing!")
    
    print() # Prints an empty line for spacing
    
    # Step 5: Follow-up question about hobbies
    hobby = input("What is your favorite hobby or activity? ")
    print(f"Wow, {hobby} sounds like an amazing way to spend your time!")
    print()
    
    # Step 6: Loop control - ask to continue or exit
    choice = input("Would you like to keep chatting? (yes/no): ").lower().strip()
    
    if choice == "no":
        chatting = False # This breaks the loop
        print() 
    elif choice == "yes":
        print("Awesome! Let's chat a bit more.\n")
    else:
        print("I'll take that as a no. Wrapping things up!\n")
        chatting = False

# Step 7: Personalized farewell message
print(f"Goodbye, {name}! Thank you for chatting with me today. Have a wonderful day!")