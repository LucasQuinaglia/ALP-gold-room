from sys import exit

bag = 0

def dead_end():
  print('Is just a dead end path')
  print('you get back.')
  return back_room()
  

def back_room():
  print('This room get nothing, just walls and lights on the ceiling.')
  print('Is like a maze, you can go left or right.')
  print('Which way do you go?')
  choice = input('> ')
  if choice == 'left':
    dead_end()
  elif choice == 'right':
    print('You see a glimpse of something you never seen before.')
    print('You cannot to describe it.')
    print('You step forward.')
    return the_monster()
  else:
    print('I got no idea what that means.')
    
def the_monster():
  print('In a crossing path, you see a child.')
  print('The child apparently it is calm.')
  print('You get a bit closer.')
  print('And see something strange.')
  print('The cild get the eyes black, like the void.')
  print('You run.')
  print('You run as fast as you can.')
  print('You take the first right that you see.')
  print('Then you see a gun. You take it.')
  print('Would you take come back to face the child or get out?')
  choice = input('> ')
  if choice == 'face':
    print('You get back to the child.')
    print('You perceive that the child is blind.')
    print('You shoot the child.')
    print('The child falls and starts to crying.')
    print('And then you get the eye membrane, that is about 100 to 200 times more resistant than your skin.')
    print('You get out.')
    merchant(bag)
    
  elif choice == 'get out':
    print('You get out.')
    merchant(bag)
  else:
    print('I got no idea what that means.')
    
def merchant(bag):
    print('walking through the halls. You see somebody.')
    print('He isn\'t a human. His muscles are exposed, he has no skin.')
    print('He has a backpack full of items.')
    print('He is a merchant.')
    print('Would you like to buy something or get out?')
    choice = input('> ')
    if choice == 'buy':
      print('The merchant has a lot of items that can be useful.')
      print(f'You had {bag} gold')
      print('The merchant has a potion that can heal you for 5 gold.')
      print('He has a sword that can be useful for 10 gold.')
      print('He has a shield that can protect you for 15 gold.')
      print('What would you like to buy?')
      while choice != 'leave':
        choice = input('> ')
        if choice == 'potion':
          if bag >= 5:
            print('You bought a potion.')
            bag -= 5
            print(f'You have {bag} gold.')
            print('would you buy something else or leave?')
            choice = input('> ')
          else:
            print('You don\'t have enough gold.')
            print('would you buy something else or leave?')
            choice = input('> ')
        elif choice == 'sword':
          if bag >= 10:
            print('You bought a sword.')
            bag -= 10
            print(f'You have {bag} gold.')
            print('would you buy something else or leave?')
            choice = input('> ')
          else:
            print('You don\'t have enough gold.')
            print('would you buy something else or leave?')
            choice = input('> ')
        elif choice == 'shield':
          if bag >= 15:
            print('You bought a shield.')
            bag -= 15
            print(f'You have {bag} gold.')
            print('would you buy something else or leave?')
            choice = input('> ')
          else:
            print('You don\'t have enough gold.')
            print('would you buy something else or leave?')
            choice = input('> ')
        else:
          print('I got no idea what that means.')
    

def gold_room(): 
  print("This room is full of gold. How much do you take?") 
  choice = input("> ")
  if choice.isdigit():
    how_much = int(choice)
  else: 
    dead("Man, learn to type a number.") 
  if how_much < 50:
    print("Nice, you're not greedy, you get the gold!") 
    print('You step forward.')
    print('You see a door and get in.')
    print('You are now on the back rooms.')
    bag = how_much
    back_room()
  else: 
    dead("You greedy bastard!")

def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")   
  print("How are you going to move the bear?") 
  print("Do you take the honey or taunt bear?")
  bear_moved = False
  while True: 
    choice = input("> ")
    if choice == "take honey":
     dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear" and not bear_moved: 
      print("The bear has moved from the door.")
      print("Open the door or taunt bear again?.") 
      bear_moved = True
      choice = input("> ")
      if choice == "taunt bear":
        dead("The bear gets pissed off and chews your leg off.") 
      elif choice == "open door": 
        gold_room(bag)
      else: 
        print("I got no idea what that means.")
    else: 
      print("I got no idea what that means.")

def cthulhu_room(): 
  print("Here you see the great evil Cthulhu.")
  print("He, it, whatever stares at you and you go insane.") 
  print("Do you flee for your life or eat your head?")
  choice = input("> ")
  if "flee" in choice: 
    start()
  elif "head" in choice: 
    dead("Well that was tasty!")
  else:
    print("I got no idea what that means.")

def dead(why):
  print(why, "Good job!") 
  exit(0)

def start(): 
  print("You are in a dark room.")
  print("There is a door to your right and left.") 
  print("Which one do you take?")
  choice = input("> ")
  if choice == "left": 
    bear_room()
  elif choice == "right": 
    cthulhu_room()
  else: 
    dead("You stumble around the room until you starve.")

start()