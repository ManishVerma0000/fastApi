from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User, create_tables


# Create a session factory
DATABASE_URL = "postgresql://postgres:1234@127.0.0.1:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def userLogin(logindetails):
    print(logindetails)
    session = SessionLocal()
    user = session.query(User).filter(User.village_id == logindetails.villageId, User.phone == logindetails.phone).first()
    if user:
        return {'hello from the services part',user}

def registerUser(user):
    name = user.name
    village_name = user.villageName
    role = user.role
    village_id = user.villageId
    phone = user.phone
    galli_name=user.galli_name
    insert_user(name, village_name, role, village_id, phone,galli_name)
    return f"User {name} registered successfully."
def insert_user(name: str, village_name: str, role: str, village_id: int, phone: str,galli_name:list[str]):
    session = SessionLocal()
    try:
        new_user = User(name=name, village_name=village_name, role=role, village_id=village_id, phone=phone,galli_name=galli_name)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        print(f"User {new_user.name} with phone {new_user.phone} added.")
    except Exception as e:
        session.rollback()
        print("Failed to insert user", e)
    finally:
        session.close()


