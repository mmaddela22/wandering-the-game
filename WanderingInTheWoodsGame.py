import random
import time

class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moves = 0

def initialize_grid(rows, cols, num_people):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    people = []
    
    for i in range(num_people):
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        people.append(Person(x, y))
        grid[x][y] = str(i)
    
    return grid, people

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def move_person(person, rows, cols):
    direction = random.choice(['up', 'down', 'left', 'right'])
    
    if direction == 'up' and person.x > 0:
        person.x -= 1
    elif direction == 'down' and person.x < rows - 1:
        person.x += 1
    elif direction == 'left' and person.y > 0:
        person.y -= 1
    elif direction == 'right' and person.y < cols - 1:
        person.y += 1
    
    person.moves += 1

def check_collisions(people):
    positions = [(person.x, person.y) for person in people]
    return len(positions) != len(set(positions))

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    num_people = int(input("Enter number of people: "))
    
    grid, people = initialize_grid(rows, cols, num_people)
    
    while not check_collisions(people):
        for person in people:
            move_person(person, rows, cols)
        
        print_grid(grid)
        time.sleep(1)
        print("\n")
    
    print("Collisions detected!")
    for person in people:
        print(f"Person {grid[person.x][person.y]} took {person.moves} moves.")
    
if __name__ == "__main__":
    main()
