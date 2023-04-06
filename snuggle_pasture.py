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