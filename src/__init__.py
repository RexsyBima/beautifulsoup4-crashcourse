from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_URL = "https://books.toscrape.com/"


DATABASE_URL = "sqlite:///database.sqlite"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
