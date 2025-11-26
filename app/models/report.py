from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from app.extensions import db

class Report(db.Model,SerializerMixin):
    __tablename__ = 'reports'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), ForeignKey('users.id'),nullable=True)
    abuse_type = db.Column(db.Enum("physical","mental","emotional",name="abuse_types"), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    is_anonymous = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    

    user = relationship("User", back_populates="reports")

    def __repr__(self):
        return f"<Report(id={self.id}, user_id={self.user_id}, abuse_type='{self.abuse_type}', is_anonymous={self.is_anonymous})>"
    
