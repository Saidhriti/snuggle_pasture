# modules
import pygame
import os
import time
import sys
import random

# initialise pygame
pygame.init()

# variables needed for below functions
list_of_locations = ["Home", "Pretty Pets", "Grape Goods", "Awful Attire", "Faerie Florist", "Toadstool Tavern"]

player_location = "Home"

locations_art = {
    "Home": r'''  
      __________ ,%%&%,
     /\     _   \%&&%%&%
    /  \___/^\___\%&%%&&
    |  | []   [] |%\Y&%\'
    |  |   .-.   | ||  
  ~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
       `""") )"""` ''',
    "Pretty Pets": r"""
                            +&-
                          _.-^-._    .--.
                       .-'   _   '-. |__|
                      /     |_|     \|  |
                     /               \  |
                    /|     _____     |\ |
                     |    |==|==|    |  |
 |---|---|---|---|---|    |--|--|    |  |
 |---|---|---|---|---|    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""",
     "Grape Goods": r'''
         _
      _-'_'-_
   _-' _____ '-_
_-' ___________ '-_
 |___|||||||||___|
 |___|||||||||___|
 |___|||||||o|___|
 |___|||||||||___|
 |___|||||||||___|
 |___|||||||||___|
''',
     "Awful Attire":r'''
====!====!=====!=====!====!===!===!=====!===!===!====
      /`\__/`\   /`\   /`\  |~| |~|  /)=I=(\  /`"""`\
     |        | |   `"`   | | | | |  |  :  | |   :   |
     '-|    |-' '-|     |-' )/\ )/\  |  T  \ '-| : |-'
       |    |     |     |  / \// \/  (  |\  |  '---'
       '.__.'     '.___.'  \_/ \_/   |  |/  /
                                     |  /  /
                                     |  \ /
                                     '--'`''',
     "Faerie Florist": r"""
.'.         .'.
|  \       /  |
'.  \  |  /  .'
  '. \\|// .'
    '-- --'
    .'/|\'.
   '..'|'..' """,
     "Toadstool Tavern": r"""
                       .-'~~~-.
                     .'o  oOOOo`.
                    :~~~-.oOo   o`.
                     `. \ ~-.  oOOo.
                       `.; / ~.  OO:
                       .'  ;-- `.o.'
                      ,'  ; ~~--'~
                      ;  ;
_______\|/__________\\;_\\//___\|/________"""                       }

# general functions 
def check_name(name):
  while name == "":
    name = input("｡･:*˚:✧｡Please enter a name to begin playing!｡✧:˚*:･｡\n\n(⌒▽⌒)☞ ")
    print()
  return name.title()

def loading(x):
  time.sleep(x)

def text_loading(string, delay = 0.05):
    for char in string:
        time.sleep(delay) 
        print(char, end='', flush=True) 

def animation():
    start_time = time.time()
    while time.time() - start_time < 5:
        print('\r~(˘▾˘~)', end='')
        time.sleep(0.5)
        print('\r(~˘▾˘)~', end='')
        time.sleep(0.5)
    print()

def list_products_once(dictionary,personalstring):
    loading(0.5)
    text_loading(personalstring+"\n")
    print()
    for key, value in dictionary.items():
      loading(0.5)
      text_loading("{key}, a {tpe}\n".format(key=key.name, tpe=key.tpe, value=value)) 
    print()

def display_friendship_level(friendship_points, user):
    bar_length = 20
    filled_length = int((friendship_points / 100)% 1 * bar_length)
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    if friendship_points >= 100:
        x = (friendship_points%100) 
        if friendship_points == 100:
           user.pet.friendship_level += 1
           friendship_points = 0
           filled_length = 0
        else:
           user.pet.friendship_level += 1
           friendship_points = 0
           friendship_points += x
           filled_length = 0
    new_filled_length = int((friendship_points / 100) % 1 * bar_length)
    bar = '#' * new_filled_length + '-' * (bar_length - new_filled_length)     
    x = f"How far to next level: [{bar}]"
    return x

def display_location(player_location):
    text_loading(locations_art.get(player_location, "Unknown location, try again"), delay = 0.03)
    print("\n\n")             
    loading(1)

def where_to_go(player_location):
    text_loading(f"You are currently at {player_location}, where do you want to go next?")
    for x in list_of_locations:
        if x == player_location:
            continue
        text_loading(x)
        loading(1)
  
    while True:
        next_location = input("Enter your destination: ").title()
        if next_location in list_of_locations:
            text_loading(f"You are heading to {next_location}!")
            player_location = next_location
            return player_location
        else:
            text_loading("Invalid location. Please try again.")
            loading(1)

def change_location():
    global player_location
    print()
    player_location = where_to_go(player_location)
    display_location()
    print()
    text_loading(f"You have arrived at {player_location}.\n\n")
    loading(1)
    print()

def generate_question():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        answer = num1 // num2
        num1 = answer * num2  
    return f"What is {num1} {operator} {num2}?", answer

# classes
class Player:
  def __init__(self,name,pet,money = 100):
    self.name = name
    self.money = money
    self.pet = pet
    self.food_items = []
    self.petcessories = []
    self.potions = []
    self.toys = []

  def __repr__(self):
    if self.money == 1:
      y = "\nYour name is {name} and you have {money} dabloon at present.\n\n".format(money = self.money, name = self.name)
      return(f"{y}"+ repr(self.pet))
    else:
      y = "\nYour name is {name} and you have {money} dabloons at present.\n\n".format(money = self.money, name = self.name)
      return (f"{y}"+ f"{self.pet}")    
  def list_inventory(self):
    delimiter = "\n"
    text_loading("You have these food items:")
    food_str = delimiter.join([f"{name}, {tpe}" for name, tpe in self.food_items])
    text_loading(food_str)
    print()
    text_loading("You have these toys:")
    toy_str = delimiter.join([f"{name}, {tpe}" for name, tpe in self.toys])
    text_loading(toy_str)
    print()
    text_loading("You have these petcessories:")
    petcessories_str = delimiter.join([f"{name}, {tpe}" for name, tpe in self.petcessories])
    text_loading(petcessories_str)
    print()
    text_loading("You have these potions:")
    potions_str = delimiter.join([f"{name}, {tpe}" for name, tpe in self.potions])
    text_loading(potions_str)

class Shop:
    def __init__(self, name, shop_owner, shop_type, personal_string):
        self.name = name
        self.shop_owner = shop_owner
        self.shop_type = shop_type
        self.personal_string = personal_string
        self.products_sold = {}

    def __repr__(self):
        s = f"\033[3mWelcome to {self.name}, I am {self.shop_owner}! We sell {self.personal_string} {self.shop_type}.\033[0m"
        return s
    
    def add_products_once(self, products_dict):
       self.products_sold.update(products_dict)
       return self.products_sold

    def add_products(self, products_dict):
        self.products_sold.update(products_dict)
        return self.products_sold

    def remove_products(self, product_key):
        self.products_sold.pop(product_key)
        if self.name == "Pretty Pets":
           del toys_dict[product_key]
        if self.name == "Grape Goods":
           del food_dict[product_key]
        if self.name == "Awful Attire":
           del clothes_dict[product_key]
        if self.name == "Toadstool Tavern":
           del potions_dict[product_key]

    def list_products_for_user(self):
        loading(0.5)
        gap = ""
        print()
        counter = 1
        for (name,tpe), value in self.products_sold.items():
           text_loading(f"{counter}. {name}, {tpe}, for {value} dabloons\n")
           counter += 1
        return gap
    
    def at_shop(self,user):
       text_loading(f"{self}")
       action_finished = False
       while True:
        global player_location
        if not self.products_sold:
           text_loading("THIS SHOP HAS SOLD OUT OF PRODUCTS")
           action_finished = True
           break
        else:
         text_loading(f"\n\nYou currently have {user.money} dabloons\n\nWhat would you like to do?\n\n1. Buy products\n2. Check inventory\n3. Leave shop\nEnter an option between 1-3:")
         action_finished = False
         z = input("\n\n(⌒▽⌒)☞ ")
         if z == "1":
            text_loading("\nCurrently we have these amazing products:")
            self.list_products_for_user()
            valid_input = False
            while True:
               text_loading("\nSo would you like to buy a product or nah? Enter yes or no here:")
               check = input("\n\n(⌒▽⌒)☞ ")
               if check.lower() == "yes":
                  valid_input = True
                  valid3 = False
                  while True:
                     chosen_product = input("Please enter the number of the product you would like, e.g. 1:\n\n(⌒▽⌒)☞ ")
                     try:
                        chosen_integer = int(chosen_product)
                        if chosen_integer in range(1,(len(self.products_sold)+1)):
                           valid_input = True
                           text_loading(f"\nYou have chosen {chosen_integer}\n\n")
                           if self.name == "Pretty Pets":
                              product_name = list(toys_dict.keys())[chosen_integer-1]
                              product_price = toys_dict[product_name]
                           elif self.name == "Grape Goods":
                              product_name = list(food_dict.keys())[chosen_integer-1]
                              product_price = food_dict[product_name]
                           elif self.name == "Awful Attire":
                              product_name = list(clothes_dict.keys())[chosen_integer-1]
                              product_price = clothes_dict[product_name]
                           elif self.name == "Toadstool Tavern":
                              product_name = list(potions_dict.keys())[chosen_integer-1]
                              product_price = potions_dict[product_name]
                           if user.money >= product_price:
                              user.money -= product_price
                              if self.name == "Pretty Pets":
                                 pet_shop.remove_products(list(toys_dict.keys())[chosen_integer-1])
                                 user.toys.append(product_name)
                              elif self.name == "Grape Goods":
                                 food_shop.remove_products(list(food_dict.keys())[chosen_integer-1])
                                 user.food_items.append(product_name)
                              elif self.name == "Awful Attire":
                                 clothes_shop.remove_products(list(clothes_dict.keys())[chosen_integer-1])
                                 user.petcessories.append(product_name)
                              elif self.name == "Toadstool Tavern":
                                 pub_shop.remove_products(list(potions_dict.keys())[chosen_integer-1])
                                 user.potions.append(product_name)
                              chosen_integer-=1
                              text_loading("Purchase successful, product added to inventory!")
                              valid3 = True
                              break
                           else:
                              text_loading("You don't have enough dabloons, sorry!\n\n") 
                              valid3 = True
                           valid3 = True
                           break
                        else:
                           text_loading("\nPlease enter a valid option\n")
                           valid3 = False
                     except ValueError:
                        text_loading("\nPlease enter a valid option\n")   
                  if valid3:
                     break
               elif check.lower() == "no":
                  text_loading("No problem\n\n")
                  valid_input = True
                  break
               else: 
                  text_loading("\nPlease enter a valid option\n")
            if not valid_input:
               text_loading("Error: invalid input")
            # if action_finished == True:
            #    break
         elif z == "2":
            user.list_inventory()
         elif z == "3":
            text_loading("No problem, bye!\n\n")
            action_finished = True
            break
         else:
           text_loading("\nPlease enter a valid option\n")
         if action_finished:
            break
        if action_finished == True:
           break

class Pet:
  def __init__(self,name,tpe,age,energy=15,is_friendly=True,friendship_level=0, friendship_points = 0):
    self.name = name
    self.age = age
    self.tpe = tpe
    self.energy = energy
    self.is_friendly = is_friendly
    self.is_happy = True
    self.tired = False
    self.friendship_level = friendship_level
    self.friendship_points = friendship_points
    
  def __repr__(self):
    x = "Their loveliest trait is that they are a {tpe}!".format(tpe = self.tpe)
    if self.is_friendly:
      friendly_msg = "They are charismatic and sociable."
    else:
      friendly_msg = "They are introverted and picky about who they like. Take that as a compliment :)"
    
    if self.is_happy:
      happy_msg = "{} is currently happy! Keep doing what you're doing to increase your friendship level from {} to {}.".format(self.name, self.friendship_level, self.friendship_level + 1)
    elif self.tired:
      happy_msg = "{} is tired. Feed them to increase their energy.".format(self.name)
    else:
      happy_msg = ""

    c = "Your cow is called {name} and is {age} years old. {x} {friendly} {happy}\n\n{name} currently has {energy} energy points. Your friendship level with {name} is {friend}!\n".format(
      name=self.name, age=self.age, friend=self.friendship_level, energy=self.energy,
        friendly=friendly_msg, happy=happy_msg,x=x)
    d = display_friendship_level(self.friendship_points, user)
    return f"{c}{d}\n"
    

  def feed(self, chosen_food):
     if not chosen_food:
        text_loading("You have no food items to feed your pet. Please buy some food first.")
     else:
        self.energy += 20
        self.friendship_points += 20
        text_loading(f"You fed {self.name}! Their energy is now {self.energy} points and your friendship has gotten stronger!\n\n")
        text_loading(display_friendship_level(self.friendship_points, user))
        if self.energy < 5:
           text_loading(f"Uh oh, {self.name}'s energy is low. Feed them some more")
        else:
           pass
        
  def play(self, chosen_toy):
     if not chosen_toy:
        text_loading("You have no toys for your pet to play with. Please buy some toys first.")
     else:
        self.energy -= 5
        self.friendship_points += 30
        text_loading(f"You played with {self.name}! Their energy is now {self.energy} points and your friendship has gotten stronger!\n\n")
        text_loading(display_friendship_level(self.friendship_points, user))
        if self.energy < 5:
           text_loading(f"Uh oh, {self.name}'s energy is low. Feed them some food")
        else:
           pass

  def change(self, chosen_petcessory):
     if not chosen_petcessory:
        text_loading("You have no petcessories for your pet to wear. Please buy some petcessories first.")
     else:
        self.energy -= 5
        self.friendship_points += 30
        text_loading(f"You put a petcessory on {self.name}! Their energy is now {self.energy} points and your friendship has gotten stronger!\n\n")
        text_loading(display_friendship_level(self.friendship_points, user))
        if self.energy < 5:
           text_loading(f"Uh oh, {self.name}'s energy is low. Feed them some food")
        else:
           pass
        
  def potion(self, chosen_potion, user):
     if not chosen_potion:
        text_loading("You have no potions to give to your pet. Please buy some potions first.")
     else:
        if chosen_potion[0] == "Energy Maximus":
           self.energy += 100
           text_loading(f"You fed {self.name} with {chosen_potion[0]}! Their energy is now {self.energy} points and your friendship has gotten stronger!\n\n")
           self.friendship_points += 40
           text_loading(display_friendship_level(self.friendship_points, user))
        elif chosen_potion[0] == "Friendlymaker":
           self.energy -= 5
           self.is_friendly = True
           text_loading(f"You fed {self.name} with {chosen_potion[0]}! They are now friendly, and your friendship has gotten stronger!\n\n")
           self.friendship_points += 40
           text_loading(display_friendship_level(self.friendship_points, user))
        elif chosen_potion[0] == "Add a Couple Years":
           self.energy -= 5
           self.age += 30
           text_loading(f"You fed {self.name} with {chosen_potion[0]}! Their age is now {self.age} and your friendship has gotten stronger!\n\n")
           self.friendship_points += 40
           text_loading(display_friendship_level(self.friendship_points, user))
        elif chosen_potion[0] == "Happy Calf":
           self.energy -= 5
           self.is_happy = True
           text_loading(f"You fed {self.name} with {chosen_potion[0]}! They are now happy, and your friendship has gotten stronger!\n\n")
           self.friendship_points += 40
           text_loading(display_friendship_level(self.friendship_points, user))
        elif chosen_potion[0] == "Friendship Upgrade":
           self.energy -= 5
           if self.friendship_points == 0:
              self.friendship_points += 100
              text_loading(display_friendship_level(self.friendship_points, user))
              self.friendship_points = 0
           if self.friendship_points > 0:
              self.friendship_points += 100
              text_loading(display_friendship_level(self.friendship_points, user))
           text_loading(f"You fed {self.name} with {chosen_potion[0]}! Their friendship with you has gone up a level!\n\n")
        elif chosen_potion[0] == "Instant Dabloons":
           self.energy -= 5
           user.money += 100
           text_loading(f"You fed {self.name} with {chosen_potion[0]}! You now have {user.money} dabloons and your friendship with {self.name} has gotten stronger!\n\n")
           self.friendship_points += 40
           text_loading(display_friendship_level(self.friendship_points, user))
        if self.energy < 5:
           text_loading(f"Uh oh, {self.name}'s energy is low. Feed them some food")
        else:
           pass

class Product:
  def __init__(self, name, tpe):
    self.name = name
    self.tpe = tpe 
  def __repr__(self):
    return f"{self.name}, {self.tpe}"
  
# shop instances
pet_shop = Shop("Pretty Pets", "Petunia","pets and pet toys", "the peachiest")
food_shop = Shop("Grape Goods", "Greg", "groceries", "a delicious variety of")
clothes_shop = Shop("Awful Attire", "Ambrosia", "clothes", "atrocious but artistic")
flower_shop = Shop("Faerie Florist", "Frangipane", "flowers", "the rarest")
pub_shop = Shop("Toadstool Tavern", "Topper", "alcoholic beverages", "the finest")

# product instances
Cornbread = Product("Cornbread", "a bread dish")
Hay = Product("Hay", "a type of crop")
Biscuits  = Product("Biscuits", "a snack")
Tomatoes = Product("Tomatoes", "a fruit")
Pecans = Product("Pecans", "a nut")
Peaches = Product("Peaches", "a dessert")

Collar = Product("Cowbell Collar","a decorative petcessory")
Headband = Product("Horned Headband","a decorative petcessory")
Covers = Product("Udder Covers","a decorative petcessory")
Bandana = Product("Cow-print Bandana","a decorative petcessory")
Ribbon = Product("Tail Ribbon","a decorative petcessory")
Hoofrings = Product("Vogue Cow-Hoofrings","a decorative petcessory")

Maximus = Product("Energy Maximus","a potion to increase your cow's energy")
Friendlymaker = Product("Friendlymaker","a potion to make your cow friendly")
Addyears = Product("Add a Couple Years","a potion to age your cow")
Happycalf = Product("Happy Calf","a potion to make your cow happy")
Upgrade = Product("Friendship Upgrade","a potion to increase your friendship level with your cow")
Instantmoney = Product("Instant Dabloons","a potion to give you double what you spent buying it")

# pet instances
Gulliver = Pet('Gulliver','bouncy cow' ,3, energy=20, is_friendly=True)
Caroline = Pet('Caroline','quiet cow', 7, energy=10 ,is_friendly=False)
Chase = Pet('Chase','quirky cow', 5, is_friendly=False)
Cuddly = Pet('Cuddly','bright cow', 10, energy=10)
Bo = Pet('Bo','sweet cow', 2, energy=20)
Pooh = Pet('Pooh','silly cow', 4, is_friendly=False)

# dictionaries and products_sold lists for every shop
pets_dict = {Gulliver:0,Caroline:0,Chase:0,Cuddly:0,Bo:0,Pooh:0}
pets_sold = pet_shop.add_products_once(pets_dict)

food_dict = {(Cornbread.name, Cornbread.tpe):15, (Hay.name, Hay.tpe):15, (Biscuits.name, Biscuits.tpe):15, (Tomatoes.name, Tomatoes.tpe):15, (Pecans.name, Pecans.tpe):15, (Peaches.name, Peaches.tpe):15}
food_sold = food_shop.add_products(food_dict)

clothes_dict = {(Collar.name, Collar.tpe):25, (Headband.name, Headband.tpe):25, (Covers.name, Covers.tpe):25, (Bandana.name, Bandana.tpe):25, (Ribbon.name, Ribbon.tpe):25,(Hoofrings.name, Hoofrings.tpe):25}
clothes_sold = clothes_shop.add_products(clothes_dict)

potions_dict = {(Maximus.name, Maximus.tpe):30, (Friendlymaker.name, Friendlymaker.tpe):30, (Addyears.name, Addyears.tpe):30, (Happycalf.name, Happycalf.tpe):30, (Upgrade.name, Upgrade.tpe):50, (Instantmoney.name, Instantmoney.tpe):50}
potions_sold = pub_shop.add_products(potions_dict)

# pet functions
def feed_pet():
    global player_location
    finished = False
    while True:
      if user.food_items:
        text_loading("What would you like to feed your pet?")
        for index, food in enumerate(user.food_items):
            text_loading(f"{index+1}. {food[0]}, {food[1]}")
        while True:
            try:
                choice = int(input("Enter a number: "))
                if choice < 1 or choice > len(user.food_items):
                    text_loading("\nPlease enter a number from the list above.\n")
                else:
                    chosen_food = user.food_items[choice-1]
                    user.pet.feed(chosen_food)
                    user.food_items.remove(chosen_food)
                    finished = True
                    break
            except ValueError:
                text_loading("\nPlease enter a number from the list above.\n")
                continue
            if finished:
               break
      else:
        while True:
            text_loading(f"You have no food to feed {pet_choice}! Would you like to go to Grape Goods?")
            get_food = input("\n\n(⌒▽⌒)☞ ")
            if get_food.lower() == "yes":
                player_location = "Grape Goods"
                text_loading("\nYou are heading to Grape Goods!")
                display_location(player_location)
                text_loading(f"You have arrived at {player_location}.\n\n")
                food_shop.at_shop(user)
                finished = False
            elif get_food.lower() == "no":
                text_loading("No problem\n\n")
                finished = False
            else:
                text_loading("\nPlease enter yes or no!\n")
                finished = True
            if not finished:
               break
      if finished:
         break
      if not finished:
         break

def play_pet():
    global player_location
    finished = False
    while True:
      if user.toys:
         text_loading(f"Which toy would you like {pet_choice} to play with?")
         for index, toy in enumerate(user.toys):
            text_loading(f"{index+1}. {toy[0]}, {toy[1]}")
         while True:
            try:
                choice = int(input("Enter a number: "))
                if choice < 1 or choice > len(user.toys):
                    text_loading("\nPlease enter a number from the list above.\n")
                else:
                    chosen_toy = user.toys[choice-1]
                    user.pet.play(chosen_toy)
                    user.toys.remove(chosen_toy)
                    finished = True
                    break
            except ValueError:
                text_loading("\nPlease enter a number from the list above.\n")
                continue
            if finished: 
               break
      else:
         while True:
            get_toys = input(f"You have no toys for {pet_choice} to play with! Would you like to go to Pretty Pets?\n\n(⌒▽⌒)☞ ")
            if get_toys.lower() == "yes":
                player_location = "Pretty Pets"
                text_loading("You are heading to Pretty Pets!")
                display_location(player_location)
                text_loading(f"You have arrived at {player_location}.\n\n")
                pet_shop.at_shop(user)
                finished = False
                break
            elif get_toys.lower() == "no":
                text_loading("No problem\n\n")
                finished = False
            else:
                text_loading("\nPlease enter yes or no!\n")
                finished = True
            if not finished:
               break
      if finished:
          break
      if not finished:
          break

def change_pet():
   global player_location
   finished = False
   while True:
      if user.petcessories:
         text_loading(f"Which petcessory would you like {pet_choice} to put on?")
         for index, petcessory in enumerate(user.petcessories):
            text_loading(f"{index+1}. {petcessory[0]}, {petcessory[1]}")
         while True:
            try:
               choice = int(input("Enter a number: "))
               if choice < 1 or choice > len(user.petcessories):
                  text_loading("\nPlease enter a number from the list above.\n")
               else:
                  chosen_petcessory = user.petcessories[choice-1]
                  user.pet.change(chosen_petcessory)
                  user.petcessories.remove(chosen_petcessory)
                  finished = True
                  break
            except ValueError:
               text_loading("\nPlease enter a number from the list above.\n")
               continue
            if finished:
               break
      else:
         while True:
            get_petcessories = input("You have no petcessories for {pet} to put on! Would you like to go to Awful Attire?\n\n(⌒▽⌒)☞ ".format(pet = pet_choice))
            if get_petcessories.lower() == "yes":
               player_location = "Awful Attire"
               text_loading("You are heading to Awful Attire!")
               display_location(player_location)
               text_loading(f"You have arrived at {player_location}.\n\n")
               clothes_shop.at_shop(user)
               finished = False
               break
            elif get_petcessories.lower() == "no":
               text_loading("No problem\n\n")
               finished = False
            else:
               text_loading("\nPlease enter yes or no!\n")
               finished = True
            if not finished:
               break
      if finished:
         break
      if not finished:
         break

def potion_pet():
   global player_location
   finished = False
   while True:
      if user.potions:
         text_loading(f"Which potion would you like to give to {pet_choice}?")
         for index, potion in enumerate(user.potions):
            text_loading(f"{index+1}. {potion[0]}, {potion[1]}")
         while True:
            try:
               choice = int(input("Enter a number: "))
               if choice < 1 or choice > len(user.potions):
                  text_loading("\nPlease enter a number from the list above.\n")
               else:
                  chosen_potion = user.potions[choice-1]
                  user.pet.potion(chosen_potion, user)
                  user.potions.remove(chosen_potion)
                  finished = True
                  break
            except ValueError:
               text_loading("\nPlease enter a number from the list above.\n")
               continue
            if finished:
               break
      else:
         while True:
            get_potions = input("You have no potions to give to {pet}! Would you like to go to Toadstool Tavern?\n\n(⌒▽⌒)☞ ".format(pet = pet_choice))
            if get_potions.lower() == "yes":
               player_location = "Toadstool Tavern"
               text_loading("You are heading to Toadstool Tavern!")
               display_location(player_location)
               text_loading(f"You have arrived at {player_location}.\n\n")
               pub_shop.at_shop(user)
               finished = False
               break
            elif get_potions.lower() == "no":
               text_loading("No problem\n\n")
               finished = False
            else:
               text_loading("\nPlease enter yes or no!\n")
               finished = True
            if not finished:
               break
      if finished:
         break
      if not finished:
         break

def work():
    text_loading("Here are the latest stock calculations that need solving!\n\n")
    num_correct = 0
    while num_correct < 5:
        question, answer = generate_question()
        text_loading(question)
        user_answer = input("Enter your answer: ")
        try:
            user_answer = int(user_answer)
            if user_answer == answer:
                num_correct += 1
                text_loading("Correct!")
            else:
                text_loading("Incorrect, try again.")
        except ValueError:
            text_loading("Invalid input, try again.")
    user.money += 25
    text_loading(f"Thank you for your hard work. We have added 15 dabloons to your account. You now have {user.money} dabloons.")

# formatting references
border1 = ". . • ☆ . ° .• °:. *₊ ° . ☆. . • ☆ . ° .• °:. *₊ ° . ☆. . • ☆ . ° .• °:. *₊ ° . ☆. . • ☆ . ° .• °:. *₊ "
border2 = "⋆⋅☆⋅⋆ ─────────────────────────────────────────  ⋆⋅☆⋅⋆  ───────────────────────────────────────── ⋆⋅☆⋅⋆"
border3 = "❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀•°❀°•❀"
border4 = "(._.) ( l: ) ( .-. ) ( :l ) (._.) ( l: ) ( .-. ) ( :l ) (._.) ( l: ) ( .-. ) ( :l ) (._.) ( l: ) ( .-. )"

# ¯\_(ツ)_/¯ (づ｡◕‿‿◕｡)づ (づ￣ ³￣)づ 
# (◕‿◕✿) (☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜) ♪~ ᕕ(ᐛ)ᕗ     
# ༼ つ ಥ‿‿ಥ ༽つ ~(˘▾˘~) (~˘▾˘)~ \ (•◡•) /
# (._.) ( l: ) ( .-. ) ( :l ) (._.)
# ᕦ(ò_óˇ)ᕤ ᕙ(⇀‸↼‶)ᕗ (✿´‿`)
# ("\n｡･:*˚:✧｡ xxx ｡✧:˚*:･｡")
# animation()


# script before game loop
pygame.mixer.music.load(r'intro.mp3')
pygame.mixer.music.play()

loading(3.5)

text_loading("\n\033[3m｡･:*˚:✧｡ Welcome to Snuggle Pasture (◕‿◕✿) Please tell us your name, and make sure to hit enter ｡✧:˚*:･｡\033[0m")

p_name = input("\n\n(⌒▽⌒)☞ ")
print()

player_name = check_name(p_name.title())

text_loading(f"Well, howdy there {player_name}! You're about to embark on a wholesome adventure (✿´‿`)\n")

text_loading("\n" + border2 + "\n\n")

loading(0.5)

frames = [
r"""
___________________________________/   ,   /________
                                            
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    
 ___________________        __________________________
                   /   ,   / """,

r"""
___________________________________/   ,   /_ .--⹁ _
                                            '0---0'~
 _ _  ,--.  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    ~'O---O'
 ___________________        __________________________
                   /   ,   / """,

r"""
____________________________  .--⹁ /   ,   /________
                            '0---0'~
 _ _ _ _ _ _  ,--.  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
            ~'O---O'
 ___________________        __________________________
                   /   ,   / """,
                            
r"""
_________________  .--⹁  __________/   ,   /________
                 'O---O'~ 
 _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _ _ _ _ _ _ _ _
                       ~'O---O'
 ___________________        __________________________ 
                   /   ,   / """,

r"""
________  .--⹁  ___________________/   ,   /________
        '0---0'~
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _ _ _ 
                                 ~'O---O'
 ___________________        __________________________
                   /   ,   / """,

r"""
.--⹁  _____________________________/   ,   /________
---O'~
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.  
                                                 ~'O---
 ___________________        __________________________ 
                   /   ,   / """,

r"""
-⹁  _______________________________/   ,   /________
-O'~
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ,-  
                                                   ~'O-
 ___________________        __________________________ 
                   /   ,   / """

]

num_repeats = 3

for i in range(num_repeats):
    for idx, frame in enumerate(frames):
        if i == 0 and idx == 0:
            print(frame, end="\r")
        else:
            print("\n" * 50)
            os.system('cls' if os.name == 'nt' else 'clear') 
            print(frame, end="\r")
        loading(0.2)

print("\n\n")

text_loading("You've come a long way from the city with all them boxes in your car.\nLooks like you're ready to start a new life out here in the countryside ᕦ(ò_óˇ)ᕤ\n\nIt's a cozy spot, with friendly folks, rolling fields, and all kinds of critters roaming around ~(˘▾˘~)\n\nSo, tell us now, friend - what's the name of this here place you've hitched your wagon to?")

t_name = input("\n\n(⌒▽⌒)☞ ")
print()

town_name = check_name(t_name.title())

text_loading(f"{town_name} is just about as pretty as a fresh-picked bouquet of wildflowers in the morning dew!\n\n\n")

text_loading(border3 + "\n")

print()
text_loading('''  
      __________ ,%%&%,
     /\     _   \%&&%%&%
    /  \___/^\___\%&%%&&
    |  | []   [] |%\Y&%\'
    |  |   .-.   | ||  
  ~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
       `""") )"""` ''')
print()

loading(1)

text_loading("\n\nYou sure did snag yourself a mighty fine deal on this here house in the country, but it's a bit more spacious than you bargained for, ain't it?.\n\nAs you sit there ponderin' whether you need yourself a roommate to help fill up all that space, you hear a knockin' on your front door.\n\nWho could that be, you wonder? Only one way to find out, I reckon.\n\n")

loading(1)
text_loading("♪~ ᕕ(ᐛ)ᕗ\n\n")
loading(1)

text_loading(f"\033[3m{player_name}, this here's Petunia, owner of Pretty Pets - the only darn tootin' animal distributor still standin'\033[0m \ (•◡•) / \n\n\033[3mNow listen up, 'cause I've got some mighty important news for ya.")
loading(1)
text_loading(f"'Round these parts, it's a long-held tradition to welcome new folks with a cute cow to call their own - don't ask why \033[0m(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)\033[3m\n\nSo let's take you on down to my shop and help you pick out the perfect companion for your new life in {town_name}\033[0m!\n")

loading(1)
text_loading("\n\nBefore you can say anything, Petunia guesses what's on your mind ¯\_(ツ)_/¯ \n\n\n")
loading(1)

text_loading("\033[3mI know what you're thinkin' - you just moved out to the countryside, and money might be a little tight." + "\nBut don't you worry none, 'cause we're givin' this here pet to you as a gift." + "\n\nAnd as for the other costs, well, let's just say our prices are a mite more reasonable than them big-city pet stores." + f"\n\nSo what do ya say, {player_name}? You gonna turn down our generous offer of a new furry friend?\033[0m\n\n")

loading(1)

text_loading("\nWell, I reckon you don't really have much of a choice in the matter - you're goin' to Pretty Pets with Petunia, and that's that!\n\n\n")

loading(1)

text_loading(f"\033[3mLet's go! The pets are just itchin' to meet the newest member of {town_name}'s community.\033[0m\n\n\n")

text_loading(border1 + "\n\n\n")

text_loading("As you walk to the shop, you'll see all sorts of sights along the way. And when you arrive, you'll be greeted by a whole slew of critters just beggin' for a new home.\n\n")

loading(1.5)

text_loading("""
                            +&-
                          _.-^-._    .--.
                       .-'   _   '-. |__|
                      /     |_|     \|  |
                     /               \  |
                    /|     _____     |\ |
                     |    |==|==|    |  |
 |---|---|---|---|---|    |--|--|    |  |
 |---|---|---|---|---|    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""", delay = 0.01)
      
loading(1.5)

text_loading("\n\n\033[3mNow, let's take a look at what we've got here!\033[0m\n\n")

list_products_once(pets_sold, "Currently we have these amazing animals waiting for forever homes:")

loading(1.5)

text_loading(f"\033[3mWhich cow will it be {player_name}?\n\nTake your time, and choose wisely. This here's a big decision, and it's one you'll have to stick with for the rest of your time in our little town.\n\nWhen you find the one for you, you'll know it in your heart.\033[0m")

p_choice = input("\n\n(⌒▽⌒)☞ ")

pet_choice = p_choice.title()

while pet_choice not in ['Gulliver', 'Caroline', 'Chase', 'Cuddly', 'Bo', 'Pooh']:
    text_loading("\nY'all chose a frickin' imaginary pet! C'mon and enter a name from our list.")
    p_choice = input("\n\n(⌒▽⌒)☞ ")
    pet_choice = p_choice.title()

if pet_choice == 'Gulliver':
  user = Player(player_name, Gulliver)
elif pet_choice == 'Caroline':
  user = Player(player_name, Caroline)
elif pet_choice == 'Chase':
  user = Player(player_name, Chase)
elif pet_choice == 'Cuddly':
  user = Player(player_name, Cuddly)
elif pet_choice == 'Bo':
  user = Player(player_name, Bo)
elif pet_choice == 'Pooh':
  user = Player(player_name, Pooh)

pygame.mixer.music.load(r'celebration.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    loading(1)

loading(1)
text_loading("\nNew player created:\n")
loading(1)

text_loading(f"{user}\n\n")

text_loading("Petunia beams with joy! つ ಥ‿‿ಥ ༽つ\n\n")

text_loading(f"\033[3mI hope you liked our welcome! Let's get you and {pet_choice} back to your home.\033[0m\n\n")

text_loading("\n" + border4 + "\n\n")

loading(2)
text_loading(f"\nWell shucks, you sure had yourself quite the first day here on the farm, {player_name}!\n\nBut now, let me tell ya 'bout what you gotta do next. The goal is to build up a mighty friendship level of 5 with {pet_choice}.\n\nYou can get all sorts of fancy toys over at Pretty Pets, some darn fine clothes at Awful Attire, or rare potions over at Toadstool Tavern. And don't you forget to give {pet_choice} some grub from Grape Goods!\n\nNow, how you plannin' on payin' for all that, you ask? By workin' as Faerie Florist's accountant, of course! You already got yourself 100 dabloons, so you're in good shape for a spell.\n\n\033[3m｡･:*˚:✧｡ But the path you choose from here on out is all up to you ｡✧:˚*:･｡\033[0m")

# reassigning pet shop products - from cows (pet instances) to toys (product instances)
pet_shop.products_sold = {}
Moosical = Product("Moo-sical Hoof","a pet toy")
Cowbell = Product("Cowbell","a pet toy")
Yoyo = Product("Yo-Yo","a pet toy")
Teddy = Product("Teddy Calf","a pet toy")
Ball = Product("Moo-print Ball","a pet toy")
Teeth = Product("Teeth Strengthener","a pet toy")
toys_dict = {(Moosical.name, Moosical.tpe):20, (Cowbell.name, Cowbell.tpe):20, (Yoyo.name, Yoyo.tpe):20, (Teddy.name, Teddy.tpe):20, (Ball.name, Ball.tpe):20, (Teeth.name, Teeth.tpe):20}
toys_sold = pet_shop.add_products(toys_dict)

# game loop
done = False
while not done:
  while user.pet.friendship_level < 5:
    while True:
      if user.pet.friendship_level >= 5:
       break
      text_loading("\n\nWhat do you want to do now, {name}?\n".format(name=player_name))
      menu = "\n1. Go home\n2. Feed {pet}\n3. Play with {pet}\n4. Change {pet}'s accessories\n5. Give {pet} a potion\n6. Go to a shop\n7. Go to work\n8. See current player stats\n9. See pet stats\n10. Quit game (progress will not be saved)".format(pet=pet_choice)
      for line in menu.split('\n'):
         text_loading(line)
         print()
      user_input = input("\nEnter an option between 1-10:\n\n(⌒▽⌒)☞ ")
      option = user_input.split()[0]
      if option == "1":
          if player_location == "Home":
            text_loading("\nYou're already at home!")
            break
          else:
             player_location = "Home"
             text_loading("You are heading to Home!\n\n")
             display_location(player_location)
             text_loading(f"You have arrived at {player_location}.\n\n")
             break
      elif option == "2":
          while True:
            text_loading(f"\n\nDo you want to feed {pet_choice}?\n\nPlease enter yes, no, or 'go home' to return to main menu:")
            y = input("\n\n(⌒▽⌒)☞ ")
            if y.lower() == "yes":
              print()
              feed_pet()
            elif y.lower() == "no":
              print()
              text_loading("No problem\n\n")
              break
            elif y.lower() == "go home" or y == "1":
               break  
            else:
               text_loading("Invalid input, try again\n")  
      elif option == "3":
         while True:
            text_loading(f"\n\nDo you want to play with {pet_choice}?\n\nPlease enter yes, no, or 'go home' to return to main menu:")
            y = input("\n\n(⌒▽⌒)☞ ")
            if y.lower() == "yes":
              play_pet()
            elif y.lower() == "no":
              text_loading("No problem\n\n")
              break
            elif y.lower() == "go home" or y == "1":
               break  
            else:
               text_loading("Invalid input, try again\n")   
      elif option == "4":
         while True:
            text_loading(f"\n\nDo you want {pet_choice} to put on or change petcessories?\n\nPlease enter yes, no, or 'go home' to return to main menu:")
            y = input("Enter an option:\n\n(⌒▽⌒)☞ ")
            if y.lower() == "yes":
              change_pet()
            elif y.lower() == "no":
              text_loading("No problem\n\n")
              break
            elif y.lower() == "go home" or y == "1":
               break  
            else:
               text_loading("Invalid input, try again\n") 
      elif option == "5":
         # break
         while True:
            text_loading(f"\n\nDo you want to give {pet_choice} a potion? The effects cannot be reversed.\n\nPlease enter yes, no, or 'go home' to return to main menu:")
            y = input("Enter an option:\n\n(⌒▽⌒)☞ ")
            if y.lower() == "yes":
              potion_pet()
            elif y.lower() == "no":
              text_loading("No problem\n\n")
              break
            elif y.lower() == "go home" or y == "1":
               break  
            else:
               text_loading("Invalid input, try again\n") 
      elif option == "6":
         valid2 = False
         while True:
            shop_menu = f"\nWhere do you want to go?\n\n1. Pretty Pets\n2. Grape Goods\n3. Awful Attire\n4. Toadstool Tavern"
            for line in shop_menu.split('\n'):
               text_loading(line)
               loading(0.5)
            shop_input = input("Enter an option between 1-4:\n\n(⌒▽⌒)☞ ")
            shop_option = shop_input.split()[0]
            if shop_option == "1":
               if not toys_dict:
                  text_loading("THIS SHOP HAS SOLD OUT OF PRODUCTS")
                  valid2 = True
                  break
               else:
                  player_location = "Pretty Pets"
                  text_loading("You are heading to Pretty Pets!")
                  display_location(player_location)
                  text_loading(f"You have arrived at {player_location}.\n\n")
                  pet_shop.at_shop(user)
                  valid2 = True
                  break
            elif shop_option == "2":
               if not food_dict:
                  text_loading("THIS SHOP HAS SOLD OUT OF PRODUCTS")
                  valid2 = True
                  break
               else:
                  player_location = "Grape Goods"
                  text_loading("You are heading to Grape Goods!")
                  display_location(player_location)
                  text_loading(f"You have arrived at {player_location}.\n\n")
                  food_shop.at_shop(user)
                  valid2 = True
                  break
            elif shop_option == "3":
               if not clothes_dict:
                  text_loading("THIS SHOP HAS SOLD OUT OF PRODUCTS")
                  valid2 = True
                  break
               else:
                  player_location = "Awful Attire"
                  text_loading("You are heading to Awful Attire!")
                  display_location(player_location)
                  text_loading(f"You have arrived at {player_location}.\n\n")
                  clothes_shop.at_shop(user)
                  valid2 = True
                  break
            elif shop_option == "4":
               if not potions_dict:
                  text_loading("THIS SHOP HAS SOLD OUT OF PRODUCTS")
                  valid2 = True
                  break
               else:
                  player_location = "Toadstool Tavern"
                  text_loading("You are heading to Toadstool Tavern!")
                  display_location(player_location)
                  text_loading(f"You have arrived at {player_location}.\n\n")
                  pub_shop.at_shop(user)
                  valid2 = True
                  break
            else:
               text_loading("\nPlease enter a valid option.\n")
         if not valid2:
            text_loading("Error: invalid input")
      elif option == "7":
          text_loading(f"\nHi there {player_name}, ready for your shift at Faerie Florist's? We could really use those city smarts with these finances of ours.\n")
          while True:
             choose_work = input("Enter yes, no or go home to return to main menu:\n\n(⌒▽⌒)☞ ")
             if choose_work.lower() == "yes":
                player_location = "Faerie Florist"
                text_loading("You are heading to Faerie Florist!")
                display_location(player_location)
                text_loading("You have arrived at work. Time to grind!\n\n")
                work()
                break
             elif choose_work.lower() == "no":
                text_loading("No problem\n\n")
                break
             elif choose_work.lower() == "go home" or choose_work.lower() == "1":
                break  
             else:
                text_loading("\nPlease enter a valid option.\n") 
      elif option == "8":
          text_loading(user)
      elif option == "9":
         text_loading(user.pet)
      elif option == "10":
         text_loading("Thank you for playing!\n\n")
         done = True
         break
      else:
          text_loading("\nPlease enter a valid option.\n")
    break
  if user.pet.friendship_level >= 5:
     pygame.mixer.music.load(r'end.mp3')
     pygame.mixer.music.play()
     text_loading("\nYou have completed this game, thank you for playing!")
     break
          
sys.exit()