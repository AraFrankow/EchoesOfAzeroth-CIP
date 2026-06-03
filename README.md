# ⚔ Echoes of Azeroth

A turn-based RPG game built in Python, inspired by World of Warcraft. Fight your way through three enemies — a Murloc, an Orc Warrior, and a Dragon — using unique class abilities and strategic decisions.

Built as a Final Project for [Code in Place 2025](https://codeinplace.stanford.edu/) by Stanford University.

---

## 📸 Screenshots

### Intro Screen
![Intro](/screenshots/screen1.PNG)

### Combat
![Combat](/screenshots/screen2.PNG)

### Victory
![Victory](/screenshots/screen3.PNG)

---

## 🎮 How to Play

### Option 1 — Code in Place IDE (recommended)
1. Go to [codeinplace.stanford.edu](https://codeinplace.stanford.edu/cip6/share/chY0oneYtrSz7eHn5xcE)
2. And run the game.

### Option 2 — Local (console version)
1. Make sure you have Python 3 installed
2. Clone the repository:
   ```
   git clone https://github.com/AraFrankow/EchoesOfAzeroth-CIP.git
   ```
3. Run the game:
   ```
   python final_project_cip.py
   ```

---

## ⚔ Classes

| Class | HP | Playstyle |
|---|---|---|
| **Warrior** | 200 | High HP, physical damage, Execute & Shield Block |
| **Mage** | 100 | Low HP, powerful spells, Ice Barrier & Ice Block |
| **Rogue** | 150 | Medium HP, critical hits, Cloak of Shadows & Vanish |

---

## 🗡 Abilities

### Warrior
| # | Ability | Description |
|---|---|---|
| 1 | Mortal Strike | Deals 25 damage |
| 2 | Heroic Strike | Deals 40 damage |
| 3 | Execute | Deals 100 damage (only usable below 30% enemy HP) |
| 4 | Shield Block | Heal 40 HP + 50% chance to dodge next attack |

### Mage
| # | Ability | Description |
|---|---|---|
| 1 | Frostbolt | Deals 45 damage |
| 2 | Arcane Blast | Deals 60 damage |
| 3 | Ice Barrier | Deals 35 damage + 50% chance to dodge |
| 4 | Ice Block | Heal 50 HP + 100% dodge next attack |

### Rogue
| # | Ability | Description |
|---|---|---|
| 1 | Sinister Strike | Deals 30 damage |
| 2 | Slice and Dice | Deals 45 damage (40% chance critical hit x2) |
| 3 | Cloak of Shadows | Deals 40 damage + 50% chance to dodge |
| 4 | Vanish | Heal 30 HP + 70% dodge next attack |

---

## 👾 Enemies

| Enemy | HP | Difficulty |
|---|---|---|
| Murloc | 60 | Easy |
| Orc Warrior | 120 | Medium |
| Dragon | 200 | Hard |

---

## 🛠 Built With

- Python 3
- No external libraries — only the built-in `random` module

---

## 📚 About

This project was built as the Final Project for Code in Place 2025, a free introductory Python course by Stanford University. It demonstrates the use of classes, object-oriented programming, loops, conditionals, and functions.
