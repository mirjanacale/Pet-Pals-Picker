import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
quit
# Function to display the title in ASCII art with color
def display_title():
    title = r"""
  ___     _     ___      _      ___ _    _            
 | _ \___| |_  | _ \__ _| |___ | _ (_)__| |_____ _ _  
 |  _/ -_)  _| |  _/ _` | (_-< |  _/ / _| / / -_) '_| 
 |_| \___|\__| |_| \__,_|_/__/ |_| |_\__|_\_\___|_|                                                                                                                                                             
    """
    print(Fore.CYAN + Style.BRIGHT + title + Style.RESET_ALL)
def display_ascii(animal):
    ascii_art = {
        "cat": rf'''
{Fore.YELLOW} 
 /|_,-~/|
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. |
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'      
{Style.RESET_ALL}
        ''',
        "dog": rf'''
{Fore.RED}        
 / \__
(    @\___
 /         O
 /   (_____
/_____/   U 
{Style.RESET_ALL}
        ''',
        "fish": rf'''
{Fore.CYAN}
       o                 o
                  o
         o   ______      o
           _/  (   \_
 _       _/  (       \_  O
| \_   _/  (   (    0  |
|== \_/  (   (          |
|=== _ (   (   (        |
|==_/ \_ (   (          |
|_/     \_ (   (    \__/
          \_ (      _/
            |  |___/
           /__/        
{Style.RESET_ALL}
 
        ''',
        "bird": rf'''
{Fore.BLUE}
   (
  `-`-.
  '( @ >
   _) (
  /    )
 /_,'  / 
   \  / 
===m""m===  
{Style.RESET_ALL}      
        ''',
        "rabbit": rf'''
{Fore.GREEN}
    / _ |
   | / \ |
   ||   || _______
   ||   || |\     |
   ||   || ||\     |
   ||   || || \    |
   ||   || ||  \__/
   ||   || ||   ||
    \_/ \_/ \_//
   /   _     _   |
  /               |
  |    O     O    |
  |   \  ___  /   |                           
 /     \ \_/ /     |
/  -----  |  --\    /
|     \__/|\__/ \   |
\       |_|_|       /
 \_____       _____/
       \     /
       |     |        
{Style.RESET_ALL}        
        ''',
      "hamster": rf'''
{Fore.MAGENTA}
     (q\_/p)
      /. .\.-""""-.      ___
     =\_t_/=    /  `\   (
       )\ ))__ _\    |___)
      nn-nn`  `nn---'  
{Style.RESET_ALL}          
        ''',
      "snake": rf'''
{Fore.YELLOW}
           /^\/^|
         _|__|  O|
\/     /~     \_/ |
 \____|__________/  |
        \_______      |
                 \     \                 |
                  |     |                  |
                 /      /                    |
                /     /                       ||
              /      /                         \ |
             /     /                            \  |
           /     /             _----_            \   |
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~        
{Style.RESET_ALL}
        ''',  
        "turtle": rf'''
{Fore.GREEN}
                    __
         .,-;-;-,. /'_/
       _/_/_/_|_\_\) /
     '-<_><_><_><_>=/|
       /_/====/_/-'\_|
        ""     ""    ""        
{Style.RESET_ALL} 
        ''', 
        "lizard": rf'''  
{Fore.RED} 
              ____...---...___
___.....---"""        .       ""--..____
     .                  .            .
 .             _.--._       /|
        .    .'()..() .    / /
            ( -.__.-' )  ( (    .
   .         \        /    \ /
       .      \      /      ) )        .
            .' -.__.- `.-.-'_.'
 .        .'  /-____-\  `.-'       .
          \  /-.____.- '  / .
           \ \`-.__.-'/ /\|\|           .
          .'  `.    .'  `.
          |/\/\|    |/\/\|
          
{Style.RESET_ALL}
        ''',      
        "frog": rf'''
{Fore.GREEN}
         o  o   o  o
         |\ / \^/ \|
         |,-------.|
       ,-.(|)   (|),-.
       \_*._ ' '_.* _/
        /`-.`--' .-'/
   ,--./    `---'    \,--.
   \   |(  )     (  )|   /
    \  | ||       || |  /
     \ | /|\     /|\ | /
     /  \-._     _,-/  /
    //| \   ---'  // | \ 
   /,-.,-.\       /,-.,-./
  o   o   o      o   o    o        
{Style.RESET_ALL}
        '''
    } 
    print(ascii_art[animal])
def ask_question(question, choices):
    """
    Asks a question to the user and returns their choice.

    Args:
        question (str): The question to ask the user.
        choices (List[str]): The list of possible choices for the user.
    Returns:
        str: The chosen option from the list of choices.
    """
    print(question)
    # Loop through the choices and print them with an index
    for idx, choice in enumerate(choices, 1):
        
        print(f"{idx}. {choice}")
        
    while True:
        try:
            answer = int(input("Choose an option by entering the corresponding number:\n"))
            if 1 <= answer <= len(choices):
                return choices[answer - 1]
            else:
                print(f"Please enter a number between 1 and {len(choices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        
def find_animal():
    answers = []

    questions = [
        ("Which pet size do you prefer?", ["Small", "Medium", "Large"]),
        ("How much time can you give to your pet's?", ["A few minutes", "A few hours", "All day"]),
        ("Which type of pet would you rather have?", ["Quiet", "Vocal"]),
        ("How much space do you think your pet needs?", ["A small space", "A medium space", "A large space"]),
        ("Are you looking for a pet that requires minimal effort to care for?", ["Yes", "No"]),
        ("Which would you prefer a pet that is free, or in the cage?", ["Cage", "Free"]),
        ("Are you willing to regularly clean up after your pet?", ["Yes", "No"]),
        ("Do you think it's important that your pet learn tricks?", ["Yes", "No"]),
        ("Do you want a pet that has a long lifespan?", ["Yes", "No"]),
        ("Would you prefer a pet that is active during the day, or at night?", ["Day", "Night"])
    ]
    for question, choices in questions:
        answer = ask_question(question, choices)
        answers.append(answer)
    
         # Decision logic based on user answers
    if answers[0] == "Small" and answers[1] == "A few minutes":
        if answers[2] == "Quiet":
            if answers[6] == "Yes":
                return "fish", "A fish can be a great pet if you prefer a quiet, low-maintenance companion."
            else:
                return "frog", "A frog is a good choice for a quiet and minimal care pet."
        else:
            return "bird", "A bird can be a lively companion in a small space."
    elif answers[0] == "Small" and answers[1] == "A few hours":
        if answers[3] == "A small space":
            if answers[7] == "Yes":
                return "hamster", "A hamster is a small, low-maintenance pet that can provide entertainment."
            else:
                return "rabbit", "A rabbit can be a gentle pet if you have a bit more space and time."
        else:
            return "lizard", "A lizard is a good choice for a small space and moderate care needs."
    elif answers[0] == "Medium":
        if answers[4] == "Yes":
            return "cat", "A cat can be a loving companion that is fairly independent."
        else:
            return "dog", "A dog can be a loyal and affectionate pet if you're willing to invest time in training."
    elif answers[0] == "Large":
        if answers[5] == "Free":
            if answers[8] == "Yes":
                return "snake", "A snake can be an intriguing pet that requires minimal interaction."
            else:
                return "turtle", "A turtle is a long-living pet that can be fascinating to observe."
        else:
            return None, "Sorry, there's no suitable pet recommendation based on your preferences."

    return None, "Sorry, there's no suitable pet recommendation based on your preferences."
       
  
def main():
    """
    The main function that runs the Animal Adoption Quiz.
    """
    # Print welcome message
    print("Welcome to the Pet Pals Picker!")

    # Find the best animal based on user answers
    animal, description = find_animal()

    # If an animal is found, display it and its description
    if animal:
        print(f"The best animal for you is a {animal}!")
        print(description)
        # Display ASCII art of the animal
        display_ascii(animal)
    else:
        # If no suitable animal is found, display the description
        print(description)
# Run the main function
if __name__ == "__main__":
    main()
        
        
        

    
    
    
    
    
# answers = find_animal()
# print(answers)
# print(display_ascii("cat"))
# print(display_ascii("snake"))


