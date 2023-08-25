import time

play = True

while play:
    name = input('What is your name?: ')
    print('Hey', name)
    print('Welcome to the Land of Adventure!')
    print('You find yourself standing at the entrance of a dark and mysterious door.')
    print('1. Enter the door \n2. Leave')
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
        
        print("You've venture deeper into the dark")
      