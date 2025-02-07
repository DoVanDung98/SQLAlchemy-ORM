from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)

class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="address")

    def __repr__(self):
        return f"<Address(id)={self.id}, city='{self.city}>"
    


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String)
    age = Column(Integer)
    address: Mapped[list["Address"]] = relationship()

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.name}')>"

Base.metadata.create_all(engine)