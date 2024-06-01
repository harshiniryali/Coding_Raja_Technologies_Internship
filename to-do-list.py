import json
import os
from datetime import datetime

tasks = []

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    tasks.append({
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })
    save_tasks()
    print("Task added successfully!")

def remove_task():
    task_name = input("Enter task name to remove: ")
    for task in tasks:
        if task["name"] == task_name:
            tasks.remove(task)
            save_tasks()
            print(f"Task '{task_name}' removed successfully.")
            return
    print(f"Task '{task_name}' not found.")

def mark_completed():
    task_name = input("Enter task name to mark as completed: ")
    for task in tasks:
        if task["name"] == task_name:
            task["completed"] = True
            save_tasks()
            print(f"Task '{task_name}' marked as completed.")
            return
    print(f"Task '{task_name}' not found.")

def list_tasks():
    print("\n--- Task List ---")
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"{status} {task['name']} (Priority: {task['priority']}, Due: {task['due_date']})")
    print("-----------------\n")

def main():
    global tasks
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()