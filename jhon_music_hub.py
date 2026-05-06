# lesson_scheduler.py - Level 11: The Function Master
# Student Management System para sa Jhon's Music Hub

# 1. Student Database - Dictionary
students = {}

# 2. Function: Mag-add ng new student
def enroll_student(name, instrument, day, time):
    student_id = len(students) + 1
    students[student_id] = {
        "name": name,
        "instrument": instrument,
        "schedule": f"{day} - {time}",
        "payment_status": "Pending"
    }
    print(f"✅ Enrolled: {name} - {instrument} every {day} at {time}")

# 3. Function: Mark student as paid
def mark_paid(student_id):
    if student_id in students:
        students[student_id]["payment_status"] = "Paid"
        name = students[student_id]["name"]
        print(f"💰 Payment received from {name}!")
    else:
        print("❌ Student not found!")

# 4. Function: Show all students - The Master Report
def show_all_students():
    print("\n=== JHON'S MUSIC HUB - STUDENT ROSTER ===")
    total_income = 0
    
    if not students:
        print("Wala pang students. Enroll ka na!")
        return
    
    for id, data in students.items():
        print(f"\nStudent #{id}")
        print(f"  Name: {data['name']}")
        print(f"  Instrument: {data['instrument']}")
        print(f"  Schedule: {data['schedule']}")
        print(f"  Payment: {data['payment_status']}")
        
        if data['payment_status'] == "Paid":
            total_income += 400  # ₱400 per lesson
    
    print(f"\n💰 TOTAL INCOME THIS MONTH: ₱{total_income}")
    print(f"👑 Total Students: {len(students)}")
    print(f"📍 Branch: Polomolok Main")

# 5. TESTING - Simulan natin yung school mo!
print("🎸 Jhon's Music Hub - Lesson Scheduler 🎸\n")

# Enroll 3 students sa Polomolok Branch
enroll_student("Maria Santos", "Guitar", "Monday", "4:00 PM")
enroll_student("Pedro Cruz", "Drums", "Tuesday", "5:00 PM") 
enroll_student("Ana Reyes", "Piano", "Wednesday", "3:00 PM")

# Mark 2 as paid
mark_paid(1)  # Maria bayad na
mark_paid(3)  # Ana bayad na

# Show report
show_all_students()