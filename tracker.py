habits = []
def add_habit(habit_name):
    habits.append({'Habit_name': habit_name, })
    return 
def view_habits():
    return habits
def remove_habit(habit):
    if habit in habits:
        habits.remove(habit)
        return habits
    else:
        return"habit not found"
    
while True:
    print("Choose an option:")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Remove Habit")
    print("4.Exit")

    
    choice = int(input())
    if choice == 1:
        habit_name = input("Enter habit name: ")
        add_habit(habit_name)
        print("Habit added.")
    elif choice == 2:
        print("Your habits:")
        for habit in view_habits():
            print(habit)
    elif choice == 3:
        habit_name = input("Enter habit name to remove: ")
        result = remove_habit({'Habit_name': habit_name, })
        print(result)
    elif choice == 4:
        print("Exiting the habit tracker.")
        break
    else:
        print("Invalid choice")



