from sqlalchemy import  ForeignKey,func
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from app.extensions import db  



class Message(db.Model,SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), ForeignKey('users.id'), nullable=False)
    is_anonymous = db.Column(db.Boolean(), default=False)
    receiver_type = db.Column(db.Enum("admin","support","user", name="receiver_types"), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    is_read = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)

    user = relationship("User", back_populates="messages")

    def __repr__(self):
        return f"<Message(id={self.id}, user_id={self.user_id}, receiver_type='{self.receiver_type}', is_read={self.is_read})>"

