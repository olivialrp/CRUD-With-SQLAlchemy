from pathlib import Path

from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

from werkzeug.security import generate_password_hash, check_password_hash

current_folder = Path(__file__).parent
PATH_TO_BD = current_folder / 'bd_users.sqlite'

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(30))
    admin_access: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"User({self.id=}, {self.name=})"
    
    def defines_password(self, password):
        self.password = generate_password_hash(password)

    def checks_password(self, password):
        return check_password_hash(self.password, password)

    
engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine)

# CRUD -------------------

def creates_users(
        name,
        password,
        email,
        **kwargs
):
    with Session(bind=engine) as session:
        user = User(
            name= name,
            email= email,
            **kwargs
        )
        user.defines_password(password)
        session.add(user)
        session.commit()

def reads_all_users():
    with Session(bind=engine) as session:
        command_sql = select(User)
        users = session.execute(command_sql).fetchall()
        users = [user[0] for user in users]
        return users 
    
def reads_user_by_id():
    with Session(bind=engine) as session:
        command_sql = select(User).filter_by(id=id)
        users = session.execute(command_sql).fetchall()
        return users[0][0]
    
def updates_user(
        id,
        **kwargs
        ):
    with Session(bind=engine) as session:
        command_sql= select(User).filter_by(id=id)
        users = session.execute(command_sql).fetchall()
        for user in users:
            for key, value in kwargs.items():
                if key == 'password':
                    user[0].defines_password(value)
                else: 
                    setattr(user[0], key, value)
        session.commit()

def deletes_user(id):
    with Session(bind=engine) as session:
        command_sql= select(User).filter_by(id=id)
        users = session.execute(command_sql).fetchall()
        for user in users:
            session.delete(user[0])
        session.commit()


if __name__ == '__main__':
    creates_users(
        'jhon does cousin',
        password= 'doessecretpassword',
        email= 'doesmail.com',
        admin_access= True,
    )

#   users = reads_all_users()
#   user_0 = users[0]
#   print(user_0)
#  to read some specific item, type .desiredItem, example: print(user_0.password, user_0.email)

#  user_jhon = reads_user_by_id(id=1)
#  print(user_jhon)
#  print(user_jhon.name, user_jhon.email)

# updates_user(id=1, email = 'newemail.com', password = 'newdoespassword')

#  creates_users(
#      'Jhon Doe',
#      password='doessecretpassword',
#      email='doesmail.com'
#  )