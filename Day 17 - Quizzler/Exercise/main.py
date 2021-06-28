
#create a class, always in Pascal Case  ThisIsPasacalCase
#attributes are variables that a class has
#methods are functions that a class can use
class User:

    #initalize a class by using def __init__(self) function, you must initialize a class
    def __init__(self, user_id, username, name, password):
        self.id = user_id
        self.username = username
        self.name = name.capitalize()
        self.password = password
        self.followers = 0
        self.following = 0

    #when creating methods, the function (method) always has to have "self" as the first parameter
    def follow(self, user):
        #The user that we are following, their follower count goes up by one
        user.followers += 1
        #Our own following count (SELF, OURSELF) goes up when we follow a user(the second parameter) using this method (function)
        self.following += 1

user_1 = User(
    "01",
    "Lludu",
    "Andrew",
    "myPasswordIsGreat",
)

user_2 = User(
    "02",
    "Beeewoop",
    "Bobbert",
    "drowssap",
)


print(f'\n{user_1.username} has {user_1.followers} followers, and is following {user_1.following} users.')
print(f'{user_2.username} has {user_2.followers} followers, and is following {user_2.following} users.')
print(f'{user_1.username} has clicked follow on {user_2.username}.')
user_1.follow(user_2)

print(f'\n{user_1.username} has {user_1.followers} followers, and is following {user_1.following} users.')
print(f'{user_2.username} has {user_2.followers} followers, and is following {user_2.following} users.')

