from sqlalchemy import Column, Integer, String,ARRAY, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    village_name = Column("villageName", String, index=True)
    role = Column(String, index=True)
    village_id = Column("villageId", Integer, index=True)
    phone = Column(String, unique=True, index=True)
    galli_name = Column("GalliName", ARRAY(String), index=True)

def create_tables():
    DATABASE_URL = "postgresql://postgres:1234@127.0.0.1:5432/postgres"
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
