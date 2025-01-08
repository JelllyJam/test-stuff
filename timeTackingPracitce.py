# purpose: this file is for learning how to store data for another time. This is preparation for making the habit tracking program

import datetime

def add_habit(habit_name):
    with open("habits.txt", "a") as f:
        f.write(f"{habit_name},{datetime.date.today()}:0\n")

def track_habit(habit_name):
    with open("habits.txt", "r") as f:
        lines = f.readlines()

    with open("habits.txt", "w") as f:
        for line in lines:
            if line.startswith(habit_name):
                habit, date_str, count = line.strip().split(",")
                date = datetime.date.fromisoformat(date_str)
                if date == datetime.date.today():
                    count = int(count) + 1
                f.write(f"{habit},{date}:{count}\n")
            else:
                f.write(line)

def view_habits():
    with open("habits.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            habit, date_str, count = line.strip().split(",")
            print(f"{habit}: {count} on {date_str}")

if __name__ == "__main__":
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Track Habit")
        print("3. View Habits")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            habit_name = input("Enter habit name: ")
            add_habit(habit_name)
        elif choice == "2":
            habit_name = input("Enter habit name: ")
            track_habit(habit_name)
        elif choice == "3":
            view_habits()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

print('done')