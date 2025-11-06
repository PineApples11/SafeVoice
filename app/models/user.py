from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime,func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default='user', nullable=False)
    display_name = Column(String(100), default='None')
    is_anonymous = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    last_login = Column(DateTime, default=None)

    reports = relationship("Report", back_populates="user")
    messages = relationship("Message", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"