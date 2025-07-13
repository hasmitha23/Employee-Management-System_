import getpass


# Admin Login System
admin_id = "Hasmitha8866"
admin_password = "hasmitha@86"

print("="*40)
print("🔐 Admin Login Required".center(40))
print("="*40)

entered_id = input("Enter Admin ID: ").strip()
entered_pass = getpass.getpass("Enter Password: ").strip()


if entered_id != admin_id or entered_pass != admin_password:
    print("❌ Access Denied! Invalid credentials.")
    exit()
else:
    print("✅ Login Successful! Welcome, Hasmitha(Admin).")

# 🧠 Employee Data Storage
employee_db = {}

# 📜 Show Menu
def show_menu():
    print("\n🛠️ What would you like to do?")
    print("1. ➕ Add Employee")
    print("2. 📋 View All Employees")
    print("3. ✏️ Update Employee")
    print("4. ❌ Delete Employee")
    print("5. 💰 Salary Report")
    print("6. 🚪 Exit")

# 🚀 App Starts
print("="*40)
print("🤖 Employee Management System".center(40))
print("="*40)

while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ").strip()

    # ➕ Add Employee
    if choice == '1':
        print("\n[+] Add Employee Selected")
        emp_id = input("Enter Employee ID (e.g., E101): ").strip()
        if emp_id in employee_db:
            print("⚠️ This ID already exists. Try a different one.")
        else:
            name = input("Enter Employee Name: ").strip().title()
            try:
                age = int(input("Enter Age: "))
                exp = float(input("Enter Years of Experience: "))
                salary = float(input("Enter Salary (₹): "))
                employee_db[emp_id] = {
                    "name": name,
                    "age": age,
                    "exp": exp,
                    "salary": salary
                }
                print(f"✅ Employee {name} (ID: {emp_id}) added successfully!")
            except ValueError:
                print("❌ Invalid input. Age, experience, and salary must be numbers.")

    # 📋 View Employees
    elif choice == '2':
        print("\n📋 Employee List")
        if not employee_db:
            print("😶 No employees found. Try adding some first!")
        else:
            print("-" * 70)
            print(f"{'ID':<10} {'Name':<15} {'Age':<5} {'Exp(yrs)':<10} {'Salary(₹)':>10}")
            print("-" * 70)
            for emp_id, d in employee_db.items():
                print(f"{emp_id:<10} {d['name']:<15} {d['age']:<5} {d['exp']:<10} {d['salary']:>10.2f}")
            print("-" * 70)
            print(f"👥 Total Employees: {len(employee_db)}")

    # ✏️ Update Employee
    elif choice == '3':
        print("\n✏️ Update Employee")
        emp_id = input("Enter Employee ID to update: ").strip()
        if emp_id not in employee_db:
            print("❌ Employee ID not found.")
        else:
            current = employee_db[emp_id]
            print(f"Current Details: {current}")
            print("What would you like to update?")
            print("1. Name only")
            print("2. Salary only")
            print("3. Both Name and Salary")
            print("4. All Details")

            update_choice = input("Enter choice (1, 2, 3, or 4): ").strip()

            if update_choice == '1':
                new_name = input("Enter new name: ").strip().title()
                employee_db[emp_id]['name'] = new_name
                print("✅ Name updated successfully!")
            elif update_choice == '2':
                try:
                    new_salary = float(input("Enter new salary (₹): "))
                    employee_db[emp_id]['salary'] = new_salary
                    print("✅ Salary updated successfully!")
                except ValueError:
                    print("❌ Invalid salary input.")
            elif update_choice == '3':
                new_name = input("Enter new name: ").strip().title()
                try:
                    new_salary = float(input("Enter new salary (₹): "))
                    employee_db[emp_id]['name'] = new_name
                    employee_db[emp_id]['salary'] = new_salary
                    print("✅ Name and salary updated successfully!")
                except ValueError:
                    print("❌ Invalid salary input.")
            elif update_choice == '4':
                try:
                    new_name = input("New Name: ").strip().title()
                    new_age = int(input("New Age: "))
                    new_exp = float(input("New Experience (yrs): "))
                    new_salary = float(input("New Salary (₹): "))
                    employee_db[emp_id] = {
                        "name": new_name,
                        "age": new_age,
                        "exp": new_exp,
                        "salary": new_salary
                    }
                    print("✅ All details updated successfully!")
                except ValueError:
                    print("❌ Invalid input. Please use proper number formats.")
            else:
                print("⚠️ Invalid update option.")

    # ❌ Delete Employee
    elif choice == '4':
        print("\n❌ Delete Employee")
        emp_id = input("Enter Employee ID to delete: ").strip()
        if emp_id in employee_db:
            confirm = input(f"Are you sure you want to delete {employee_db[emp_id]['name']}? (yes/no): ").strip().lower()
            if confirm == 'yes':
                del employee_db[emp_id]
                print("✅ Employee deleted successfully.")
            else:
                print("❎ Deletion cancelled.")
        else:
            print("⚠️ Employee ID not found.")

    # 💰 Salary Report
    elif choice == '5':
        print("\n💰 Salary Report")
        if not employee_db:
            print("😕 No employees in the system yet.")
        else:
            salaries = [details['salary'] for details in employee_db.values()]
            total = sum(salaries)
            average = total / len(salaries)
            max_salary = max(salaries)
            min_salary = min(salaries)
            highest_paid = [eid for eid, details in employee_db.items() if details['salary'] == max_salary]
            lowest_paid = [eid for eid, details in employee_db.items() if details['salary'] == min_salary]

            print(f"\n📊 Total Salary Expense: ₹{total:.2f}")
            print(f"📈 Average Salary: ₹{average:.2f}")
            print(f"👑 Highest Paid: {', '.join(highest_paid)} (₹{max_salary:.2f})")
            print(f"📉 Lowest Paid: {', '.join(lowest_paid)} (₹{min_salary:.2f})")

    # 🚪 Exit
    elif choice == '6':
        print("\n👋 Exiting... Have a great day, Admin!")
        break

    else:
        print("\n⚠️ Invalid choice. Please enter a number from 1 to 6.")