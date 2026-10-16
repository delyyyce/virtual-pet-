name = "Kitty"
age = 1
hunger = 50
happiness = 50
energy = 50
has_food = True
game_running = True 

def kitty_eats():
    global hunger, happiness, has_food
    #hunger += 20
    if hunger + 20 > 100:
        hunger = 100
    else: 
        hunger += 20
    #happiness += 10
    if happiness + 10 > 100:
        happiness = 100
    else: 
        happiness += 10
    print("Kitty ate!")
    print("Happiness level:", happiness)
    print("Hunger level:", hunger)
    has_food = False
  

def kitty_sleeps():
    global energy, happiness, hunger
    #energy += 20
    if energy + 20 > 100:
        energy = 100
    else: 
        energy += 20
    #happiness += 10
    if happiness + 10 > 100:
        happiness = 100
    else: 
        happiness += 10
    #hunger -= 10
    if hunger - 10 < 0:
        hunger = 0
    else:
        hunger -= 10
    print("Kitty slept!")
    print("Happiness level:", happiness)
    print("Energy level:", energy)
    print("Hunger level:", hunger)



#if has_food:
#   kitty_eats()
#else:
#   print("Kitty has no food :(")

while game_running: 
    answer = input("What do you want Kitty to do?")
    answer = answer.lower()
    #if (answer == "Eat" or answer == "eat") and has_food:
        #kitty_eats()
    #else:
         #print("Kitty has no food :(")
    if (answer == "eat") and has_food:
        kitty_eats()
    elif (answer == "eat") and not has_food:
        print("Kitty has no food.")
    elif (answer == "sleep"):
        kitty_sleeps()
    elif (answer == "quit"):
        print("Goodbye!")
        game_running = False







