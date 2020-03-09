class User():
    def __init__(self, user_id, email, user_name, user_last_name):
        '''
        Class initialization
        '''
        pass

class UserCollection():
    def __init__(self):
        '''
        Class initialization
        Suggestion is to create a dictionary where the key
        will be user_id and the value will be an instance
        of Users.
        '''
        pass

    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection.
        Requirements:
        - user_id cannot exist in the collection.
        - user_id, email, user_name and user_last_name cannot be empty.
        - Returns False if there is any error.
        - Otherwise, it returns True.
        '''
        pass

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user.
        Requirements:
        - user_id needs to exist in the collection.
        - user_id cannot be modified.
        - user_id, email, user_name, user_last_name cannot be empty.
        - Returns False if there is any error.
        - Otherwise, it returns True.
        '''
        pass

    def delete_user(self, user_id):
        '''
        Deletes a user from the collection.
        Requirements:
        - user_id needs to exist in the collection.
        - Returns False if there is any error.
        - Otherwise, it returns True.
        '''
        pass

    def search_user(self, user_id):
        '''
        Searches for a user in the collection.
        Requirements:
        - If user_id exists, it returns the corresponding
        User instance.
        - Otherwise, it returns None
        '''
        pass