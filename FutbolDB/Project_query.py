import Project as my_db

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Session = sessionmaker(bind=my_db.engine)
session = Session()


print("")
print("")
query = session.query(my_db.Players)
results = query.all()
for item in results:
   print ("id={} player name={} player number={} ".format(item.id, item.playerName, item.number))

print("")
""" print("")
query = session.query(my_db.Club.name, my_db.Club.city)
#default output now named tuples
results = query.all()
for item in results:
   print(item)
   print(item.name) 
   print(item[0])
   print(item._asdict()) """

first_club = session.query(my_db.Club).first()
print("{} plays in ".format(first_club.name))
for club in first_club.plays_in:
   print(club.compName)
print("")

query = session.query(my_db.Players.playerName).filter(my_db.Players.pos == "CAM")
results = query.all()
for item in results:
   print ("These players play CAM: {}".format(item)) 

print("\n join \n")
myjoin = session.query(my_db.Club, my_db.Players).filter(my_db.Club.id == my_db.Players.club_id).all()
for row in myjoin:
   print("{}: {}".format(row.Club.name, row.Players.playerName))

print("\n double jointed \n")
myjoin = session.query(my_db.Club, my_db.comp_table, my_db.Comp).filter(my_db.Club.id == my_db.comp_table.c.club_id).filter(my_db.Comp.id == my_db.comp_table.c.comp_id).all()
for row in myjoin:
   print("{}: {}".format(row.Club.name, row.Comp.compName))

