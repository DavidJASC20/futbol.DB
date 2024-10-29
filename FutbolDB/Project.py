from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
#from sqlalchemy import func

engine = create_engine('sqlite:///./futbol.db')
#engine = create_engine('sqlite:///')
Base = declarative_base()



comp_table = Table('comp_table', Base.metadata,
    Column('club_id', String, ForeignKey('club.id')),
    Column('comp_id', Integer, ForeignKey('comp.id'))
)

#################################################################
# 
class Club(Base):
   __tablename__ = 'club'
   
   id = Column(String, primary_key=True)
   name = Column(String)
   badge = Column(String)
   city = Column(String)
   country = Column(String)
   players = relationship("Players") # note relationship added to imports above
   plays_in = relationship("Comp", secondary=comp_table, viewonly=True)
#################################################################
#   
class Players(Base):
   __tablename__ = 'players'
   
   id = Column(Integer, primary_key=True)
   playerName = Column(String)
   pos = Column(String)
   number = Column(String)
   age =  Column(Integer)
   club_id = Column(String, ForeignKey('club.id'))
 

#################################################################

class Comp(Base):
   __tablename__ = 'comp'
   
   id = Column(Integer, primary_key=True)
   compName = Column(String)
   most = Column(String)
   hosts = relationship("Club", secondary=comp_table, viewonly=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Manchester United and Manchester City are both in Champions League
session.execute(comp_table.insert().values([("MU", 1), ("MC", 1)]))
session.commit()
# Real Madrid are in the Champions League
session.execute(comp_table.insert().values([("RM", 1)]))
session.commit()
# Napoli play in Serie A and Champions League 
session.execute(comp_table.insert().values([("SCN", 1), ("SCN", 7)]))
session.commit()
# Crystal Palace are in the Premier League
session.execute(comp_table.insert().values([("CPFC", 4)]))
session.commit()