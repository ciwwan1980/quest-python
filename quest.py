import time

def scary_animation():
    for _ in range(10):
        print("\033[1;31;40m        ...Something's watching you...\033[m")
        time.sleep(0.5)
        print("\033[1;32;40m                                \033[m")
        time.sleep(0.5)

def jump_scare():
    print("\033[1;31;40m        !!!BOO!!!                    \033[m")

play = True

while play:
    name = input('What is your name?: ')
    print('Hey', name)
    print('Welcome to the Land of Adventure!')
    print('You find yourself standing at the entrance of a dark and mysterious door.')
    
    try:
        choice = int(input('Choose a door: Type 1, 2, or 3 to select the door number: '))

        if choice == 1:
            print('You cautiously step into the door...')
            time.sleep(1)
        
            eye_position = 0
            direction = 3
        
            for _ in range(20):
                screen = [' '] * 40  
            
                eye_position += direction
            
                if eye_position >= len(screen) - 2 or eye_position <= 0:
                    direction *= -2 
            
                screen[eye_position] = '👁'  
            
                print(''.join(screen))
            
                time.sleep(0.2)  
        
            print("You've ventured deeper into the dark")

        elif choice == 2: 
            print("Just read underline")
            scary_animation()
            jump_scare()

        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
