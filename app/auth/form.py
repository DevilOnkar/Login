
class LoginForm:
    def __init__(self,user,passw):
        self._user=user
        self._passw=passw

    def get_user(self):
        return self._user

    def set_user(self,user):
        self._user=user

    def get_passw(self):
        return self._passw

    def set_passw(self,passw):
        self._passw=passw
    
    user=property(get_user,set_user)
    passw=property(get_passw,set_passw)