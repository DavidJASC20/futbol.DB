import Project as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()


#################################################################
# initially populate database tables from a JSON file 
import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('static/data/Club.json') as f:
   FC_club = json.load(f)

# to have access to the list element and its index 
# you can use enumerate
for i, club in enumerate(FC_club["football_clubs"]):
   a_club = my_db.Club(id=club["club_id"], name=club["club_name"], badge=club["club_badge"], 
   city=club["city"],country=club["country"]) 
   session.add(a_club)
   session.flush() 
   
with open('static/data/Players.json') as f:
   players_data = json.load(f)

for i, players in enumerate(players_data["football_players"]):
   a_player = my_db.Players(club_id=players["club_id"],playerName=players["player_name"], pos=players["player_pos"], number=players["player_num"], 
   age=int(players["player_age"])) 
   session.add(a_player)
   session.flush()  

with open('static/data/Comp.json') as f:
   comp_data = json.load(f)

for i, comp in enumerate(comp_data["football_comp"]):
   a_comp = my_db.Comp(compName=comp["comp_name"], most=comp["most_wins"]) 
   session.add(a_comp)
   session.flush()   
   session.commit()


