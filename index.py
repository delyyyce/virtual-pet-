name = "Kitty"
age = 1
hunger = 50
happiness = 50
has_food = True

def kitty_eats():
        global hunger, happiness, has_food
        hunger -= 20
        happiness += 10
        print("Kitty ate!")
        print("Happiness level:", happiness)
        print("Hunger level:", hunger)
        has_food = False

if has_food:
    kitty_eats()
else:
    print("Kitty has no food :(")



