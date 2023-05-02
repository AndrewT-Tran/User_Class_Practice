class users:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = "False"
        self.gold_card_points = 0

    def display_info(self):
        print("==========================")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==========================")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        if self.gold_card_points < 0:
            print("You don't have enough points.")
        return self


user1 = users("John", "Smith", "JSmith101@gmail.com", 35)
user2 = users("Mary", "Jane", "MaryJ420@gmail.com", 28)
user3 = users("SpongeBob", "SquarePants", "Spongebob@squarepants.com", 22)
# Have the first user spend 50 points
user1.enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
