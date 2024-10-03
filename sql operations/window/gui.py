import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def create_window(operation):
    #this function creates a window so that the user can perform an operation
    #if the operation == create user, the data is sent back to the main method of the father directory
    #before that, the data is passed on to the show form method which confirms it on another window
    #if it the operation == find user,


    #variables to store user inputs
    user_data = {'username': '', 'password': '', 'email': '', 'full_name': ''}

    def submit_form():
        if operation == 'create_user':
            # Get data from the entry fields
            user_data['username'] = username_entry.get()
            user_data['password'] = password_entry.get()
            user_data['email'] = email_entry.get()
            user_data['full_name'] = full_name_entry.get()

        elif operation == 'find_user':
            user_data['user_id'] = user_id_entry.get()

        elif operation == 'update_email':
            user_data['new_email'] = email_entry.get()
            user_data['user_id'] = user_id_entry.get()

        elif operation == 'delete_user':
            user_data['user_id'] = user_id_entry.get()
        display_message(operation, user_data, '')
        root.destroy()


    def handle_option(option):
        nonlocal user_data
        user_data = option
        root.destroy()


    #create the main window
    root = tk.Tk()
    root.title("Create New User")
    
    #set the size of the window
    root.geometry('1024x720')  #width x height in pixels
    
    #set the background color of the window
    root.configure(bg='lightblue')
    

    #load and set the background image
    try:
        image = Image.open('window/resources/background.jpg')  #replace with your image file path
        background_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)
        #keep a reference to the image to prevent it from being garbage collected
        background_label.image = background_image
    except Exception as e:
        print(f"Error loading image: {e}")
        
    if operation == 'create_user':
        root.title("Create New User")
        #create and place the label
        label = tk.Label(root, text="Please create a new user", bg='lightblue')
        label.pack(pady=10)

        #create and place the username input
        tk.Label(root, text="Username:", bg='lightblue').pack(pady=5)
        username_entry = tk.Entry(root)
        username_entry.pack(pady=5)

        #create and place the password input
        tk.Label(root, text="Password:", bg='lightblue').pack(pady=5)
        password_entry = tk.Entry(root, show="*")  #`show="*"` hides the password input
        password_entry.pack(pady=5)

        #create and place the email address input
        tk.Label(root, text="Email Address:", bg='lightblue').pack(pady=5)
        email_entry = tk.Entry(root)
        email_entry.pack(pady=5)

        #create and place the full name input
        tk.Label(root, text="Full Name:", bg='lightblue').pack(pady=5)
        full_name_entry = tk.Entry(root)
        full_name_entry.pack(pady=5)

            
    elif operation == 'find_user':
        root.title("Find User")
        label = tk.Label(root, text="Please provide the user id that you are searching for", bg='lightblue')
        label.pack(pady=10)

        tk.Label(root, text="User id:", bg='lightblue').pack(pady=5)
        user_id_entry = tk.Entry(root)
        user_id_entry.pack(pady=5)

    elif operation == 'update_email':
        root.title("Update email")
        label = tk.Label(root, text="Please provide the user id that you are searching for, and the new email adress", bg='lightblue')
        label.pack(pady=10)

        tk.Label(root, text="User id:", bg='lightblue').pack(pady=5)
        user_id_entry = tk.Entry(root)
        user_id_entry.pack(pady=5)

        #create and place the email address input
        tk.Label(root, text="Email Address:", bg='lightblue').pack(pady=5)
        email_entry = tk.Entry(root)
        email_entry.pack(pady=5)
    
    elif operation == 'delete_user':
        root.title("Update email")
        label = tk.Label(root, text="Please provide the id of the user you want to delete", bg='lightblue')
        label.pack(pady=10)

        tk.Label(root, text="User id:", bg='lightblue').pack(pady=5)
        user_id_entry = tk.Entry(root)
        user_id_entry.pack(pady=5)
      
    else:
        #if we are initializing our app
        #configure the grid layout
        for i in range(3):
            root.grid_rowconfigure(i, weight=1)
        for i in range(3):
            root.grid_columnconfigure(i, weight=1)

        #create and place the options using a grid layout
        tk.Label(root, text="Select an operation", bg='lightblue').grid(row=0, column=1, pady=20, padx=20, columnspan=1, sticky='n')

        # Create and place the buttons in a symmetrical layout
        tk.Button(root, text="Create New User", command=lambda: handle_option('Create New User')).grid(row=1, column=0, padx=40, pady=20, sticky='ew')
        tk.Button(root, text="Read User Info", command=lambda: handle_option('Find User')).grid(row=1, column=2, padx=40, pady=20, sticky='ew')
        tk.Button(root, text="Update Email", command=lambda: handle_option('Update Email')).grid(row=2, column=0, padx=40, pady=20, sticky='ew')
        tk.Button(root, text="Delete User", command=lambda: handle_option('Delete User')).grid(row=2, column=2, padx=40, pady=20, sticky='ew')

    #create and place the submit button if 
    if operation in ['create_user', 'find_user', 'update_email', 'delete_user']:
        submit_button = tk.Button(root, text="Submit", command=submit_form)
        submit_button.pack(pady=20)
    #run the application
    root.mainloop()
    return user_data



def display_message(operation, user_data, title):
    if operation == 'create_user':
        #display a message box with user information (for demonstration purposes)
        messagebox.showinfo(title, user_data)
    elif operation == 'find_user':
        #if isinstance(user_data, dict):
            # Display the user's information
        messagebox.showinfo(title, user_data)

    elif operation == 'update_email':
        messagebox.showinfo(title, user_data)
    
    elif operation == 'delete_user':
        messagebox.showinfo(title, user_data)
