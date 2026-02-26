print("Welcome to the Nail Polish Matcher!")

# This function displays a list of available nail polish colors
def show_available_colors():
    # List of nail polish colors (list data type)
    available_colors = ["Red", "Blue", "Pink", "Nude", "Purple"]
    
    print("Available colors:")
    for color_option in available_colors:   # Loop through list
        print("-", color_option)


# This function checks if a color matches the skin tone
def check_color_match(skin_tone, chosen_color):
    # Decision-making structure
    if skin_tone == "Warm" and chosen_color == "Blue":
        print("That color may not be the best match for a Warm skin tone.")
    else:
        print("Great choice!", chosen_color, "looks good with", skin_tone, "tones.")


continue_program = True   # Boolean data type

while continue_program:   # Loop for repeated tasks
    
    print("\n1. Pick a color")
    print("2. Match skin tone")
    
    user_selection = input("Please enter your choice (1 or 2): ")
    
    if user_selection == "1":
        show_available_colors()
        preferred_color = input("What is your preferred color? ")
        print("You selected", preferred_color)
        
    elif user_selection == "2":
        show_available_colors()
        skin_tone = input("Enter your skin tone (Warm, Cool, Neutral, or Unknown): ")
        
        if skin_tone == "Unknown":
            print("We recommend Neutral for you!")
            skin_tone = "Neutral"
            
        chosen_color = input("What color would you like to wear? ")
        check_color_match(skin_tone, chosen_color)
        
    else:
        print("Invalid choice. Please enter 1 or 2.")
    
    repeat_answer = input("Would you like to pick again? (Yes/No): ")
    
    if repeat_answer == "No":
        continue_program = False   # Boolean controls loop


print("Thank you for using the Nail Polish Matcher!")