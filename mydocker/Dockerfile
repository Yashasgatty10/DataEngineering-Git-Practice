FROM python:3.10.2-alpine3.15

# Create directories
RUN mkdir -p /root/workspace/src

# Copy the web scraping program
COPY ./web_scrapping.py /root/workspace/src/

# Switch to project directory
WORKDIR /root/workspace/src

# Install required packages
RUN pip install requests beautifulsoup4 html5lib
