import random
#dictionary of emojis and their descriptions
emoji_dict ={
    "😀":"grinning face",
    "😃":"grinning face with big eyes",
    "😄":"grinning face with smiling eyes",
    "😁":"beaming face with smiling eyes",
    "😆":"grinning squinting face",
    "😅":"grinning face with sweat",
    "😂":"face with tears of joy",
    "🤣":"rolling on floor laudhing",
    "😎":"smiling face with sunglasses",
    "😍":"heart eyes",
    "😘":"face blowing a kiss",
    "😜":"winking face with tongue",
    "🤔":"thinking face",
    "😎":"cool face with sunglasses",
    "😢":"crying face",
    "😡":"pouting face",
    "🥺":"pleading face",
    "❤":"red heart",
    "👍":"thumbs up",
    "🎉":"party popper",
    "🍕":"pizza",
    "🌟":"star",
    "🐶":"dog",
    "🚗":"car",
    "🔥":"fire",
}
#function to start the emoji to text game
def emoji_game():
    #Introduction to the game
    print("Welcome to the 'convert the Emoji to Text' Game!")
    print("In this game, you will be shown an emoji.Type the correct description to earn points.")
    print("Type 'quit' to exit the game.")
    print("-"*40)

    score=0 #keep track of the player's score
    emojis=list(emoji_dict.keys()) #Extract all emoji keys from the dictionary

    #Infinite loop to keep the game running until the player chooses to quit
    while True:
        emoji=random.choice(emojis) #Randomly selects an emoji from the list
        print(f"Emoji: {emoji}")

        #Prompts the user for their answer and standerdizes it from comparison
        answer=input("Your Answer:").strip().lower()

        #Exist the game if the user types 'quit'
        if answer=="quit":
            print(f"Game Over! Your Final Score: {score}")
            break

        #Checks if the answer is correct
        if answer==emoji_dict[emoji]:
            print("Correct!🎉") #Print the correct answer
            score+=1 #Increments the score
        else:
            #Displays the correct answer if the user's input is wrong
            print(f"Wrong! The correct answer is: '{emoji_dict[emoji]}'")

        #Displays the player's current score
        print(f"Your Current Score: {score}") 
        print("-"*40)
    
#start the game
emoji_game()