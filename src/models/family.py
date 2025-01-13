from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String

from core.models import Base


class FamilyBase(Base):
    __tablename__ = "Family"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(60))
    slogan: Mapped[str] = mapped_column(String(300))

    members: Mapped[list["User"]] = relationship("User", back_populates="family") # type: ignore
