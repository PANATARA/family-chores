from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, ForeignKey

from core.models import Base


class UserBase(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(60))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    date_of_birth: Mapped[Optional[Date]] = mapped_column(Date, nullable=True)

    family_id: Mapped[int] = mapped_column(ForeignKey("Family.id"), nullable=True)
    family: Mapped["Family"] = relationship("Family", back_populates="members") # type: ignore
