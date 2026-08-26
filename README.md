# DataEngineering-Git-Practice
# Dockerized Web Scraping Project

## Overview

This project demonstrates how to **Dockerize a Python web-scraping application** using Docker and Docker Compose.

The Python program scrapes book information from **Books to Scrape**, identifies books with a **5-star rating**, and saves the results into a text file.

## Project Structure

```text
mydocker/
├── Dockerfile
├── docker-compose.yaml
├── web_scrapping.py
└── five_star_books.txt
```

## Technologies Used

* Python 3.10
* Docker
* Docker Compose
* Requests
* BeautifulSoup (bs4)
* HTML5lib

## Dockerfile

The Dockerfile:

1. Uses the Python 3.10 Alpine image.
2. Creates a workspace directory inside the container.
3. Copies the web-scraping Python script into the container.
4. Installs the required Python packages.
5. Sets the working directory for the application.

## Docker Compose

Docker Compose is used to configure and run the Python container.

The service is named:

```text
python_service
```

and the container is:

```text
workshop_python_container
```

The project uses a Docker volume so that files from the local project directory can be accessed by the container.

## Running the Project

### 1. Build the Docker image

```bash
docker build --no-cache --network=host ./ -t workshop1
```

### 2. Start the container

```bash
docker compose up -d
```

### 3. Check the running container

```bash
docker ps
```

### 4. Enter the container

```bash
docker exec -it workshop_python_container sh
```

### 5. Run the scraper

Inside the container:

```bash
python web_scrapping.py
```

## Output

The scraper identifies books with a 5-star rating.

Example output:

```text
5-STAR RATED BOOKS

Total 5-star books found: 4
Results saved to five_star_books.txt
```

The results are stored in:

```text
five_star_books.txt
```

The file contains the title, price, availability, and rating of each 5-star book.

## Purpose

The main purpose of this exercise is to understand how to:

* Build a Docker image for a Python application.
* Run a Python application inside a Docker container.
* Install Python dependencies inside the container.
* Use Docker Compose to manage the container.
* Perform web scraping from inside a Dockerized environment.
* Save the scraped results to an output file.

## Author

**Yashas Gatty**
