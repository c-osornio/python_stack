class User:
    def __init__(self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

# Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"Hello {self.first_name} {self.last_name}! Email: {self.email} Age:  {self.age}")
        if self.is_rewards_member == True:
            print(f"Welcome back rewards member! You currently have {self.gold_card_points} points!")
        else:
            print(f"Ask us about our rewards program!")
        return self
# Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"Thank you for becoming a rewards member! You now have {self.gold_card_points} points!")
        else:
            print(f"WHOOPS! You are already enrolled in the rewards program.")
        return self

# have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
            print(f"Thank you for your purchase! You now have {self.gold_card_points} points left.")
        else: 
            print(f"Sorry, you dont have enough points.")
        return self

user1 = User("Carlos", "Osornio", "carlos@gmail.com",30)

user1.display_info().enroll().spend_points(50)
# user1.enroll()
# user1.spend_points(50)

user2 = User("Aidee", "Aguilar", "aidee@gmail.com",26)
user3 = User("Kai", "Osornio", "kai@gmail.com",1)

user1.spend_points(50)
user2.enroll().spend_points(80)
# user2.spend_points(80)

user1.display_info().enroll().display_info().spend_points(101)
user2.display_info()
user3.display_info().spend_points(40)

# user1.enroll()
# user1.display_info()
# user1.spend_points(101)

# user3.spend_points(40)
