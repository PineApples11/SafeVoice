from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from app.extensions import db



class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='user', nullable=False)
    display_name = db.Column(db.String(100), default='None')
    is_anonymous = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    last_login = db.Column(db.DateTime, default=None)

    reports = relationship("Report", back_populates="user")
    messages = relationship("Message", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"