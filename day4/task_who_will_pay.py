#this is a task where we have to determine who will pay for the bill at a restront when a group of friends are at 
#restaurant we have the list of friends
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#one way is to use randit 
# random_person = random.randint(0, len(friends)-1)
# or other way is to use the choice function
random_p = random.choice(friends)
print(f"{random_p} will have to pay the bill")
