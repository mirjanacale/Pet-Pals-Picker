import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Function to display the title in ASCII art with color
def display_title():
    title = """
    
  _____  ______ _______            _____        _       _____            _____ _____ _____ _  ________ _____   
 |  __ \|  ____|__   __|          |  __ \ /\   | |     / ____|          |  __ \_   _/ ____| |/ /  ____|  __ \  
 | |__) | |__     | |     ______  | |__) /  \  | |    | (___    ______  | |__) || || |    | ' /| |__  | |__) | 
 |  ___/|  __|    | |    |______| |  ___/ /\ \ | |     \___ \  |______| |  ___/ | || |    |  < |  __| |  _  /  
 | |    | |____   | |             | |  / ____ \| |____ ____) |          | |    _| || |____| . \| |____| | \ \  
 |_|    |______|  |_|             |_| /_/    \_\______|_____/           |_|   |_____\_____|_|\_\______|_|  \_\ 
                                                                                                               
                                                                                                                                                              
    """
    print(Fore.CYAN + Style.BRIGHT + title + Style.RESET_ALL)
    
def display_ascii(animal):
    ascii_art = {
        "cat": f'''
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
{Fore.RESIT_ALL}
        ''',
        "dog": f'''
{Fore.RED}
        
 / \__
(    @\___
 /         O
 /   (_____
/_____/   U 
{Style.RESIT_ALL}
        ''',
        "fish": F'''
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
{Style.REST_ALL}
 
        ''',
        "bird": f'''
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
        "rabbit": F'''
{Fore.GREEN}
        
  / |
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
      "hamster": f'''
        
{Fore.MAGENTA}
     (q\_/p)
      /. .\.-""""-.      ___
     =\_t_/=    /  `\   (
       )\ ))__ _\    |___)
      nn-nn`  `nn---'  
            
{Style.RESET_ALL}        
        
        
        ''',
        "snake": f'''
{Fore.YELLOW}
        
           /^\/^|
         _|__|  O|
\/     /~     \_/ |
 \____|__________/  |
        \_______      |
                `\     \                 |
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

            
        "turtule": f'''
{Fore.GREEN}
                    __
         .,-;-;-,. /'_\
       _/_/_/_|_\_\) /
     '-<_><_><_><_>=/\
      `/_/====/_/-'\_\
        ""     ""    ""        
{Style.RESET_ALL} 
        ''', 
        "lizard": f'''  
{Fore.RED} 
              ____...---...___
___.....---"""        .       ""--..____
     .                  .            .
 .             _.--._       /|
        .    .'()..()`.    / /
            ( `-.__.-' )  ( (    .
   .         \        /    \ /
       .      \      /      ) )        .
            .' -.__.- `.-.-'_.'
 .        .'  /-____-\  `.-'       .
          \  /-.____.-\  /-.
           \ \`-.__.-'/ /\|\|           .
          .'  `.    .'  `.
          |/\/\|    |/\/\|
          
{Style.RESET_ALL}
        ''',      
        "frog": f'''
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
    //| \\  `---'  // |\\
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

    
    answer = int(input("Choose an option: "))

    return choices[answer - 1]



def find_animal():
    answers = []

    questions = [
        ("How much room in your house is physically set aside for a pet? Think about how big your living space is, if you have a yard, and what other spaces your pet might use.Which pet size do you prefer?", ["Small", "Medium", "Large"]),
        ("How much time can you actually dedicate to your pet's daily care and interaction? When responding, take into account your work schedule, social obligations, and personal downtime?", ["A few minutes", "A few hours", "All day"]),
        ("Which type of pet would you rather have—one that is bubbly and lively all the time, or one that is more reserved and quiet? Consider how much noise you can handle and how it might impact your home.", ["Quiet", "Vocal"]),
        ("How much room in your house is physically set aside for a pet? Consider the size of your living space, your yard's size, and any additional spaces the pet might use?", ["A small space", "A medium space", "A large space"]),
        ("Are you looking for a pet that requires minimal effort to care for, or are you prepared to invest significant time and effort into its care and maintenance?", ["Yes", "No"]),
        ("Which would you prefer—a pet that is free to roam your living area or one that is housed in a cage or other enclosure? Take into account your comfort level and any safety issues?", ["Cage", "Free"]),
        ("Are you willing to regularly clean up after your pet, including tasks such as litter box maintenance, cleaning cages, and picking up waste?", ["Yes", "No"]),
        ("Do you think it's important that your pet learn tricks, obey commands, or adopt certain behaviors? Consider the amount of time and energy you are prepared to devote to your training?", ["Yes", "No"]),
        ("Do you want a pet that has a long lifespan, potentially providing many years of companionship, or are you looking for a shorter-term commitment?", ["Yes", "No"]),
        ("Would you prefer a pet that is most active during the day when you are likely to be awake and available to interact, or one that is more active at night?", ["Day", "Night"])
    ]

    for question, choices in questions:
        answer = ask_question(question, choices)
        answers.append(answer)
         # return the answers ( map answers to specific pets)
         
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


