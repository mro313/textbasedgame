# Michael Oben
# TextBasedGame.py - final project for IT 140 
# 12/21/2020

def show_instructions():  
   # print some instructions
    print("\n----------------------------------------------------------------------------------")
    print("\nWelcome to the Move Out game!")
    print("How to win: You'll need to collect all your stuff BEFORE running into your roommate!")
    print("\n----------------------------------------------------------------------------------")


def main():

    current_room = 'Foyer'
    user_input = 0
    user_items = []

    def display_items():
        print("These are the following items in your collection:")
        print(user_items)

    def display_room():
        print("\n-------------------- You are in the", current_room,"--------------------")

    rooms = {
   'Foyer' : { 'East' : 'Living Room' },
   'Living Room' : { 'North' : 'Dining Room', 'East' : 'Library', 'South' : 'Bedroom', 'West' : 'Foyer', 'item' : 'TV' },
   'Dining Room' : { 'East' : 'Kitchen', 'South' : 'Living Room', 'item' : 'Table' },
   'Kitchen' : { 'West' : 'Dining Room', 'item' : 'Mug' },
   'Bedroom' : { 'East' : 'Closet', 'North' : 'Living Room', 'item' : 'Shoes' },
   'Closet' : { 'West' : 'Bedroom', 'item' : 'Tuxedo' },
   'Library' : { 'North' : 'Office', 'West' : 'Living Room', 'item' : 'Book' },
   'Office' : { 'South' : 'Library' } #villain
    }

    while user_input != 'exit':

        # user is in Foyer
        if current_room == 'Foyer':
            display_room()
            display_items()
            user_move = input('\nMove commands: Go North, Go South, Go East, Go West: ')
            
            if user_move == 'Go East':
                current_room = rooms['Foyer']['East']
            
            #insert logic for other directions
            else:
                print("\nThat didn't work. Try again.")

        # user is in the Living room
        if current_room == 'Living Room':
            display_room()
            display_items()
            
            # item logic
            if user_items.count('TV') == 0:
                print("You found the", rooms['Living Room']['item'])
                decision = input("Want to collect this item? Type 'yes' or 'no' ")
            
                # adds item to user list, removes from dictionary
                if decision == 'yes':
                    print('Cool!')
                    user_items.append('TV')
                    del rooms['Living Room']['item']

                else:
                    print('Okay!') 

            # move logic
            user_move = input('\nMove commands: Go North, Go South, Go East, Go West: ')

            if user_move == 'Go North':
                current_room = rooms['Living Room']['North']

            elif user_move == 'Go South':
                current_room = rooms['Living Room']['South']
            
            elif user_move == 'Go East':
                current_room = rooms['Living Room']['East']
            
            elif user_move == 'Go West':
                current_room = rooms['Living Room']['West']
            
            else:
                print("\nThat didn't work. Try again.")

        # user is in the Dining Room
        if current_room == 'Dining Room':
            display_room()
            display_items()
            
            # item logic
            if user_items.count('Table') == 0:
                print("You found the", rooms['Dining Room']['item'])
                decision = input("Want to collect this item? Type 'yes' or 'no' ")
            
                # adds item to user list, removes from dictionary
                if decision == 'yes':
                    print('Cool!')
                    user_items.append('Table')
                    del rooms['Dining Room']['item']

                else:
                    print('Okay!') 

            # move logic
            user_move = input('\nMove commands: Go North, Go South, Go East, Go West: ')

            if user_move == 'Go East':
                current_room = rooms['Dining Room']['East']
            
            elif user_move == 'Go South':
                current_room = rooms['Dining Room']['South']

            else:
                print("\nThat didn't work. Try again.")

        # user is in the Kitchen
        if current_room == 'Kitchen':
            display_room()
            display_items()
            
            # item logic
            if user_items.count('Mug') == 0:
                print("You found the", rooms['Kitchen']['item'])
                decision = input("Want to collect this item? Type 'yes' or 'no' ")
            
                # adds item to user list, removes from dictionary
                if decision == 'yes':
                    print('Cool!')
                    user_items.append('Mug')
                    del rooms['Kitchen']['item']

                else:
                    print('Okay!') 

            # move logic
            user_move = input('\nMove commands: Go North, Go South, Go East, Go West: ')

            if user_move == 'Go West':
                current_room = rooms['Kitchen']['West']

            else:
                print("\nThat didn't work. Try again.")

        # user is in the Bedroom
        if current_room == 'Bedroom':
            display_room()
            display_items()
            
            # item logic
            if user_items.count('Shoes') == 0:
                print("You found the", rooms['Bedroom']['item'])
                decision = input("Want to collect this item? Type 'yes' or 'no' ")
            
                # adds item to user list, removes from dictionary
                if decision == 'yes':
                    print('Cool!')
                    user_items.append('Shoes')
                    del rooms['Bedroom']['item']

                else:
                    print('Okay!') 

            # move logic
            user_move = input('\nMove commands: Go North, Go South, Go East, Go West: ')

            if user_move == 'Go East':
                current_room = rooms['Bedroom']['East']
            
            elif user_move == 'Go North':
                current_room = rooms['Bedroom']['North']

            else:
                print("\nThat didn't work. Try again.")

        # user is in the Closet
        if current_room == 'Closet':
            display_room()
            display_items()
            
            # item logic
            if user_items.count('Tuxedo') == 0:
                print("You found the", rooms['Closet']['item'])
                decision = input("Want to collect this item? Type 'yes' or 'no' ")
            
                # adds item to user list, removes from dictionary
                if decision == 'yes':
                    print('Cool!')
                    user_items.append('Tuxedo')
                    del rooms['Closet']['item']

                else:
                    print('Okay!') 

            # move logic
            user_move = input('\nMove commands: Go North, Go South, Go East, Go West: ')

            if user_move == 'Go West':
                current_room = rooms['Closet']['West']

            else:
                print("\nThat didn't work. Try again.")

        # user is in the Library
        if current_room == 'Library':
            display_room()
            display_items()
            
            # item logic
            if user_items.count('Book') == 0:
                print("You found the", rooms['Library']['item'])
                decision = input("Want to collect this item? Type 'yes' or 'no' ")
            
                # adds item to user list, removes from dictionary
                if decision == 'yes':
                    print('Cool!')
                    user_items.append('Book')
                    del rooms['Library']['item']

                else:
                    print('Okay!') 

            # move logic
            user_move = input('\nMove commands: Go North, Go South, Go East, Go West: ')

            if user_move == 'Go North':
                current_room = rooms['Library']['North']
            
            elif user_move == 'Go West':
                current_room = rooms['Library']['West']

            else:
                print("\nThat didn't work. Try again.")

        # user is in the Office
        if current_room == 'Office':
            display_room()
            display_items()
            
            # item logic
            if len(user_items) == 6:
                print("\n\n\nCongratulations! You've won. You found all the items, and just before leaving, broke the news to your roommate.")
                break
                
            else:
                print("\n\n\nSorry! You lost. You found you roommate!ou didn't collect all the items before confronting your roommate!")
                break

show_instructions()
main()