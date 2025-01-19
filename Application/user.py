

class User(Base):
    __tablename__ = "users"
    id = Colum(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    country = Column(String)
    isActive = Column(Boolean)
    hashed_password = Column(String)

Base.metadata.create_all(engine)

