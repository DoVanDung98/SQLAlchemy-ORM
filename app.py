import random
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


names = ["Andrew Pip", "Iron Man", "John Doe", "Jane Doe"]
ages = [20, 21, 22, 23, 25, 27, 35, 60]

# query all users
users = session.query(User).all()

# query all users with age greater than or equal to 25
user_filtered = session.query(User).filter(User.age>=25).all()
for user in user_filtered:
    print(f"User name: {user.name}, age: {user.age}, id: {user.id}")

print("All users: ", len(users))
print("Filtered Users: ", len(user_filtered))

# query all users with age is equal to 30
users = session.query(User).filter_by(age=35).all()
for user in users:
    print(f"User name: {user.name}, age: {user.age}, id: {user.id}")