import logging

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


logger = logging.getLogger("logger")

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()


def db_session() -> Session:
    try:
        db: Session = SessionLocal()
        yield db
    except Exception:
        logger.critical("DB is down", exc_info=True)
    finally:
        db.close()


class CRUDMixin(object):
    """
    Helper class with CRUD utilities
    """

    @classmethod
    def create(cls, db: Session, commit=True, **kwargs):
        instance = cls(**kwargs)
        return instance.save(db, commit=commit)

    def save(self, db: Session, commit=True):
        db.add(self)

        if commit:
            db.commit()
        else:
            db.flush()
            db.refresh(self)

        return self

    @classmethod
    def get_by_id(cls, db: Session, id):
        return db.query(cls).filter(cls.id == id).first()

    def update(self, db: Session, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

        return commit and self.save(db) or self

    def delete(self, db: Session, commit=True):
        """Hard delete from DB"""
        db.delete(self)
        return commit and db.commit()


class Comment(Base, CRUDMixin):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    url = Column(String)
    key = Column(String)
    Comment = Column(String)
