from sys import exit

bag = 0

inventory = []

def dead_end():
    print('It\'s just a dead-end path.')
    print('You get back.')
    return back_room()
  
def final_battle():
    print("As you proceed, you feel a chilling breeze.")
    print("The walls around you seem to close in, the lights flickering erratically.")
    print("You step into a vast chamber, where the temperature drops drastically.")
    print("At the center of the room stands a towering figure, cloaked in darkness.")
    print("You can barely make out its features, but its eyes glow a menacing red.")
    print("This is the source of all the horrors you’ve faced.")
    print("The final villain stands before you, waiting silently.")

    print("Do you confront the villain, attempt to negotiate, or flee?")
    choice = input("> ").lower()

    if "confront" in choice:
        confront_villain()
    elif "negotiate" in choice:
        negotiate_villain()
    elif "flee" in choice:
        flee_villain()
    else:
        print("I have no idea what that means.")
        return final_battle()

def confront_villain():
    global bag
    global inventory
    print("You muster all your courage and step forward to confront the villain.")
    print("The villain lets out a deep, resonant laugh that echoes through the chamber.")
    print("It raises a hand, and you feel an invisible force pressing down on you.")
    
    if "sword" in inventory:
        print("You unsheathe the sword you bought from the merchant.")
        print("The blade seems to hum with energy as you charge at the villain.")
        print("The villain recoils slightly as you strike, but it quickly recovers.")
        print("A fierce battle ensues, with sparks flying as your sword clashes against the villain's dark energy.")
        print("In a moment of desperation, you notice a glowing weak spot on the villain's chest.")
        print("Do you aim for the weak spot or continue fighting?")
        
        choice = input("> ").lower()
        if "aim" in choice:
            print("You gather all your strength and aim for the glowing spot.")
            print("Your sword pierces through the villain's defenses, striking the weak spot directly.")
            print("The villain lets out a roar of agony as it crumbles to the ground, defeated.")
            print("You stand victorious, but exhausted. The darkness begins to fade away.")
            print("You have saved yourself, and perhaps the world, from a terrible fate.")
        else:
            print("You continue fighting, but the battle drags on.")
            print("The villain's power seems endless, and you begin to tire.")
            print("In your fatigue, you miss an opening, and the villain strikes you down.")
            print("You fought bravely, but in the end, the villain was too powerful.")
            if "potion" in inventory:
                print("As you lay on the ground, you remember the potion you bought from the merchant.")
                print("You quickly drink it, feeling a surge of energy.")
                print("You rise to your feet, ready to face the villain once more.")
                print("This time, you aim for the weak spot and strike true, defeating the villain.")
                print("You have emerged victorious, but the battle has taken its toll.")
                print("You have saved yourself, and perhaps the world, from a terrible fate.")
            elif 'shield' in inventory:
                print("As you lay on the ground, you remember the shield you bought from the merchant.")
                print("You quickly raise the shield, deflecting the villain's attack.")
                print("The shield absorbs the dark energy, and you feel a surge of power.")
                print("You rise to your feet, ready to face the villain once more.")
                print("This time, you aim for the weak spot and strike true, defeating the villain.")
                print("You have emerged victorious, but the battle has taken its toll.")
                print("You have saved yourself, and perhaps the world, from a terrible fate.")
            else:
                dead("You should have prepared better.")
    else:
        print("Without a weapon, you are helpless against the villain's might.")
        print("The villain easily overpowers you, and you fall to the ground.")
        dead("You should have prepared better.")

def negotiate_villain():
    print("You raise your hands in a gesture of peace, hoping to negotiate with the villain.")
    print("The villain narrows its eyes, its dark aura intensifying.")
    print("It speaks in a voice that chills you to the bone: 'Why should I spare you?'")
    print("Do you offer to serve the villain, or try to persuade it to leave peacefully?")
    
    choice = input("> ").lower()
    if "serve" in choice:
        print("You offer to serve the villain, promising loyalty in exchange for your life.")
        print("The villain considers your offer and then smiles cruelly.")
        print("'Very well,' it says. 'But you will regret this decision.'")
        print("You are bound to the villain's will, becoming its pawn in a dark and twisted world.")
        print("You survive, but at a terrible cost.")
    elif "persuade" in choice:
        print("You try to persuade the villain that there is no need for violence.")
        print("The villain listens silently, and for a moment, you think you might have succeeded.")
        print("But then it laughs, a cold, heartless sound.")
        print("'You are a fool to think you can change my mind,' it says.")
        print("The villain attacks without warning, and you are caught off guard.")
        dead("Your attempt at diplomacy has failed.")

def flee_villain():
    print("Realizing you are no match for the villain, you turn and flee.")
    print("The villain's laughter echoes behind you as you sprint through the dark corridors.")
    print("But no matter how fast you run, the darkness seems to follow, growing stronger.")
    print("You find yourself back where you started, trapped in the chamber with the villain.")
    print("There is no escape. You must face the villain, whether you want to or not.")
    return final_battle()
  
def after_merchant():
    print("You continue your journey through the halls.")
    print("The sense of foreboding grows stronger with each step.")
    print("Finally, you reach a large, ominous door.")
    print("You know that beyond this door lies the final challenge.")
    print("Do you enter?")
    choice = input("> ").lower()
    if "yes" in choice or "enter" in choice:
        final_battle()
    else:
        print("You hesitate, unsure if you're ready for what lies ahead.")
        print("But you know that there is no other way.")
        print("With a deep breath, you push open the door and step inside.")
        final_battle()


def back_room():
    print('This room has nothing, just walls and lights on the ceiling.')
    print('It\'s like a maze, you can go left or right.')
    print('Which way do you go?')
    choice = input('> ').lower()
    if choice == 'left':
        return dead_end()
    elif choice == 'right':
        print('You see a glimpse of something you have never seen before.')
        print('You cannot describe it.')
        print('You step forward.')
        return the_monster()
    else:
        print('I have no idea what that means.')
        return back_room()

def the_monster():
    print('In a crossing path, you see a child.')
    print('The child appears calm.')
    print('You get a bit closer.')
    print('And see something strange.')
    print('The child\'s eyes turn black, like the void.')
    print('You run.')
    print('You run as fast as you can.')
    print('You take the first right that you see.')
    print('Then you see a gun. You take it.')
    print('Would you come back to face the child or get out?')
    choice = input('> ').lower()
    if choice == 'face':
        print('You go back to the child.')
        print('You realize that the child is blind.')
        print('You shoot the child.')
        print('The child falls and starts crying.')
        print('And then you take the eye membrane, which is about 100 to 200 times more resistant than your skin.')
        print('You get out.')
        merchant()
    elif choice == 'get out':
        print('You get out.')
        merchant()
    else:
        print('I have no idea what that means.')
        return the_monster()

def merchant():
    global bag
    print('Walking through the halls, you see somebody.')
    print('He isn\'t human. His muscles are exposed, he has no skin.')
    print('He has a backpack full of items.')
    print('He is a merchant.')
    print('Would you like to buy something or get out?')
    choice = input('> ').lower()
    if choice == 'buy':
        print('The merchant has a lot of items that can be useful.')
        print(f'You have {bag} gold.')
        print('The merchant has a potion that can heal you for 5 gold.')
        print('He has a sword that can be useful for 10 gold.')
        print('He has a shield that can protect you for 15 gold.')
        print('What would you like to buy?')
        while choice != 'leave':
            choice = input('> ').lower()
            if choice == 'potion':
                if bag >= 5:
                    print('You bought a potion.')
                    inventory.append('potion')
                    bag -= 5
                    print(f'You have {bag} gold.')
                    print('You want to leave or will buy something else?')
                else:
                    print('You don\'t have enough gold.')
                    print('You want to leave or will buy something else?')
            elif choice == 'sword':
                if bag >= 10:
                    print('You bought a sword.')
                    inventory.append('sword')
                    bag -= 10
                    print(f'You have {bag} gold.')
                    print('You want to leave or will buy something else?')
                else:
                    print('You don\'t have enough gold.')
                    print('You want to leave or will buy something else?')
            elif choice == 'shield':
                if bag >= 15:
                    print('You bought a shield.')
                    inventory.append('shield')
                    bag -= 15
                    print(f'You have {bag} gold.')
                    print('You want to leave or will buy something else?')
                else:
                    print('You don\'t have enough gold.')
                    print('You want to leave or will buy something else?')
        
        after_merchant()
    elif choice == 'get out':
      print('You decide not to interact with the merchant.')
      after_merchant()
    else:
      print('I have no idea what that means.')    

def gold_room():
    global bag
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy. You take the gold!")
        print('You step forward.')
        print('You see a door and get in.')
        print('You are now in the back rooms.')
        bag = how_much
        back_room()
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("Do you take the honey or taunt the bear?")
    bear_moved = False
    while True:
        choice = input("> ").lower()
        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("Open the door or taunt the bear again?.")
            bear_moved = True
            choice = input("> ").lower()
            if choice == "taunt bear":
                dead("The bear gets pissed off and chews your leg off.")
            elif choice == "open door":
                gold_room()
            else:
                print("I got no idea what that means.")
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    choice = input("> ").lower()
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        print("I got no idea what that means.")
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    choice = input("> ").lower()
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()