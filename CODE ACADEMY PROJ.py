# FUNCTION ARGUMENTS
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False):
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)



### SAMS SURF SHOP
import unittest
import datetime
import surfshop
class ShoppingCart:
    def __init__(self):
        self.item_count = 0
        self.locals_discount = False
        self.checkout_date = None

    def add_surfboards(self, num_surfboards):
        if self.item_count + num_surfboards > 4:
            raise TooManySurfboardsError()
        self.item_count += num_surfboards
        return f"Successfully added {num_surfboards} surfboard{'s' if num_surfboards > 1 else ''} to cart!"

    def get_item_count(self):
        return self.item_count

    def add_item(self, item_name, quantity):
        self.item_count += quantity

    def remove_item(self, item_name, quantity=1):
        self.item_count -= quantity

    def apply_locals_discount(self):
        self.locals_discount = True
        return "Locals discount applied!"

    def set_checkout_date(self, checkout_date):
        if checkout_date <= datetime.datetime.now():
            raise CheckoutDateError()
        self.checkout_date = checkout_date


class TooManySurfboardsError(Exception):
    def __init__(self):
        super().__init__("Cart cannot have more than 4 surfboards in it!")


class CheckoutDateError(Exception):
    def __init__(self):
        super().__init__("Checkout date must be in the future!")


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_surfboards(self):
        self.assertEqual(self.cart.add_surfboards(1), "Successfully added 1 surfboard to cart!")

    def test_add_surfboards_multiple(self):
        self.assertEqual(self.cart.add_surfboards(2), "Successfully added 2 surfboards to cart!")
        self.assertEqual(self.cart.add_surfboards(3), "Successfully added 3 surfboards to cart!")
        self.assertEqual(self.cart.add_surfboards(4), "Successfully added 4 surfboards to cart!")

    @unittest.expectedFailure
    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def test_initial_cart_items(self):
        self.assertEqual(self.cart.get_item_count(), 0)

    def test_add_item_to_cart(self):
        self.cart.add_item("Apple", 2)
        self.assertEqual(self.cart.get_item_count(), 2)

    def test_remove_item_from_cart(self):
        self.cart.add_item("Apple", 2)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.get_item_count(), 0)

    @unittest.skip("Skipping test due to off-season")
    def test_too_many_surfboards_error(self):
        with self.assertRaises(TooManySurfboardsError):
            self.cart.add_surfboards(5)

    def test_set_checkout_date_past(self):
        past_date = datetime.datetime(2022, 1, 1)
        with self.assertRaises(CheckoutDateError):
            self.cart.set_checkout_date(past_date)


if __name__ == '__main__':
    unittest.main()



### NEW TEACHER IN TOWN
from roster import student_roster
import itertools

class ClassroomOrganizer:
    def __init__(self):
        self.students = student_roster

    def get_students_with_subject(self, subject):
        return (student for student in self.students if student['favorite_subject'] == subject)

    def seat_students(self):
        math_students = self.get_students_with_subject('Math')
        science_students = self.get_students_with_subject('Science')
        combinations = list(itertools.product(math_students, science_students, repeat=2))
        return combinations

# Usage example
classroom = ClassroomOrganizer()
combinations = classroom.seat_students()

for combination in combinations:
    print(combination)


#### GENERATORS REVIEW


def summa():
    yield 'Summa Cum Laude'

def magna():
    yield 'Magna Cum Laude'

def cum_laude():
    yield 'Cum Laude'

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()


def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1


days = 25
countdown_generator = (day for day in range(days, -1,-1))
grad_days = graduation_countdown(days)
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print("Days Left: " + str(day))


days = 25
gpas = [3.2, 4.0, 3.6, 2.9]
honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)




#### EVEN CORDINATOR

def read_guestlist(file_name):
    guests = {}
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
    return guests


def add_guest(name, age):
    guests[name] = age


def table_seats(table_number):
    foods = ["Chicken", "Beef", "Fish"]
    table = f"Table {table_number}"
    for seat in range(1, 6):
        yield (foods[seat - 1], table, f"Seat {seat}")


# Read the guest list
guests = read_guestlist("guest_list.txt")

# Add a new guest
add_guest("Jane", 35)

# Retrieve a generator of names for guests who are 21 and over
guests_21_and_over = (name for name, age in guests.items() if age >= 21)

# Print the names of guests who are 21 and over
for guest in guests_21_and_over:
    print(guest)

# Print meal and seat assignments for each table
for table_num in range(1, 4):
    print(f"Table {table_num}:")
    seat_assignments = table_seats(table_num)
    for guest, meal_seat in zip(guests_21_and_over, seat_assignments):
        print(f"{guest}: {meal_seat}")
    print()


### SETS REVIEW

music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Checkpoint 1
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Checkpoint 2
frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

# Checkpoint 3
regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

# Checkpoint 4
frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

# Checkpoint 5
regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)

### THE GREAT ROBOT RACE

from collections import deque, Counter, namedtuple
from time import sleep
from robot_race_functions import RobotRace

maze_file_name = "maze_data_1.csv"
seconds_between_turns = 1
max_turns = 100

# Create a namedtuple to keep track of our bot score data
BotScoreData = namedtuple('BotScoreData', ['name', 'num_moves', 'num_collisions', 'score'])

# Create a deque to store the robot moves
moves = deque()

# Create a RobotRace object
rr = RobotRace(maze_file_name)

# Initialize the maze data and robots
maze_data = rr.load_maze()
bots = rr.initialize_robots()

# Determine the number of robots in the race
num_robots = len(bots)

# Create a dict to easily access each robot object by its name
bot_data = {bot.name: bot for bot in bots}

# Main loop to simulate the robot race
turn = 0
while turn < max_turns and not rr.all_bots_reached_goal():
    turn += 1
    print(f"Turn {turn}:")

    # Calculate moves for each robot
    for bot in bots:
        if not bot.has_finished:
            walls = rr.get_surrounding_walls(bot)
            goal = rr.get_goal_coordinates()
            move = rr.compute_robot_logic(walls, goal, bot)
            moves.append(move)

    # Count the number of moves and collisions for each robot
    move_counts = Counter(move[0] for move in moves)
    collision_counts = Counter(move[0] for move in moves if move[2])

    # Print the number of moves and collisions for each robot
    for robot_name, move_count in move_counts.items():
        collision_count = collision_counts[robot_name]
        print(f"{robot_name}: {move_count} moves, {collision_count} collisions")

    # Process moves and update the maze
    while moves:
        move = moves.popleft()
        robot_name, action, has_collided = move
        bot = bot_data[robot_name]
        bot.process_move(action)

        # Update the maze characters based on the robot positions and print it to the console
        rr.update_maze_characters(maze_data, bots)
        rr.print_maze(maze_data)
        sleep(seconds_between_turns)

# Calculate the scores (moves + collisions) for each robot and append it to bot_scores
bot_scores = []
for bot in bots:
    move_count = move_counts[bot.name]
    collision_count = collision_counts[bot.name]
    score = move_count + collision_count
    bot_scores.append(BotScoreData(bot.name, move_count, collision_count, score))

# Print the final results
rr.print_results(bot_scores)


### ASHIAS GREETING

from contextlib import contextmanager


@contextmanager
def generic(card_type, sender_name, receiver):
    generic_template = f"{card_type}_generic.txt"
    new_card = f"{sender_name}_generic.txt"

    try:
        with open(generic_template, 'r') as generic_file, open(new_card, 'w') as new_card_file:
            content = generic_file.read()
            new_card_file.write(f"Dear {receiver}\n{content}\nSincerely, {sender_name}")
            yield new_card_file
    finally:
        print("Card Generated!")


class Personalized:
    def __init__(self, card_type, sender_name, receiver):
        self.card_type = card_type
        self.sender_name = sender_name
        self.receiver = receiver
        self.custom_file = None

    def __enter__(self):
        self.custom_file = open(f"{self.sender_name}_personalized.txt", "w")
        self.custom_file.write(f"Dear {self.receiver}\n")
        return self.custom_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.custom_file.write(f"Sincerely, {self.sender_name}\n")
        self.custom_file.close()

    def create_card(self, content):
        custom_content = f"{content}\n"
        self.custom_file.write(custom_content)


# Test for multiple orders
with generic("birthday", "Josiah", "Remy") as generic_card:
    print("Order for Generic Birthday Card")
    generic_card.write("Happy Birthday, Remy!")
    print("Generic Card Generated!")

with Personalized("birthday", "Josiah", "Esther") as personalized_card:
    print("\nOrder for Personalized Birthday Card")
    personalized_card.create_card("Happy Birthday!! I love you to the moon and back.")
    personalized_card.create_card("Even though you’re a pain sometimes, you’re a pain I can't live without.")
    personalized_card.create_card("I am incredibly proud of you and grateful to have you as a sister.")
    personalized_card.create_card("Cheers to 25!! You’re getting old!")
    print("Personalized Card Generated!")


