from db.database import Base 
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(25), unique=True)
    user_email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_activate = Column(Boolean, default=False) 
    orders = relationship('Orders', back_populates='user')
    
    def __repr__(self):
        return f'<User {self.user_name}'


class Order(Base):
    
    ORDER_STATUSES = (
        ('PENDING', 'pending'), 
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    )
    
    PIZZA_SIZE = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'), 
        ('LARGE', 'large'), 
        ('EXTRA-LARGE', 'extra-large')
    )
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=True)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default='PENDING')
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZE), default='SMALL')
    
    flavour = Column(String(25), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_activate = Column(Boolean, default=False) 
    user_id = Column(Integer, ForeignKey('user.id'))
    user=relationship('User', back_populates='orders')
    
    
    def __repr__(self):
        return f'<Order {self.id}'