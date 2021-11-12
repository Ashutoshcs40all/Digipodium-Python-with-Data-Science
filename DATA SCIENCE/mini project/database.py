from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class Medicine(Base):
   id = Column( Integer, primary_key=True,autoincrement= True) 
   Invoice_Date = Column(Integer)
   Customer_Name = Column(String)
   Medicine_Name = Column(String)
   Manufectore = Column(Integer)
   Puraches_Date = Column(Integer)
   Medicine_Stock = Column(String)
   Return_Date = Column(Integer)
  