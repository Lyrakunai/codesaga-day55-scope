# Codesaga - Day 55
# Topic: Scope in Python


# 1. Local Scope

def show_local():
    name = "Riya"
    print(name)


show_local()


# 2. Global Scope: Reading a Global Variable

name = "Alice"


def show_name():
    print(name)


show_name()
print(name)


# 3. Local and Global Variables with the Same Name

name = "Alice"


def local_name():
    name = "Bob"
    print(name)


local_name()
print(name)


# 4. Modifying a Global Variable

score = 100


def update_score():
    global score
    score += 20


update_score()
print(score)


# 5. Enclosing Scope

def outer():
    value = "Enclosing"

    def inner():
        print(value)

    inner()


outer()


# 6. Local Scope Takes Priority

value = "Global"


def outer_value():
    value = "Enclosing"

    def inner_value():
        value = "Local"
        print(value)

    inner_value()


outer_value()


# 7. Accessing an Enclosing Variable

def show_enclosing():
    value = "Global"

    def inner():
        print(value)

    inner()


show_enclosing()


# 8. Modifying an Enclosing Variable with nonlocal

def outer_score():
    score = 50

    def increase():
        nonlocal score
        score += 10

    increase()
    print(score)


outer_score()


# 9. global Inside a Nested Function

value = "Global"


def outer_global():
    value = "Enclosing"

    def inner_global():
        global value
        value = "Changed Global"

    inner_global()
    print(value)


outer_global()
print(value)