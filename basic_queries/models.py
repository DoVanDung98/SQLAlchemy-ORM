from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)
