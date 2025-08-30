import re

from colorama import Fore, Style, init

init(autoreset = True)

def check_password_strength(password : str)-> str:
    
    strength_points = 0
    feedback = [ ]

    #Lenght Check
    
    if len(password) >= 12:
        strength_points += 2
    elif len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password is too short (Minimum 8 characters)")

    #Upper/Lower Case Check

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength_points +=1
        
    else:
        feedback.append("Use both lowercase and uppercase letters")

    #Number Check
    
    if re.search(r'[0-9]', password):
        strength_points += 1
        
    else:
        feedback.append("Add at least one number")

    #Special Character
    if re.search(r'[\W_]',password):
        strength_points += 1

    else:
        feedback.append("Add a special character")
    

    #Strength Evaluation
        
    if strength_points >=5:
        return Fore.GREEN + "Strong" + Style.RESET_ALL

    elif strength_points >= 3:
        return Fore.YELLOW + "Moderate\n"+ "\n".join(feedback) + Style.RESET_ALL
    
    else:
        return Fore.RED + "Weak\n"+ "\n".join(feedback) + Style.RESET_ALL

    #Loop
if __name__ == "__main__":
    print("Password Strength Checker")
    while True:
        pwd = input(Fore.MAGENTA +"Enter a password (or type 'quit' to exit): " + Style.RESET_ALL)
        if pwd.lower() == "quit":
            print(Fore.CYAN + "Goodbye" + Style.RESET_ALL)
            break
        print(check_password_strength(pwd))
            
        
            
    







    
        
