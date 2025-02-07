from models import Address, session, User

user1 = User(name="John Doe", age=52)
user2 = User(name="Jane Smith", age=34)


# Creating address
address1 = Address(city="New York", state="NY", zip_code="10001")
address2 = Address(city="Los Angeles", state="NY", zip_code="90001")
address3 = Address(city="Chicaggo", state="NY", zip_code="60601")

# Associating address with users
user1.address.extend([address1, address2])
user2.address.append(address3)

# Adding users and addresses to the session and committing changes to the database
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.address = }")
print(f"{user2.address = }")
print(f"{address1.user}")