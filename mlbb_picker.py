import random

print ("=== MLBB RANDOM HERO PICKER ===")
print ("Gawa ni: Jhon Nexter from Polomolok")
print ("")

player = "Jhon Nexter"
heroes = ["Miya", "Alucard", "Layla", "Gusion", "Angela", "Chou", "Fanny", "Lancelot"]

random_hero = random.choice(heroes)

print ("Player:", player)
print ("Hero mo ngayong game:", random_hero)
print ("")

if random_hero == "Layla" or random_hero == "Miya":
    print ("MM KA BRAD! Sa likod ka lang. Farm muna bago away")
elif random_hero == "Chou" or random_hero == "Alucard":
    print ("FIGHTER GODS! Pang-buhat ka. Go 1v5 mo na yan!")
elif random_hero == "Gusion" or random_hero == "Lancelot" or random_hero == "Fanny":
    print ("ASSASSIN MAIN! Fast hands lang. Combo mo agad!")
elif random_hero == "Angela":
    print ("SUPPORT GODDESS! Dikit ka sa carry nyo. Heal heal!")
else:
    print ("Kahit anong hero, win yan basta ikaw")
    
print ("")
print ("GG! Project #2 ni Jhon Nexter!")
print ("GitHub: github.com/jhonnexterherrada00-alt")