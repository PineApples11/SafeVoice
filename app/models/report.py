from sqlalchemy import Column, Integer, Boolean, Enum, Text, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey('users.id'),nullable=True)
    abuse_type = Column(Enum("physical","mental","emotional",name="abuse_types"), nullable=False, enumerated=True)
    description = Column(Text(), nullable=True)
    is_anonymous = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    

    user = relationship("User", back_populates="reports")

    def __repr__(self):
        return f"<Report(id={self.id}, user_id={self.user_id}, abuse_type='{self.abuse_type}', is_anonymous={self.is_anonymous})>"
    
