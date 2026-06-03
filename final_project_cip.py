import random

# ---- CLASES ----

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.used_evasion = False
        self.used_immunity = False
        
        if player_class == "Warrior":
            self.health = 200
            self.max_health = 200
            self.abilities = {
                "1": ("Mortal Strike", 25),
                "2": ("Heroic Strike", 40),
                "3": ("Execute", 100),
                "4": ("Shield Block", 40 ),
                "5": ("Info", 0)
            }
        elif player_class == "Mage":
            self.health = 100
            self.max_health = 100
            self.abilities = {
                "1": ("Frostbolt", 45),
                "2": ("Arcane Blast", 60),
                "3": ("Ice Barrier", 35),
                "4": ("Ice Block", 50),
                "5": ("Info", 0)
            }
        elif player_class == "Rogue":
            self.health = 150
            self.max_health = 150
            self.abilities = {
                "1": ("Sinister Strike", 30),
                "2": ("Slice and Dice", 45),
                "3": ("Cloak of Shadows", 40),
                "4": ("Vanish", 30),
                "5": ("Info", 0)
            }

    def immunity_attack(self, enemy):
        ability_name, damage = self.abilities["3"]
        self.used_immunity = True
        enemy.health -= damage
        print(f"{ability_name} deals {damage} damage! 50% chance to dodge incoming attack!")

    def attack(self, ability_key, enemy):
        ability_name, damage = self.abilities[ability_key]
        verificar_vida = (30 * enemy.max_health) / 100
        
        if self.player_class == "Warrior" and ability_key == "3":
            if enemy.health <= verificar_vida:
                print(f"EXECUTE! {ability_name} deals {damage} damage!")
                enemy.health -= damage
            else:
                print(f"Execute can only be used when enemy is below 30% HP!")
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
        heal_amounts = {
            "Warrior": 40,
            "Mage": 50,
            "Rogue": 30
        }
        heal_amount = heal_amounts[self.player_class]
        self.health = min(self.health + heal_amount, self.max_health)
        self.used_evasion = True
        print(f"You heal for {heal_amount} HP!")


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage

    def attack(self, player):
        actual_damage = random.randint(self.damage - 5, self.damage + 5)

        #heal y dodge
        if player.used_evasion:
            player.used_evasion = False
            dodge_chance = {
                "Warrior": 0.5,
                "Mage": 1.0,
                "Rogue": 0.7
            }
            if random.random() < dodge_chance[player.player_class]:
                print(f"Dodge!! No damage taken!")
                return

        #immunity
        if player.used_immunity:
            player.used_immunity = False
            if random.random() < 0.5:
                print(f"Immune! No damage taken!")
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
    while True:
        print("\nChoose your action:")
        for key, (name, value) in player.abilities.items():
            if key == "3" or key == "4":
                print(f"{key}. {name}")
            elif key == "5":
                print(f"{key}. {name}")
            else:
                print(f"{key}. {name} (Damage: {value})")

        choice = input("Enter 1-5: ")

        if choice == "5":
            print("\n=== ABILITIES INFO ===")
            if player.player_class == "Warrior":
                print("1. Mortal Strike   - Deals 25 damage")
                print("2. Heroic Strike   - Deals 40 damage")
                print("3. Execute         - Deals 100 damage (only below 30% enemy HP)")
                print("4. Shield Block    - heal 40 HP + 50% chance to block next attack")
            elif player.player_class == "Mage":
                print("1. Frostbolt       - Deals 45 damage")
                print("2. Arcane Blast    - Deals 60 damage")
                print("3. Ice Barrier     - 50% chance immune while attacking")
                print("4. Ice Block       - Heal 50 HP + 100% dodge next attack")
            elif player.player_class == "Rogue":
                print("1. Sinister Strike - Deals 30 damage")
                print("2. Slice and Dice  - Deals 45 damage (40% crit x2)")
                print("3. Cloak of Shadows- 50% chance immune while attacking")
                print("4. Vanish          - Heal 30 HP + 70% dodge next attack")
            print("======================")
        elif choice in ["1", "2", "3", "4"]:
            if choice == "4":
                player.heal(choice)
            elif choice == "3":
                if player.player_class == "Warrior":
                    player.attack("3", enemy)  # Execute
                else:
                    player.immunity_attack(enemy)  # Ice Barrier / Cloak of Shadows
            else:
                player.attack(choice, enemy)
            return
        else:
            print("Invalid option. Please enter 1-5.")


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
            player.health = min(player.health + 30, player.max_health)
    else:
        print("\n=== You defeated all enemies! YOU WIN! ===")


if __name__ == "__main__":
    main()