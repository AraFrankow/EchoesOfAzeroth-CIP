import random

# ---- CLASES ----

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.used_evasion = False
        
        if player_class == "Warrior":
            self.health = 200
            self.max_health = 200
            self.abilities = {
                "1": ("Mortal Strike", 25),    #ataque 1
                "2": ("Heroic Strike", 40),    #ataque 2
                "3": ("Shield Block", 40),     #chance to block y heal
                "4": ("Execute", 100),         #solamente se usa cuando tiene 20% de la vida 
                "5": ("Info", 0)               #Es para mostrar la info de los ataques
            }
        elif player_class == "Mage":
            self.health = 100
            self.max_health = 100
            self.abilities = {
                "1": ("Frostbolt", 45),        #ataque 1
                "2": ("Arcane Blast", 60),     #ataque 2
                "3": ("Ice Barrier", 35),      #chance de inmunidad mientras ataca
                "4": ("Ice Block", 40),        #heal y evasion 100%
                "5": ("Info", 0)               #Es para mostrar la info de los ataques
            }
        elif player_class == "Rogue":
            self.health = 150
            self.max_health = 150
            self.abilities = {
                "1": ("Sinister Strike", 30),  #ataque 1
                "2": ("Slice and Dice", 45),   #ataque 2 con chance de critico
                "3": ("Cloak of Shadows", 40), #chance de inmunidad mientras ataca
                "4": ("Vanish", 40),           #heal y evasion 100%
                "5": ("Info", 0)               #Es para mostrar la info de los ataques
            }

    def attack(self, ability_key, enemy):
        ability_name, damage = self.abilities[ability_key]
        verificar_vida = (20 * enemy.max_health) / 100

        if self.player_class == "Warrior" and ability_key == "4":
            if enemy.health <= verificar_vida:
                print(f"EXECUTE! {ability_name} deals {damage} damage!")
                enemy.health -= damage
            else:
                print(f"Execute can only be used when enemy is below 20% HP!")
            return

        if self.player_class == "Rogue" and ability_key == "2":
            if random.random() < 0.4:
                damage = damage * 2
                print(f"CRITICAL HIT! {ability_name} deals {damage} damage!")
            else:
                print(f"{ability_name} deals {damage} damage!")
        else:
            print(f"{ability_name} deals {damage} damage!")
        
        enemy.health -= damage

    def heal(self, ability_key):
        _, heal_amount = self.abilities[ability_key]
        self.health = min(self.health + heal_amount, self.max_health)
        if self.player_class == "Rogue":
            self.used_evasion = True
            print(f"Evasion activated! 50% chance to dodge next attack!")
        else:
            print(f"You heal for {heal_amount} HP!")


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage

    def attack(self, player):
        actual_damage = random.randint(self.damage - 5, self.damage + 5)
        
        if player.player_class == "Rogue" and player.used_evasion:
            if random.random() < 0.5:  # 50% de chance
                print(f"Dodge!! No damage taken")
                player.used_evasion = False  # se gasta por turno
                return
        
        print(f"{self.name} attacks you for {actual_damage} damage!")
        player.health -= actual_damage


# ---- LÓGICA DEL JUEGO ----

def choose_class():
    print("Choose your class:")
    print("1. Warrior (High HP, physical damage)")
    print("2. Mage (Low HP, powerful spells)")
    print("3. Rogue (Medium HP, chance of critical hit and chance of dodge)")
    
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == "1":
            return "Warrior"
        elif choice == "2":
            return "Mage"
        elif choice == "3":
            return "Rogue"
        else:
            print("Invalid option. Please enter 1, 2 or 3.")


def show_status(player, enemy):
    print(f"\n--- {player.name} ({player.player_class}) ---")
    print(f"HP: {player.health}/{player.max_health}")
    print(f"--- {enemy.name} ---")
    print(f"HP: {enemy.health}/{enemy.max_health}")
    print()


def player_turn(player, enemy):
    print("Choose your action:")
    for key, (name, value) in player.abilities.items():
        if key == "3":
            print(f"{key}. {name} (Heal {value} HP)")
        else:
            print(f"{key}. {name} (Damage: {value})")
    
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == "3":
            return player.heal(choice)
        elif choice == "1" or choice == "2":
            return player.attack(choice, enemy)
        else:
            print("Invalid option. Please enter 1, 2 or 3.")


def combat(player, enemy):
    print(f"\nA wild {enemy.name} appears!\n")
    
    while player.health > 0 and enemy.health > 0:
        show_status(player, enemy)
        player_turn(player, enemy)
        
        if enemy.health <= 0:
            print(f"\nYou defeated {enemy.name}!")
            return True
        
        enemy.attack(player)
        
        if player.health <= 0:
            print("\nYou died... Game Over.")
            return False
    
    return False


def main():
    print("=== WoW RPG ===\n")
    name = input("Enter your character's name: ")
    player_class = choose_class()
    player = Player(name, player_class)
    
    enemies = [
        Enemy("Murloc", 60, 10),
        Enemy("Orc Warrior", 120, 20),
        Enemy("Dragon", 200, 35)
    ]
    
    for enemy in enemies:
        result = combat(player, enemy)
        if not result:
            break
        if enemy.name != "Dragon":
            print("\nPrepare for the next enemy...\n")
            player.health = min(player.health + 30, player.max_health)  # heal entre combates
    else:
        print("\n=== You defeated all enemies! YOU WIN! ===")


if __name__ == "__main__":
    main()