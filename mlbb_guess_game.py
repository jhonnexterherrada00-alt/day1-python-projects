# Project #5 ni Jhon Nexter - Day 3
# Natutunan ko: while loop + break
# Hirap ako sa: Di humihinto yung loop nung una

import random

print("=== MLBB GUESS GAME ===")
print("Gawa ni: Jhon Nexter - Day 3 Dev")
print("Level 6 Project: The Looper 2.0")
print("")

secret_hero = "Claude"
tries = 0

print("Hulaan mo main hero ni Elnika na Top 1 Global!")
print("Hint: Marksman. Monkey Pet. Male Hero")
print("")

while True:
    hula = input("Hula mo: ")
    tries = tries + 1
    
    if hula == secret_hero:
        print("")
        print("TAMA KA BRAD!")
        print("Si Claude nga main ni Elnika!")
        print("Tries mo:", tries)
        print("GG! Project #5 ni Jhon Nexter!")
        print("Day 3 Complete! Level 6 Unlocked: The Looper 2.0!")
        break
    else:
        print("Mali! Try ulit. Isip pa")
        print("")
        
        print("Finished")