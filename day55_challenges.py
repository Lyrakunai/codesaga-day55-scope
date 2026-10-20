# Codesaga - Day 55
# Challenge: Scope and Variable Management

# Global variable
completed_tasks = 0


def complete_task():
    global completed_tasks
    completed_tasks += 1


def create_session():
    # Each session has its own private progress
    progress = 0

    def perform_action():
        nonlocal progress
        progress += 1

    def show_progress():
        print("Session progress:", progress)

    perform_action()
    perform_action()
    show_progress()

    perform_action()
    show_progress()

    complete_task()

    return show_progress


# Session 1
session_one = create_session()

# Session 2
session_two = create_session()

# Continue Session 1 independently
session_one()

# Display application-wide count
print("Completed sessions:", completed_tasks)