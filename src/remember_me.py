import json


def get_stored_username():

    """Get stored username if available."""

    """Get stored username if available"""

    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new user name"""
    username = input('Enter the new name :  ')

    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")




def greet_user():
    """Greet the user by name."""
    st_username = get_stored_username()
    username = input('Please enter your name ')
    if username == st_username:
        print('Welcome back, ' + st_username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()



