import requests, pandas as pd
from .soup import Soup
from .models import Book
import datetime
from src import session


def get_html(url: str):
    r = requests.get(url)
    return Soup(r.text)


def save_to_xlsx(books: list[Book], filename: str):
    date = datetime.datetime.now().strftime("%d_%B_%Y")
    df = pd.DataFrame(books)
    df.to_excel(f"{date}-{filename}")


def insert_to_db(book: Book):
    session.add(book)
    session.commit()
