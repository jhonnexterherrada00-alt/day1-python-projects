print("=== GCASH BUDGET CHECKER===")
print("Gawa ni: Jhon Nexter - Day 6 Dev")
print("Level 9 Project: The Budget Judge")
print("")

# Gcash wallet mo
wallet = {
     "name": "Jhon Nexter",
     "balance": 350,
     "food_budget": 150,
     "load_budget": 100
}

midnight_snack = 120

print("Checking Gcash ni", wallet["name"])
print("Current Balance: ₱", wallet["balance"])
print("Food Budget mo: ₱", wallet["food_budget"])
print("Midnight Snack: ₱", midnight_snack)
print("")

#Check kung kaya bumili
if wallet["balance"] >= midnight_snack and wallet["food_budget"] >= midnight_snack:
    print("STATUS: ORDER NA BRAD!")
    print("Kaya mo bumili ng Midnight Snack!")
    print("Sukli mo: ₱", wallet["balance"] - midnight_snack)
else:
    print("STATUS: TIIS MUNA")
    print("Kulang ka ng ₱", midnight_snack - wallet["balance"])
    print("Mag-extra income ka muna")

print("")