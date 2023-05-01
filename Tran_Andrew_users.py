class Users:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = "False"
        self.gold_card_points = 0


def display_info(self):
    print(f"Name: {self.first_name} {self.last_name}")
    print(f"Email: {self.email}")
    print(f"Age: {self.age}")
    print(f"Reward Member: {self.is_rewards_member}")
    print(f"Gold Card Points: {self.gold_card_points}")


def enroll(self):
    self.is_rewards_member = True
    self.gold_card_points = 200


def spend_points(self, amount):
    self.gold_card_points -= amount


user1 = Users("John", "Smith", "JSmith101@gmail.com", 35)
# Have the first user spend 50 points
spend_points(user1, 50)
print(display_info(user1))

user2 = Users("Mary", "Jane", "MaryJ420@gmail.com", 28)
# Have the second user enroll
enroll(user2)
# have teh second user spend 80 points
spend_points(user2, 80)
print(display_info(user2))

user3 = Users("SpongeBob", "SquarePants", "Spongebob@squarepants.com", 22)


# Call the display method on all the users.
display_info(user1)
display_info(user2)
display_info(user3)
