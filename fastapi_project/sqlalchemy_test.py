from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine("sqlite:///sqlalchemy.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="Илья", age=16)
    session.add(user)
    session.commit()
    print("Добавлен:", user.name, user.age)