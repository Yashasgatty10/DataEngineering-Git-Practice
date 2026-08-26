import os
from urllib.parse import urljoin

import psycopg2
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://blog.python.org/"

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5434")
DB_NAME = os.getenv("DB_NAME", "python_blogs")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


def scrape_blogs():
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    blogs = []

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if not href.startswith("/") or href.count("/") < 3:
            continue

        article_url = urljoin(BASE_URL, href)

        try:
            article_response = requests.get(article_url, timeout=10)
            article_response.raise_for_status()
        except requests.RequestException:
            continue

        article_soup = BeautifulSoup(article_response.text, "html.parser")

        title = (
            article_soup.title.get_text(strip=True)
            if article_soup.title
            else None
        )

        time_tag = article_soup.find("time")
        published_date = (
            time_tag.get("datetime")[:10]
            if time_tag and time_tag.get("datetime")
            else None
        )

        if title and published_date:
            blogs.append(
                {
                    "title": title,
                    "url": article_url,
                    "published_date": published_date,
                }
            )

    return blogs


def save_to_database(blogs):
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

    cursor = conn.cursor()

    for blog in blogs:
        cursor.execute(
            """
            INSERT INTO blog_posts (title, url, published_date)
            VALUES (%s, %s, %s)
            ON CONFLICT (url) DO NOTHING;
            """,
            (
                blog["title"],
                blog["url"],
                blog["published_date"],
            ),
        )

    conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    blogs = scrape_blogs()

    print(f"Scraped {len(blogs)} blog posts.")

    save_to_database(blogs)

    print("Blog posts saved to PostgreSQL.")
