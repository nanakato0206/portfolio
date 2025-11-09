from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Task(Base):
    __tablename__ = "tasks"  

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, index=True)                   
    price = Column(Float)                               
    description = Column(String, nullable=True)        
