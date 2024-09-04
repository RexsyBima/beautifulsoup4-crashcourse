from bs4 import BeautifulSoup
from .models import Book
from src import BASE_URL, session


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, "html.parser")

    def scrape(self):
        title = self.find("div", class_="product_main").find("h1").get_text()
        price = float(
            self.find("p", class_="price_color").get_text().removeprefix("Â£")
        )  # replace("Â£", "")
        stock = int(
            self.find("p", class_=["instock", "availability"])
            .get_text()
            .strip()
            .replace("In stock (", "")
            .replace(" available)", "")
        )
        rating = self.find("p", class_="star-rating").get_attribute_list("class")[-1]
        rating = self.convert_rating(rating)
        description = (
            self.find("article", class_="product_page")
            .find("p", class_=False, id=False)
            .get_text()
        )
        table: list[BeautifulSoup] = self.find(
            "table", class_="table-striped"
        ).find_all("td")
        table = [t.get_text() for t in table]
        upc = table[0]
        product_type = table[1]
        price_incl_tax = float(table[2].removeprefix("Â£"))
        price_excl_tax = float(table[3].removeprefix("Â£"))
        tax = float(table[3].removeprefix("Â£"))
        total_reviews = int(table[-1])
        img_url = self.find("img")["src"].replace("../../", BASE_URL)
        return Book(
            title=title,
            price=price,
            stock=stock,
            rating=rating,
            description=description,
            upc=upc,
            product_type=product_type,
            price_incl_tax=price_incl_tax,
            price_excl_tax=price_excl_tax,
            tax=tax,
            total_reviews=total_reviews,
            img_url=img_url,
        )

    def scrape_urls(self):
        urls: list[BeautifulSoup] = self.find_all(
            "li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"
        )
        urls = [url.find("h3", class_=False, id=False).find("a") for url in urls]
        urls = [
            url["href"].replace("../../", f"{BASE_URL}catalogue/")
            for url in urls
            if session.query(Book).filter_by(title=url["title"]).first() is None
        ]
        if len(urls) < 20:
            print(
                f"Some links already been scraped, links that are not scraped is {len(urls)}"
            )
        elif len(urls) == 20:
            print(f"Total link is 20, all links are not beingg scraped valid")

        return urls

    #            .replace("../../", f"{BASE_URL}catalogue/")

    def get_max_page(self):
        max_page = int(
            self.find("li", class_="current")
            .get_text()
            .strip()
            .removeprefix("Page 1 of ")
        )
        return max_page

    def convert_rating(self, rating: str):
        match rating:
            case "One":
                return 1
            case "Two":
                return 2
            case "Three":
                return 3
            case "Four":
                return 4
            case "Five":
                return 5
            case _:
                return 0
