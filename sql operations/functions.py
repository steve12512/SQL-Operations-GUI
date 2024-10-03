from sqlite3 import IntegrityError
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from window.gui import create_window, display_message
from database.setup_db import set_db, search_for_user, User

def create_new_user(session):
    #this function creates a new user in the database. a window opens and lets the user define the input data
    #then a new user object is created, which is then passed to the session object, which then commits it to the database

    operation = 'create_user'
    #this function creates the window for user creation store the user's data in a dictionary
    user_data = create_window(operation)

    if 'username' in user_data:
        try:
        #create a new user object
            user = User(
                    username = user_data['username'],
                    password = user_data['password'],
                    email = user_data['email'],
                    full_name = user_data['full_name']
                )  
            
            #add the new user to the session and commit to the database
            session.add(user)
            session.commit()
            info = (
            f"User Information\n"
            f"Username: {user_data['username']}\n"
            f"Password: {user_data['password']}\n"
            f"Email: {user_data['email']}\n"
            f"Full Name: {user_data['full_name']}"
        )
            title = 'Created user'
            #print(f"User {username} created successfully.")
            
        except IntegrityError as e:
            #handle cases where the username or email already exists
            session.rollback()  #rollback the transaction on error
            title = 'Could not create User'
            info = (f"Integrity error, username or email adress already exists : {str(e)}")
            
        except Exception as e:
            #handle other potential exceptions
            session.rollback()
            title = 'Could not create User'
            info = (f"An unexpected error occurred: {str(e)}")
        finally:
            session.close()  #close the session
            display_message(operation, info, title)


def find_user(session):
    #this function will read a user id(primary key, int) from the user of the app, and then proceed to search through the dabatase, by using the session object, and try to find the user through his primary key.

    operation = 'find_user'
    user_data = create_window(operation) #get a dictionary containig user id
    
    #search for the user in the db, using our dictionary
    info, title = search_for_user(session, user_data)

    display_message(operation, info, title)



def update_email(session):
    #this function reads a user id (int) and an email adress (string) from the create window function(which enables the type onto the screen). if the user is found through his primary key(id) then his new email adress replaces his previous one, if they are different of course.
    operation = 'update_email'

    #read the user id and the new email address through our gui, and save them in a dictionary
    user_data = create_window(operation)

    try:
        #search for the user in the db
        user = session.query(User).filter_by(id = user_data['user_id']).first()
        
        if user:
        #if the user exists, check if the new email is different from the current email
            if user.email != user_data['new_email']:
                user.email = user_data['new_email']
                session.commit()
                info = f"Email for user ID {user_data['user_id']} updated successfully to {user_data['new_email']}."
                title = 'Updated successfuly.'
            else: 
                #else the user has given the same email
                info = f"The new email address is the same as the current one for user ID {user_data['user_id']}."
                title = 'Same email adress given.'
        else:
            info = f"User with ID {user_data['user_id']} not found."
            title = 'User not found'
                    
    except Exception as e:
        #handle unexpected errors
        info = f"An error occurred while updating user email: {str(e)}"
        
    finally:
        session.close()  #ensure the session is closed
        display_message(operation, info, title)



def delete_user(session):
     #this function reads a user id (int) and proceeds to delete the user from the user table in the db through the sesion object
    operation = 'delete_user'
    
    #create the window to get a dictionary containing the user id
    user_data = create_window(operation)
    
    try:
        
        #query to find and delete the user
        user = session.query(User).filter_by(id = user_data['user_id']).first()
            
        if user: 
            #if the user is found
            session.delete(user)  #delete the user
            session.commit()  #commit the transaction
            info = f"User with ID {user_data['user_id']} deleted successfully."
            title = 'User Deleted'
            
        else:
            #if the user is not found
            info = f"User with ID {user_data['user_id']} not found."
            title = 'User Not Found'
            
    except Exception as e:
        #in case we encounter random exception
        info = f"User with ID {user_data['user_id']} not found."
        title = 'User Not Found'

    finally:
        session.close()
        #display the result
        display_message(operation, info, title)
