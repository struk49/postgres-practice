from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)




# instead of connecting the database directly, we will ask for session
# create a new instance of seesionmaker, then point to our engine( the db)
Session = sessionmaker(db)
# open an  actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records for our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

# creating records for our Programmer table
alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

# creating records for our Programmer table
grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL Language"
)

# creating records for our Programmer table
margraret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

# creating records for our Programmer table
bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

# creating records for our Programmer table
tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

# creating records for our Programmer table
andrew_struk = Programmer(
    first_name = "Andrew",
    last_name = "Struk",
    gender = "M",
    nationality = "British",
    famous_for = "Wannabe Web Developer"
)

# add a instance of our programmers to our session
#session.add(ada_lovelace)
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margraret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)
session.add(andrew_struk)

# commit our session to the database
session.commit()

# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "

    )


