import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Robot:

  def __init__(self,
               health,
               attackpoints,
               armorpoints,
               target,
               coins,
               name,
               rounds_won,
               power_round=1,
               dodge_change=0,
               dodge_num=0):
    self.health = health
    self.attackpoints = attackpoints
    self.armorpoints = armorpoints
    self.dodge_num = dodge_num
    self.target = target
    self.coins = coins
    self.dodge_change = dodge_change
    self.name = name
    self.power_round = power_round
    self.rounds_won = rounds_won
    self.just_dodged = 0

  def attack(self):
    self.dodge_num = 0
    if self.target.dodge_num == 1:
      print("Your attack was dodged by the enemy.")
      print("You took " + str(self.attackpoints) +
            " damage from hitting the ground.")
      self.health -= self.attackpoints
    else:
      attack_mulitpler = random.randint(1, 4)
      tottle_damage = self.attackpoints - self.target.armorpoints
      damage = ((tottle_damage + 2) * attack_mulitpler) + 5
      damage = min(damage, 50)  # This limits the max damage to 50

      self.target.health -= damage
      print("You have dealt " + str(damage) + " damage to the enemy")

      def attack_feedback(damage):
        if damage <= 10:
          attackfeedback = random.randint(1, 3)
          if attackfeedback == 1:
            print("Your attack was weak.")
          elif attackfeedback == 2:
            print("You almost missed.")
          elif attackfeedback == 3:
            print("You slide during your attack, causing low damage.")
        elif damage >= 11 and damage <= 25:
          attackfeedback = random.randint(1, 3)
          if attackfeedback == 1:
            print("Your attack was decent.")
          elif attackfeedback == 2:
            print("You hit the enemy with good force.")
          elif attackfeedback == 3:
            print(
                "You slide during your attack but managed to still hit decently."
            )
        elif damage >= 26 and damage <= 40:
          attackfeedback = random.randint(1, 3)
          if attackfeedback == 1:
            print("Your attack was amazing.")
          elif attackfeedback == 2:
            print("You hit the enemy right in the head")
          elif attackfeedback == 3:
            print(
                "You got air during your attack and hit the enemy with great force."
            )
        elif damage >= 41:
          attackfeedback = random.randint(1, 3)
          if attackfeedback == 1:
            print("Your attack was perfect.")
          elif attackfeedback == 2:
            print(
                "You hit the enemy right in the head and it was a critical hit."
            )
          elif attackfeedback == 3:
            print("You landed a strong swing attack for great damage")

      attack_feedback(damage)

  def attack_bot(self):
    self.dodge_num = 0
    if self.target.dodge_num == 1:
      self.health -= self.attackpoints
    else:
      attack_mulitpler = random.randint(1, 4)
      tottle_damage = self.attackpoints - self.target.armorpoints
      damage = ((tottle_damage + 2) * attack_mulitpler) + 5
      damage = min(damage, 50)  # This limits the max damage to 50
      self.target.health -= damage

  def dodge(self):
    dodge_change = random.randint(0, 100)
    if dodge_change + self.dodge_change > 25:
      self.dodge_num = 1
      print("If enemy attacks you can dodge.")
    else:
      self.dodge_num = 0
      print("You moved too slow and enemy can attack you.")

  def dodge_bot(self):
    dodge_change = random.randint(0, 100)
    if dodge_change + self.dodge_change > 25:
      self.dodge_num = 1
    else:
      self.dodge_num = 0

  def double(self):
    if self.power_round == 1:
      print("You have charged your double attack!")
      print("This can only be used once per round of battle.")
      choice = input("Are you sure you want to use Double Attack? (Y/N): ")
      choice = choice.upper()
      if choice == "Y":
        time.sleep(3)
        clear()
        print(f"{self.name} used Double Attack!")
        self.attack()
        self.attack()
        time.sleep(6)
        clear()
        self.power_round = 0
      else:
        self.power_round = 1
        time.sleep(1)
        clear()
        self.Turn()
    else:
      print("You have already used Double Attack this round.")
      time.sleep(2)
      clear()
      self.Turn()

  def double_robot(self):
    if self.power_round == 1:
      choice = "Y"
      if choice == "Y":
        time.sleep(3)
        clear()
        self.attack_bot()
        self.attack_bot()
        time.sleep(6)
        clear()
        self.power_round = 0
      else:
        self.power_round = 1
        time.sleep(1)
        clear()
        self.Turn()
    else:
      time.sleep(2)
      clear()
      self.Turn()

  def Turn(self):
    print("\n" + str(self.health) + " Is " + str(self.name) + "\'s health.")
    print("\n" + str(self.attackpoints) + " Is " + str(self.name) +
          "\'s attack points.")
    print("\n" + str(self.armorpoints) + " Is " + str(self.name) +
          "\'s armor points.")
    print("\n" + "What would you like to do?")
    print('''1 - Attack
2 - Dodge
3 - Double Attack''')
    time.sleep(4)
    playerchoice_turn = input("")
    playerchoice_turn = playerchoice_turn.upper()
    if playerchoice_turn == "1":
      self.attack()
      time.sleep(3)
      clear()
    elif playerchoice_turn == "2":
      self.dodge()
      time.sleep(3)
      clear()
    elif playerchoice_turn == "3":
      self.double()
      time.sleep(3)
      clear()

  def Turns_bot(self):

    def enemy_choice():
      if self.health <= 50 and self.power_round == 1:
        playerchoice_turn = random.randint(1, 3)
      elif self.health <= 50 and self.power_round == 0:
        playerchoice_turn = random.randint(1, 3)
      elif self.health > 50 and self.power_round == 1 and self.just_dodged <= 2:
        playerchoice_turn = random.randint(2, 3)
      elif self.health > 50 and self.power_round == 1 and self.just_dodged >= 3:
        playerchoice_turn = random.randint(1, 3)
        if playerchoice_turn == 2:
          playerchoice_turn = 1
      elif self.health > 50 and self.power_round == 0 and self.just_dodged <= 2:
        playerchoice_turn = random.randint(1, 2)
      elif self.health > 50 and self.power_round == 1 and self.just_dodged >= 3:
        playerchoice_turn = 1
      else:
        playerchoice_turn = 1
      return playerchoice_turn

    playerchoice_turn = enemy_choice()

    if playerchoice_turn == 1:
      self.just_dodged = self.just_dodged - 1
      self.attack_bot()
      time.sleep(3)
      clear()
    elif playerchoice_turn == 2:
      self.dodge_bot()
      self.just_dodged = self.just_dodged + 1
      time.sleep(3)
      clear()
    elif playerchoice_turn == 3:
      self.double_robot()
      time.sleep(3)
      clear()


player1 = Robot(100, random.randint(30, 40), random.randint(30, 35), None, 0,
                "player 1", 0)
player2 = Robot(100, random.randint(30, 40), random.randint(30, 35), None, 0,
                "player 2", 0)

player1.target = player2
player2.target = player1

rounds = 1

playing_bot = 0


#welcome message
def welcome():
  #Prints welcome message and asks for name.
  print("Welcome to Bot Brawl!")
  time.sleep(1)
  clear()
  print("Hi, you are at the menu page right now!\n")
  print("\nPlease choose an option below.\n")

  # Introduce different options
  time.sleep(1)
  print(
      "1.To start a battle, please type '1'.\n2.To go to the controls menu, please type '2'.\n3.To go to credits page, please type '3'."
  )
  option = input("Choice:")
  option = option.lower()

  def options(option):
    #Going to start a battle
    if option == "1":
      time.sleep(1)
      clear()

      print(
          "\nYou have chosen to start a battle!\n Enter 1 to play against a friend.\n Enter 2 to play against a bot."
      )
      battle = input("Choose your battle type:")
      battle = battle.lower()
      time.sleep(1)
      clear()
      start_battle(battle)

    #go to control menu
    elif option == "2":
      print("You have chosen to go to the controls menu!")
      time.sleep(1)
      clear()

    #go to credits
    elif option == "3":
      print("You have chosen to go to the credits page!")
      time.sleep(1)
      clear()

    else:
      print("You have not entered a valid option. Please try again.")
      option = input("Choice: ")
      options(option)

  options(option)


def turns():
  x = 1
  while player1.health > 0 and player2.health > 0:
    print("Player " + str(x) + "'s turn")
    if x == 1:
      player1.Turn()
      x = 2
    elif x == 2:
      player2.Turn()
      x = 1

  if player1.health <= 0:
    return 2

  elif player2.health <= 0:
    return 1


def turns_bot():
  player2.name = "Enemy"
  x = 1
  while player1.health > 0 and player2.health > 0:
    print("Player " + str(x) + "'s turn")
    if x == 1:
      player1.Turn()
      x = 2
    elif x == 2:
      player2.Turns_bot()
      x = 1

  if player1.health <= 0:
    return 2

  elif player2.health <= 0:
    return 1


def show_results(round_relsuts, player1, player2, rounds):
  print("\n== Battle Results ==")
  player1.health = 100
  player2.health = 100
  player1.power_round = 1
  player2.power_round = 1
  if round_relsuts == 2:
    print(f"{player2.name} wins the battle!")
    player2.coins += 10
    player2.rounds_won += 1
    print(f"{player2.name} earned 10 coins!")
    print(f"Total Coins: {player2.coins}")
    print("You can access the shop only after you win the battle.")
    entershop = input("Would you like to go to the shop? (Y/N): ")
    entershop = entershop.upper()
    if entershop == "Y":
      time.sleep(3)
      clear()
      open_shop(player2)
      time.sleep(3)
      clear()
    print("Switching to player 1's results.")
    print(f"{player1.name} lost the battle!")
    print(f"{player1.name} got no coins")
    print(f"Total Coins: {player1.coins}")
    time.sleep(4)
    clear()
  elif round_relsuts == 1:
    print(f"{player1.name} wins the battle!")
    player1.coins += 10
    player1.rounds_won += 1
    print(f"{player1.name} earned 10 coins!")
    print(f"Total Coins: {player1.coins}")
    print("You can access the shop only after you win the battle.")
    entershop = input("Would you like to go to the shop? (Y/N): ")
    entershop = entershop.upper()
    if entershop == "Y":
      time.sleep(2)
      clear()
      open_shop(player1)
      time.sleep(3)
      clear()
    print("Switching to player 2's results.")
    time.sleep(2)
    clear()
    print(f"{player2.name} lost the battle!")
    print(f"{player2.name} got no coins")
    print(f"Total Coins: {player2.coins}")
    time.sleep(4)
    clear()

  if player1.rounds_won == 2:
    print(f"{player1.name} wins the game!")
    print("Congratulations!")
    time.sleep(3)
    clear()
    print("Player 1's stats:\nHealth: " + str(player1.health) + "\nAttack:" +
          str(player1.attackpoints) + "\nArmor:" + str(player1.armorpoints) +
          "\nCoins:" + str(player1.coins) + "!")
    time.sleep(3)
    clear()
    print("Player 2's stats:\nHealth: " + str(player2.health) + "\nAttack:" +
          str(player2.attackpoints) + "\nArmor:" + str(player2.armorpoints) +
          "\nCoins:" + str(player2.coins) + "!")
    time.sleep(3)
    clear()
    print("Thank you for playing Bot Brawl!")
  elif player2.rounds_won == 2:
    print(f"{player2.name} wins the game!")
    print("Congratulations!")
    time.sleep(3)
    clear()
    print("Player 2's stats:\nHealth: " + str(player2.health) + "\nAttack:" +
          str(player2.attackpoints) + "\nArmor:" + str(player2.armorpoints) +
          "\nCoins:" + str(player2.coins) + "!")
    time.sleep(3)
    clear()
    print("Player 1's stats:\nHealth: " + str(player1.health) + "\nAttack:" +
          str(player1.attackpoints) + "\nArmor:" + str(player1.armorpoints) +
          "\nCoins:" + str(player1.coins) + "!")
    time.sleep(3)
    clear()
    print("Thank you for playing Bot Brawl!")
  else:
    rounds = rounds + 1
    print("Time for another round!")
    if playing_bot == 1:
      start_battle("2")
    elif playing_bot == 0:
      start_battle("1")


def start_battle(battle):
  #Choose who to play against and start the battle.
  if battle == "2":
    print("You have chosen to play against a bot!\n Starting game...")
    time.sleep(2)
    clear()
    global playing_bot
    playing_bot = 1
    result = turns_bot()
    show_results(result, player1, player2, rounds)
  elif battle == "1":
    print("You have chosen to play against a friend!\n Starting game...")
    time.sleep(2)
    clear()
    result = turns()
    show_results(result, player1, player2, rounds)
  else:
    print("You have not entered a valid option. Please try again.")
    print(
        "\n Enter 1 to play against a friend.\n Enter 2 to play against a bot."
    )
    battle = input("\nChoose your battle type:")
    time.sleep(1)
    clear()
    start_battle(battle)


#shop
def open_shop(player):
  #Determine if the player can open shop.
  if player.coins >= 10:
    print("You have chosen to go to the shop!")
    print(
        "Congratulations, you have enough coins to enter the shop!\n Loading..."
    )
    time.sleep(2.5)
    clear()
    shop(player)


def shop(player):
  #Open shop and ask what to buy.
  print(
      "Welcome to the shop!\nThese are your abilities right now: \n Health: " +
      str(player.health) + "\n Attack: " + str(player.attackpoints) +
      "\n Armor: " + str(player.armorpoints) + "\n")
  print("You can use coins to upgrade your robot. What would you like to buy?")
  print("1. Health +50 (20 coins)")
  print("2. Attack +5 (10 coins)")
  print("3. Armor +5 (10 coins)")
  print("4. Exit")
  print("You have " + str(player.coins) +
        " coins.\n Enter the number of your choice below.")

  #buying things
  def buy_things(buy):
    '''Buy things in the shop.'''
    #buy health, show new abilities
    if buy == "1":
      if player.coins >= 20:
        player.health += 50
        player.coins -= 20
        time.sleep(1)
        clear()
        print("You have bought 50 health! You now have:\nHealth: " +
              str(player.health) + "\nAttack:" + str(player.attackpoints) +
              "\nArmor:" + str(player.armorpoints) + "\nCoins:" +
              str(player.coins) + "!")
        if player.coins >= 10:
          print(
              "Type '4' to exit the shop.\nIf you would like to buy more items, type'5'."
          )
          buy = input("Enter here:")
        elif player.coins < 10:
          buy = input("Type '4' to exit the shop:")
      elif player.coins < 20:
        time.sleep(1)
        clear()
        print("You do not have enough coins to buy this item.")
        print(
            "Type '4' to exit the shop, or type '5' to go back to the shop menu."
        )
        buy = input("Enter choice:")
      buy_things(buy)

    #buy attack, show new abilities
    elif buy == "2":
      if player.coins >= 10:
        player.attackpoints += 5
        player.coins -= 10
        time.sleep(1)
        clear()
        print("You have bought 5 attack! You now have:\nHealth: " +
              str(player.health) + "\nAttack:" + str(player.attackpoints) +
              "\nArmor:" + str(player.armorpoints) + "\nCoins:" +
              str(player.coins) + "!")
        if player.coins >= 10:
          print(
              "Type '4' to exit the shop.\nIf you would like to buy more items, type'5'."
          )
          buy = input("Enter here:")
        elif player.coins < 10:
          buy = input("Type '4' to exit the shop:")

      elif player.coins < 10:
        time.sleep(1)
        clear()
        print("You do not have enough coins to buy this item.")
        buy = input("Type '4' to leave:")
      buy_things(buy)

    #buy armor, show new abilities
    elif buy == "3":
      if player.coins >= 10:
        player.armorpoints += 5
        player.coins -= 10
        time.sleep(1)
        clear()
        print("You have bought 5 armor! You now have:\nHealth: " +
              str(player.health) + "\nAttack:" + str(player.attackpoints) +
              "\nArmor:" + str(player.armorpoints) + "\nCoins:" +
              str(player.coins) + "!")
        if player.coins >= 10:
          print(
              "Type '4' to exit the shop.\nIf you would like to buy more items, type'5'."
          )
          buy = input("Enter here:")
        elif player.coins < 10:
          buy = input("Type '4' to exit the shop:")

      elif player.coins < 10:
        time.sleep(1)
        clear()
        print("You do not have enough coins to buy this item.")
        buy = input("Type '4' to leave:")
      buy_things(buy)

    #exit shop
    elif buy == "4":
      time.sleep(1)
      clear()
      print("Exiting the shop...")
      time.sleep(2)
      clear()

    #go back
    elif buy == "5":
      time.sleep(1)
      clear()
      shop(player)

    #invalid option
    else:
      print("You have not entered a valid option. Please try again.")
      buy = input("Enter here:")
      buy_things(buy)

  buy = input("Enter here:")
  time.sleep(1)
  clear()
  buy_things(buy)


welcome()
