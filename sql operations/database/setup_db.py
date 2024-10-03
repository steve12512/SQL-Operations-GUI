import hashlib
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#this file is responsible for setting up our connection to the database

#define a User Class Model used in the relational database. to do that, we have to initialize base class for the model
Base = declarative_base()


def set_db():
    #this function ini

    #database URL example
    DATABASE_URL = 'sqlite:///:memory:'  

    #create the database engine
    engine = create_engine(DATABASE_URL)

    #create our classes in the database
    Base.metadata.create_all(bind= engine)

    #create a configured "Session" class
    Session = sessionmaker(bind=engine)

    #create a Session instance
    session = Session()
    return session




class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)

    def __init__(self,username, password, email, full_name):
        #constructor
        self.username = username
        self.password = hash_password(password)
        self.email = email
        self.full_name = full_name
    
    def __repr__(self):
        #tostring method
        return f"({self.id}) {self.username} {self.email}"


def hash_password(password):
    #use a secure hashing algorithm to store passwords
    return hashlib.sha256(password.encode()).hexdigest()

def search_for_user(session, user_data):
    #this function takes as parameters a session object in order to establish communication with a database, as well as a dictionary containing user data
    #it connects to the db, searches for the user, and returns appropriate info
     #if we have successfully retrieved the dictionary of values
    
    if 'user_id' in user_data:
        user_id = user_data['user_id']
        try:
            #query the database for the user with the specified user_id
            user = session.query(User).filter_by(id = user_id).first()
            
            if user:
                #return user information as a dictionary
                 info = {
                    'id': user.id,
                    'username': user.username,
                    'password': user.password,
                    'email': user.email,
                    'full_name': user.full_name
                }
                 title = 'User found'
            else:
                #user not found
                info = "User with ID {user_id} not found."
                title = 'User not found'
        except Exception as e:
            #handle unexpected errors
            info = "An error occurred while retrieving user data: {e}"
            info = str(info)
            title = 'Error'
        return info, title