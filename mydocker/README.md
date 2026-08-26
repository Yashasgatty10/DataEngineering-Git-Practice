# Dockerized Web Scraper

## Workshop 1 Practice Project

A Python web-scraping application that collects **5-star rated books** from [Books to Scrape](https://books.toscrape.com/) and saves the results to a text file.

## Technologies Used

- Python 3.10
- Requests
- BeautifulSoup4
- HTML5lib
- Docker
- Docker Compose

## Project Structure

- `web_scrapping.py` – Web scraping program
- `Dockerfile` – Builds the Python Docker image
- `docker-compose.yaml` – Configures the Docker service
- `five_star_books.txt` – Contains the scraped 5-star book results

## How It Works

The scraper visits Books to Scrape, identifies books with a **5-star rating**, and saves their title, price, availability, and rating to `five_star_books.txt`.

Docker and Docker Compose are used to run the scraper inside a container.

## Running the Project

### Build and Start

`docker build --no-cache --network=host ./ -t workshop1`

`docker compose up -d`

### Check and Run

`docker ps`

`docker exec -it workshop_python_container sh`

`python web_scrapping.py`

## Result

The scraper successfully identifies the 5-star rated books and saves the results to `five_star_books.txt`.

## Author

**Yashas Gatty**
