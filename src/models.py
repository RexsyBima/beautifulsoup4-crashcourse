from src import Base, engine
from sqlalchemy import Column, Integer, String, Float


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    upc = Column(String, nullable=False)
    product_type = Column(String, nullable=False)
    price_incl_tax = Column(Float, nullable=False)
    price_excl_tax = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    total_reviews = Column(Integer, nullable=False)
    img_url = Column(String, nullable=False)


""" 
@dataclass
class Book:
    title: str  # v
    price: float  # v
    stock: int  # v
    rating: int  # v
    description: str
    upc: str
    product_type: str
    price_incl_tax: float
    price_excl_tax: float
    tax: float
    total_reviews: int
    img_url: str
"""


Base.metadata.create_all(engine)
