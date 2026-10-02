name = "Kitty"
age = 1
hunger = 50
happiness = 50
has_food = True
game_running = True 

def kitty_eats():
        global hunger, happiness, has_food
        hunger -= 20
        happiness += 10
        print("Kitty ate!")
        print("Happiness level:", happiness)
        print("Hunger level:", hunger)
        has_food = False

#if has_food:
#   kitty_eats()
#else:
#   print("Kitty has no food :(")

while game_running: 
    answer = input("What do you want Kitty to do?")
    if (answer == "Eat" or answer == "eat") and has_food:
        kitty_eats()
    else:
         print("Kitty has no food :(")








