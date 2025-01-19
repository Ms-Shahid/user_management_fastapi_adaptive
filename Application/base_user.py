

class BaseUser(BaseModel):
    email : str
    username : str
    first_name : str
    last_name : str
    gender : str
    country : str
    isActive : bool
    