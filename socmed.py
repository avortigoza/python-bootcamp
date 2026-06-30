class User:
    def __init__(self, firstName, lastName, likesCount, friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName
        print(f"User created: {self.firstName}")

    def introduce(self):
        print(f"Hi, I am {self.firstName} {self.lastName}.")

    def fullProfile(self):
        print(f"Full name: {self.firstName} {self.lastName}. \nLikes: {str(self.likesCount)}")
        print("Friends: ")
        for friend in self.friendsName:
            print(f"{friend}")

friends = ["Jun", "Anpaul", "Paulo", "Eugene"]
userOne = User("Areanne", "Ortigoza", 100, friends)
userOne.introduce()
userOne.fullProfile()
