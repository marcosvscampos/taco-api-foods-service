class EnvConfig():
    
    def __init__(self, host: str, username:str, password:str) -> None:
        self.host = host
        self.username = username
        self.password = password
        self._check()

    def _check(self):
        is_valid = True
        for key, val in vars(self).items():
            if val is None:
                is_valid = False
                print(f">>> Initialization error: [{key}] is not set")        

        if (not is_valid):
            raise RuntimeError(">>> Application configuration error")