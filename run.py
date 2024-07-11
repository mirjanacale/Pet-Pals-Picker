# Pet Pals Picker
def display_ascii(animal):
     ascii_art = {
        "cat": '''
        
     
 /|_,-~/|
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. |
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'      

        ''',
        "dog": '''
 / \__
(    @\___
 /         O
 /   (_____/
/_____/   U
        ''',
        "fish": '''
        
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
        
 
        ''',
        "bird": '''
   (
  `-`-.
  '( @ >
   _) (
  /    )
 /_,'  / 
   \  / 
===m""m===        
 
        ''',
        "rabbit": '''
        
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
        
        
 
        ''',
        "hamster": '''
        
    
     (q\_/p)
      /. .\.-""""-.      ___
     =\_t_/=    /  `\   (
       )\ ))__ _\    |___)
      nn-nn`  `nn---'        
        
        
        
        ''',
        "snake": '''
        
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
 
        ''',
        "turtle": '''
        
                             ___-------___
                         _-~~             ~~-_
                      _-~                    /~-_
   /^\__/^\         /~  \                   /    /
 /|  O|| O|        /      \_______________/        /
| |___||__|      /       /                \          /
|          \    /      /                    \          /
|   (_______) /______/                        \ _________ /
|         / /         \                      /            /
 \         \^||         \                  /               \     /
   \         ||           \______________/      _-_       //\__//
     \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
       ~-----||====/~     |==================|       |/~~~~~
        (_(__/  ./     /                    \_\      \.
               (_(___/                         \_____)_)        
 
        ''',
        "lizard": '''
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
        ''',
        "frog": '''
        
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
        
 
        '''
    } 
print(ascii_art[animal])

def find_animal():
    answers = []

    questions = [
        ("What size of pet do you prefer?", ["Small", "Medium", "Large"]),
        ("How much time can you spend with your pet daily?", ["A few minutes", "A few hours", "All day"]),
        ("Do you prefer pets that are quiet or vocal?", ["Quiet", "Vocal"]),
        ("How much space do you have for a pet?", ["A small space", "A medium space", "A large space"]),
        ("Do you want a pet that's easy to care for?", ["Yes", "No"]),
        ("Do you prefer a pet that stays in a cage or one that roams free?", ["Cage", "Free"]),
        ("Are you okay with cleaning up after your pet?", ["Yes", "No"]),
        ("Do you want a pet that can be trained?", ["Yes", "No"]),
        ("Do you want a pet that lives a long time?", ["Yes", "No"]),
        ("Do you want a pet that's active during the day or night?", ["Day", "Night"])
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
    
    
    
    
    
# answers = find_animal()
# print(answers)
# print(display_ascii("cat"))
# print(display_ascii("snake"))


