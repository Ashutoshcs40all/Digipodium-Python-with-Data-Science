from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

from app import Medicine_Name
Base = declarative_base()

class Medicine(Base):
    __tablename__ = "Search Medicine"
Medicine_Name = Column( String, primary_key=True,autoincrement= True)
Medicine_Stock = Column(String)