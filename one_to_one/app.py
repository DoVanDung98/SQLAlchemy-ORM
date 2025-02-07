from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address", back_populates="user", uselist=False)


class Address(Base):
    __tablename__="address"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="address")


Base.metadata.create_all(engine)

new_user = User(name="dungdv34")
new_address = Address(email="kspmvandung@gmail.com", user=new_user)
session.add(new_user)
session.add(new_address)
session.commit()


# print(new_user.name)
# print(new_address.email)
# print(new_user.address.email)
# print(new_address.user.name)

user = session.query(User).filter_by(name="John Doe").first()
print(f"User: {user.name}, Address: {user.address.email}")