# jhon_music_empire.py - Future CEO Simulator
# Level 10: The Cart Master + Boss Mode

# 1. Branches mo - Dictionary
branches = {
    "Polomolok": {
        "staff": ["Ana - Cashier", "Mark - Guitar Teacher"],
        "services": {"guitar_lesson": 400, "band_studio": 300, "guitar_sale": 3500},
        "daily_sales": 0
    },
    "Tupi": {
        "staff": ["Future Staff"],
        "services": {"guitar_lesson": 400, "guitar_sale": 3500},
        "daily_sales": 0
    }
}

# 2. Function: Mag-add ng sales
def add_sale(branch_name, service_name, quantity=1):
    if branch_name in branches:
        price = branches[branch_name]["services"][service_name]
        total = price * quantity
        branches[branch_name]["daily_sales"] += total
        print(f"✅ {branch_name}: Sold {quantity}x {service_name} = ₱{total}")
    else:
        print("❌ Branch not found!")

# 3. Function: Check Empire Status
def empire_report():
    print("\n=== JHON'S MUSIC EMPIRE REPORT ===")
    total_empire_sales = 0
    
    for city, data in branches.items():
        print(f"\n📍 {city} Branch:")
        print(f"   Staff: {', '.join(data['staff'])}")
        print(f"   Today's Sales: ₱{data['daily_sales']}")
        total_empire_sales += data['daily_sales']
    
    print(f"\n💰 TOTAL EMPIRE SALES TODAY: ₱{total_empire_sales}")
    print(f"👑 Boss Jhon Status: LEGEND")
    
# 4. TESTING - Simulan natin yung business mo!
print("🎸 Welcome to Jhon's Music Hub! 🎸\n")

# Polomolok Sales Today
add_sale("Polomolok", "guitar_lesson", 3)  # 3 students nag-enroll
add_sale("Polomolok", "band_studio", 2)    # 2 hours studio rent
add_sale("Polomolok", "guitar_sale", 1)    # 1 guitar nabenta

# Tupi Sales Today - Future branch mo
add_sale("Tupi", "guitar_lesson", 1)       # 1 student sa Tupi

# Show Empire Report
empire_report()