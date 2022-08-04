from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    items = relationship("Items", back_populates="owner")

class Items(Base):
    __tablename__="Items"

    id = Column(Integer, primary_key=True, index=True)
    title= Column(String, nullable=False, unique=True)
    description = Column(String)
    owner_id= Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")