print ("=== MLBB DAMAGE CALCULATOR ===")
print ("Gawa ni: Jhon Nexter - Level 3 Dev")
print ("")

hero = input("Enter hero mo: ")
attack = int(input("Enter Physical Attack mo: "))
enemy_defense = int(input("Enter Defense ng kalaban: "))

# Formula: Damage = Attack - Defense, pero  minimum 1 damage
damage = attack - enemy_defense

if damage < 1:
    damage = 1
    print ("WARNING: Makunat kalaban! 1 damage lang!")
    
print ("")
print ("=== RESULT ===")
print ("Hero", hero)
print ("Final Damage mo:", damage)

if damage >= 500:
    print ("BURST DAMAGE! One hit delete yan!")
elif damage >= 200:
    print ("Solid damage, Kaya mo yan 3 hits.")
else:
    print ("Sustain lang. Poking damage. Wag sugod.")
print ("")
print ("GG! Project #3 ni Jhon Nexter!")