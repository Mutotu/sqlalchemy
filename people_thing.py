from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()

class Person(Base):
    __tablename__ = "people"
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn} {self.firstname} {self.lastname} {self.gender} {self.age})"


class Thing(Base):
    __tablename__ = "things"
    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid} {self.description} {self.owner})"



engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

person1 = Person(12321, "Mike1", "Job", "m", 44)
person2 = Person(22321, "Mike12", "Job2", "m", 14)
person3 = Person(32321, "Mike11", "Job3", "m", 34)
session.add(person1)
session.add(person2)
session.add(person3)
session.commit()

# result = session.query(Person).all()
# result = session.query(Person).filter(Person.lastname == "Job")
# for r in result:
#     print(r)

t1 = Thing(16, "Car", person1.ssn)
t2 = Thing(15, "Lol", person3.ssn)
t3 = Thing(14, "Car2", person2.ssn)
t4 = Thing(13, "Car3", person1.ssn)
t5 = Thing(12, "Car4", person3.ssn)
session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()
result = session.query(Thing, Person).filter(Thing.owner == Person.ssn).all()
print(result)