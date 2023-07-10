# Austin Hoff
def game_instructions():
    print("Back from the dead")
    print("Collect 6 items to defeat the Grim Reaper or be killed by him.")
    print("Move commands: south, north, east, west")
    print("Type quit to end game")
    print("Add item to Inventory type: get 'item name'")
game_instructions()

#Shows rooms available to move and items in each room
rooms = {

    'Living Room': {'South': 'Master Bedroom', 'East': 'Kitchen',
                         'West': 'Bathroom', 'North': 'Guest Bedroom',},
         'Master Bedroom': {'East': 'Vault', 'North': 'Living Room',
                            'item': 'Cross'},
         'Vault': {'West': 'Master Bedroom',
                    'item': 'Script'},
         'Kitchen': {'West': 'Living Room', 'North': 'Garage',
                     'item': 'Holy Water'},
         'Garage': {'West': 'Kitchen',
                    'item': 'Grim Reaper'},
         'Bathroom': {'East': 'Living Room',
                      'item': 'Flashlight'},
         'Guest Bedroom': {'South': 'Living Room', 'East': 'Office',
                           'item': 'Keys'},
         'Office': {'West': 'Guest Bedroom',
                    'item': 'Magic Box'},
}
print('------------------------')
current_room = 'Living Room' # starts player in the Great Hall
inventory = [] # Adds an inventory
def get_new_room(current_room, direction):
    new_room = current_room # declares new room as current room.
    for i in rooms: # starts loop
        if i == current_room: # if statement
            if direction in rooms[i]: # if statement
                new_room = rooms[i][direction] # Assigns new room.
    return new_room #returns new room

def get_item(current_room):
    if 'item' in rooms[current_room]: #if statement
        return rooms[current_room]['item'] #return statement
    else:
        return 'This room has no item!' #return statement

while current_room: # gameplay loop
    print('You are in', current_room) # tells player what room they are in.
    print('Inventory:', inventory) # shows player their inventory
    item = get_item(current_room)  # defines item as get item
    print('You found the:', item) # tells the player what item they have found
    if item == 'Grim Reaper': #if statement
        print('The Grim Reaper found you before you collected all the necessary items to survive! The game has ended!')  # notifies player game has ended.
        break # ends game
    print('----------------------')
    direction = input('Enter direction you would like to move. >>')  # gets direction from player.
    direction = direction.capitalize()  # Capitalizes the players input to match what is in the dictionary.

    if direction == 'North' or direction == 'South' or direction == 'East' or direction == 'West': # if statement
        new_room = get_new_room(current_room, direction) # Calling function
        if new_room == current_room: # if statement
            print('That is a wall not an exit. Try Again!') # Print statement
        else:
            current_room = new_room # declares current room as new room
    elif direction == 'quit':
        print('Thanks for playing! Play again soon!')
        break
    elif direction == str('get ' + item).capitalize(): #input statement to add item
        if 'item' in inventory: # if statement
            print('You have already collected this item. Move to another room!') #print statement
        else:
            inventory.append(item) # adds item to inventory
    else:
        print('Not a valid direction!') # Print statement
    if len(inventory)==6: # if statement
        print('Congratulations!! You have collected all the necessary items and have safely put the Grim Reaper back to sleep!') # print statement