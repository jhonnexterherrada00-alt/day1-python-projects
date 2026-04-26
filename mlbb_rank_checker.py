# Project #4 ni Jhon Nexter - Day 2
# Natutunan ko: def function + return
# Hirap ako sa: return vs print, pero gets ko na ngayon!

def check_rank(points) :
    # Function ko to para mag-check ng rank
    if points >= 100:
        return "Mythic Glory kana brad! Pang-MPL ka na!"
    elif points >= 50:
        return "Mythic ka na! Solid!"
    elif points >= 25:
        return "Legend. Konti na lang Mythic!"
    elif points >= 10:
        return "Epic. Grind pa brad."
    else:
        return "Warrior pa. Simula pa lang. Kaya mo yan!"
        
print ("=== MLBB RANK CHECKER ===")
print ("Gawa ni: Jhon Nexter - Day 2 Dev")
print ("Level 5 Project: Function Master")
print ("")

name = input ("Name mo: ")
stars = int(input("Ilang stars ka ngayon: "))

# Tawag ko yung function ko tapos save sa result
result = check_rank(stars)

print ("")
print ("=== RESULT ===")
print ("Player:", name)
print ("Stars:", stars)
print ("Rank mo:", result)
print ("")
print ("GG! Project #4 ni Jhon Nexter!")
print ("Day 2 Complete! Level 5 Unlocked: The Function Master!")