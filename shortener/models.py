from sqlalchemy.orm import DeclarativeBase as Base, Mapped, mapped_column
from sqlalchemy import String
import datetime

class Url(Base):

    __tablename__ = "url"

    id: Mapped[int] = mapped_column(primary_key=True)
    short_url: Mapped[str] = mapped_column(String(5))
    long_url: Mapped[str] = mapped_column(String(2000))
    created: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now(datetime.UTC))

    def __repr__(self) -> str:
        return f"URL(id={self.id!r}, short_url={self.short_url!r}, long_url={self.long_url!r})"