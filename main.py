from src.utils import get_html, save_to_xlsx, insert_to_db
from src.soup import Soup

"""
def scrape_book():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    html = get_html(url)
    soup = Soup(html)
    book = soup.scrape()
    print(book)


def access_url_per_page():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    html = get_html(url)
    soup = Soup(html)
    print(soup.scrape_urls())


def access_pages():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    html = get_html(url)
    soup = Soup(html)
    max_p = soup.get_max_page()
    for i in range(1, max_p + 1):
        url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
        print(url)
"""


def main():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    soup = get_html(url)
    max_p = soup.get_max_page()
    output = []
    for i in range(1, max_p + 1):
        print(f"scraping page {i}")
        url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
        soup = get_html(url)
        urls = soup.scrape_urls()
        for url in urls:
            print(f"scraping {url}")
            soup = get_html(url)
            book = soup.scrape()
            insert_to_db(book)
            output.append(book)
            # print(book)
    save_to_xlsx(output, "books.xlsx")


if __name__ == "__main__":
    main()
