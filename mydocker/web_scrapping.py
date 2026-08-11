import requests
from bs4 import BeautifulSoup
import re

url = "https://books.toscrape.com/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

five_star_books = []

for book in books:
    title = book.find("h3").find("a")["title"]

    price = book.find("p", class_="price_color").get_text(strip=True)

    availability = book.find(
        "p", class_="instock availability"
    ).get_text(strip=True)

    # Get the rating class
    rating_class = book.find("p", class_="star-rating")["class"]

    # Check for Five-star rating
    if "Five" in rating_class:

        # Extract price using regular expression
        price_match = re.search(r"[£$€]\d+\.\d+", price)

        if price_match:
            price = price_match.group()

        five_star_books.append(
            f"Title        : {title}\n"
            f"Price        : {price}\n"
            f"Availability : {availability}\n"
            f"Rating       : 5 stars\n"
            + "-" * 60
        )

# Display the result
print("\n5-STAR RATED BOOKS")
print("=" * 60)

for book in five_star_books:
    print(book)

# Save the result to a file
with open("five_star_books.txt", "w", encoding="utf-8") as file:
    file.write("5-STAR RATED BOOKS\n")
    file.write("=" * 60 + "\n\n")

    for book in five_star_books:
        file.write(book + "\n\n")

print(f"\nTotal 5-star books found: {len(five_star_books)}")
print("Results saved to five_star_books.txt")
