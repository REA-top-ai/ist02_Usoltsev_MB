from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.dialects.postgresql import JSONB

from datetime import datetime

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    history: Mapped[list['History']] = relationship(back_populates='user')



class GithubUser(Base):
    __tablename__ = 'github_users'

    username: Mapped[str] = mapped_column(primary_key=True)
    data: Mapped[dict] = mapped_column(JSONB)
    resume: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())


class History(Base):
    __tablename__ = 'history'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    user: Mapped['User'] = relationship(back_populates='history')


