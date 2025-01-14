import bcrypt
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, ForeignKey, Integer

from core.models import Base


class UserBase(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(60), unique=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    # Внешний ключ для связи с Family
    family_id: Mapped[Optional[int]] = mapped_column(ForeignKey("Family.id"), nullable=True)

    # Связь с семьей
    family: Mapped["FamilyBase"] = relationship("FamilyBase", back_populates="members") # type: ignore

    password: Mapped[str]
    token: Mapped[str] = mapped_column(nullable=True)

    def set_password(self, raw_password: str) -> None:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), salt)
        self.password = hashed_password.decode('utf-8')

    def check_password(self, raw_password: str) -> bool:
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))