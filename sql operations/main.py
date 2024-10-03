from functions import *

#this is our main file
#first, let us set up a way to communicate with our database, using a session object
session = set_db()

#now let us create a window, for the user to select which function he/she wants to use
#save the desired user task
task = create_window('start_app')

if task == 'Create New User':
    #create new user
    create_new_user(session)

elif task == 'Find User':
    #find user
    find_user(session)
elif task == 'Update Email':
    update_email(session)
elif task == 'Delete User':
    delete_user(session)