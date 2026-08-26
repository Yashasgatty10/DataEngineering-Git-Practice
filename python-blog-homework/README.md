# Python Blog Scraper

## Workshop 1 Homework

A Dockerized Python web scraper that collects recent blog posts from **Python Insider** and stores the scraped data in a **PostgreSQL database**.

## Technologies Used

- Python 3.12
- Requests
- BeautifulSoup4
- PostgreSQL 14
- Docker
- Docker Compose

## Project Structure

- `scraper.py` – Scrapes blog titles, URLs, and published dates
- `requirements.txt` – Python dependencies
- `Dockerfile` – Builds the scraper Docker image
- `docker-compose.yaml` – Runs the scraper and PostgreSQL
- `.gitignore` – Excludes unnecessary files
- `README.md` – Project documentation

## Description

The scraper fetches blog posts from Python Insider using Requests and BeautifulSoup4. It extracts the blog title, URL, and published date and stores the information in the PostgreSQL `blog_posts` table.

Docker Compose runs the Python scraper and PostgreSQL database as separate services.

## Running the Project

### Build the Docker Image

`docker compose build`

### Start the Services

`docker compose up -d`

### Check the Containers

`docker ps -a`

### View Scraper Output

`docker logs python_blog_scraper`

### Expected Output

`Scraped 9 blog posts.`

`Blog posts saved to PostgreSQL.`

## Database Verification

### Connect to PostgreSQL

`docker exec -it python_blog_db psql -U postgres -d python_blogs`

### Check Number of Posts

`SELECT COUNT(*) FROM blog_posts;`

### View Stored Posts

`SELECT id, title, published_date FROM blog_posts ORDER BY published_date DESC;`

## Result

The project successfully scrapes Python Insider blog posts and stores them in PostgreSQL using Docker and Docker Compose.

## Author

**Yashas Gatty**
