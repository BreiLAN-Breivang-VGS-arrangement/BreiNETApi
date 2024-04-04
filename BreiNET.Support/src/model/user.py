class user:
    def __init__(self, uid: int, name: str, password: str, loginState: bool):
        self.uid = uid
        self.name = name
        self.password = password
        self.loginState = loginState