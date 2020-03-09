class UserStatus():
    def __init__(self, status_id, user_id, status_text):
        '''
        Class initialization
        '''
        pass

class UserStatusCollection():
    def __init__(self):
        '''
        Class initialization
        It is recommended to use a dictionary where the key
        is status_id and the value is an instance of UserStatus        
        '''
        pass

    def add_status(self, status_id, user_id, status_text):
        '''
        Adds a new status for a given user.
        Requirements:
        - status_id cannot already exist.
        - status_text cannot be empty.
        - Method returns False if there is any error.
        - Otherwise, it returns True.
        '''
        pass

    def modify_status(self, status_id, status_text):
        '''
        Modifies an existing status
        Requirements:
        - The status_id needs to exist already, since you're modifying it.
        - status_text cannot be empty.
        - Method returns False for any error.
        - Otherwise, it returns True.
        '''
        pass

    def delete_status(self, status_id):
        '''
        Deletes a status from the collection.
        Requirements:
        - status_id needs to exist in the collection.
        - Returns False for any error.
        - Otherwise, it returns True.
        '''
        pass

    def search_status(self, status_id):
        ''' 
        Searches for a status_id in the collection.
        Requirements:
        - If status_id exists in the collection, will return
        the corresponding instance of UserStatus
        - If status_id does not exist, it will return None.
        '''       
        pass