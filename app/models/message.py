from sqlalchemy import Column, Text, Boolean, Integer, ForeignKey, DateTime, func, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()

class Message(Base,SerializerMixin):
    __tablename__ = 'messages'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    is_anonymous = Column(Boolean(), default=False)
    receiver_type = Column(Enum("admin","support","user", name="receiver_types"), nullable=False)
    content = Column(Text(), nullable=False)
    is_read = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    user = relationship("User", back_populates="messages")

    def __repr__(self):
        return f"<Message(id={self.id}, user_id={self.user_id}, receiver_type='{self.receiver_type}', is_read={self.is_read})>"

