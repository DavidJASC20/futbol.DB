'''
   Uses Flask to set up routes related to Project database
'''

import Project as my_db

from sqlalchemy.orm import sessionmaker

from flask import Flask, render_template, url_for, request, redirect



Session = sessionmaker(bind=my_db.engine)
session = Session()


#print(result_dict)

# use query with explicit fields for improved datatable
query2 = session.query(my_db.Club.id, my_db.Club.name, my_db.Club.badge)
results2 = query2.all()
result_dict2 = [u._asdict() for u in results2]



app = Flask(__name__)

app.config["SECRET_KEY"]='why_a_ball?'

#############################################################################################################
# default route redirected
@app.route("/")
def myredirect():
   return redirect(url_for('Project_datatable'))

##############################################################################################################
# route to datatable -- sorting and searching 
# note uses a different layout -- connects to jQuery JavaScript library
@app.route('/Project_datatable')
def Project_datatable():
   query = session.query(my_db.Club)
   results = query.all()

   result_dict = [u.__dict__ for u in results]
   return render_template('Project_datatable.html', title="Project Data Table", header="Project Data Table", futbol=result_dict)

###############################################################################################################
# route to gridjs datatable -- sorting and searching 
# note uses a different layout -- connects to gridjs 
# switched to query with explicit fields/columns no _sa_instance_state to worry about
@app.route('/Player_gridjs')
def Player_gridjs():

   query2 = session.query(my_db.Players.id, my_db.Players.playerName, my_db.Players.pos,my_db.Players.club_id)
   results2 = query2.all()
   result_dict2 = [u._asdict() for u in results2]
   columns = list(result_dict2[0].keys())
   #columns.remove('_sa_instance_state')
   print(columns)
   data = []
   for record in result_dict2:
      rowList = list(record.values())
      #rowList.pop(0)
      data.append(rowList)
   print(data)

   return render_template('Player_gridjs.html', 
                          title="Player Gridjs Data Table", 
                          header="Player Gridjs Data Table", columns=columns, data=data)

############################################################################################################
from Project_form import Club_insert
@app.route('/Club_insertt', methods=['GET', 'POST'])
def Club_insertt():
   form = Club_insert()
   print(form.validate_on_submit())
   # Keep around in case we encounter some validation issues
   if form.validate_on_submit():
   #if form.is_submitted():
      result = request.form
      
      a_club = my_db.Club(name= result["club_name"],badge = result["club_badge"],city=result["club_city"],country=result["club_country"])
      a_club.id=(result["club_id"])
      #a_club.plays_in = (result[" "])
      session.add(a_club)
      session.commit() 

      query = session.query(my_db.Club)
      results = query.all()
      result_dict = [u.__dict__ for u in results]
      return render_template('Project_datatable.html', title="After Insertion", header="After Insertion", futbol=result_dict)

   return render_template('Club_insertt.html', title="Insert Club Form", header="Insert Club Form", form=form)

# inserting a Player
from Project_form import Player_insert
@app.route('/Player_insertt', methods=['GET', 'POST'])
def Player_insertt():
   club_list = session.query(my_db.Club).all()
   club_choices = []
   for item in club_list:
      mylist=[]
      mylist.append(str(item.id))
      mylist.append("{}".format(item.name))
      my_tuple = tuple(mylist)
      club_choices.append(my_tuple)

   form = Player_insert()
   form.Club_id.choices=club_choices
   print(form.validate_on_submit())
   # Keep around in case we encounter some validation issues
   if form.validate_on_submit():
   #if form.is_submitted():
      result = request.form
      
      a_player = my_db.Players(playerName= result["playName"], pos = result["position"],number= result["num"], age = int(result["age"]))
      
      a_player.club_id = result["Club_id"]
      session.add(a_player)
      session.commit() 

      #query = session.query(my_db.Players)
      #results = query.all()
      #result_dict = [u.__dict__ for u in results] 


      #return render_template('Player_gridjs.html', title="After Insertion", header="After Insertion", futbol=result_dict)
      return redirect(url_for('Player_gridjs'))
   return render_template('Player_insertt.html', title="Insert Player Form", header="Insert Player Form", form=form)

if __name__ == "__main__":
   app.run(debug=True)   