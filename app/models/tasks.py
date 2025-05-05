
import datetime
from sqlalchemy import Date, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from app.models.users import User

class Task(db.Model):
    __tablename__ = 'tasks'  # needed, otherwise it would generate a table "user" (lowercase of class name).
    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column()
    deadline: Mapped[str] = mapped_column()
    priority: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    __table_args__ = (
        CheckConstraint('priority BETWEEN 1 AND 5', name='priority_range'),
    )
