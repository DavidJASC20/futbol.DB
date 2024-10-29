# WTF using flask wt-forms

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Length
#from wtforms.ext.sqlalchemy.fields import QuerySelectField

   
class Club_insert(FlaskForm):

   club_id = StringField("Club ID",validators=[InputRequired(message="You must enter a ID"), Length(min=2, max=4, message="Title length must be between 2 and 4 characters")], 
   default="ZERO")

   club_name = StringField("Club Name",validators=[InputRequired(message="You must enter a Name")])
   club_badge = StringField("Club Badge")  
   club_city = StringField("Club City",validators=[InputRequired(message="You must enter a City")])
   club_country = StringField("Club Country")
   
   
   submit = SubmitField("Insert Club")
   
class Player_insert(FlaskForm):

   playName = StringField("Player Name", 
   validators=[InputRequired(message="You must enter a Name"), 
   Length(min=2, max=60, message="First Name length must be between 2 and 60 characters")])
   
   position = SelectField("Position", choices=[('ST', 'ST'),
   ('LW','LW'),('RW','RW'),('CAM','CAM'),('CM','CM'),('CDM','CDM'),
   ('CB','CB'),('RB','RB'),('LB','LB'),('GK','GK')],
   validators=[InputRequired(message="You must choose a postion")])

   num = StringField("Player Number", default="#")

   age = IntegerField("Player Age")


   Club_id = SelectField("Club ID ")
   
   submit = SubmitField("Insert Player")