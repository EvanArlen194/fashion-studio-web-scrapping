# Fashion Studio Web Scraping Project

This repository contains code for scraping product data from the [Fashion Studio](https://fashion-studio.dicoding.dev/) website and performing ETL (Extract, Transform, Load) operations on the collected data.

## Project Overview

This project scrapes product information from the Fashion Studio e-commerce website, processes the data, and stores it in a structured format. The data collected includes product names, prices, ratings, colors, size, and gender.

## Features

- Web scraping of product information from Fashion Studio
- Data extraction from multiple product categories
- Data transformation and cleaning
- Data loading into structured formats
- ETL pipeline for automated data processing

## Technologies Used

- Python
- BeautifulSoup4 for web scraping
- Pandas for data manipulation
- Requests for HTTP requests
- Google API Client for Google Sheets integration
- PostgreSQL for database storage
- SQLAlchemy for ORM
- Pytest for testing
- Python-crontab for scheduling
- Git for version control

### Dependencies

```
beautifulsoup4==4.13.3
cachetools==5.5.2
certifi==2025.1.31
charset-normalizer==3.4.1
colorama==0.4.6
coverage==7.8.0
google-api-core==2.24.2
google-api-python-client==2.166.0
google-auth==2.38.0
google-auth-httplib2==0.2.0
googleapis-common-protos==1.69.2
greenlet==3.1.1
httplib2==0.22.0
idna==3.10
iniconfig==2.1.0
numpy==2.2.4
packaging==24.2
pandas==2.2.3
pluggy==1.5.0
proto-plus==1.26.1
protobuf==6.30.2
psycopg2-binary==2.9.10
pyasn1==0.6.1
pyasn1_modules==0.4.2
pyparsing==3.2.3
pytest==8.3.5
pytest-cov==6.1.0
python-crontab==3.2.0
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.3
rsa==4.9
six==1.17.0
soupsieve==2.6
SQLAlchemy==2.0.40
typing_extensions==4.13.1
tzdata==2025.2
uritemplate==4.1.1
urllib3==2.3.0
```

## Installation

1. Clone this repository:
```
git clone https://github.com/EvanArlen194/fashion-studio-web-scrapping.git
```

2. Navigate to the project directory:
```
cd fashion-studio-web-scrapping
```

3. Activate virtual environment:
```
venv/Scripts/activate
```

4. Install required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the scraper to collect data and process the collected data using the ETL pipeline:
```
python main.py
```

2. The processed data will be available in:
   - `products.csv`
   - Google Sheets
   - PostgreSQL database

## Project Structure

```
fashion-studio-web-scrapping/
├── utils/                 # Utility functions and helper modules  
├── tests/                 # Test files for the application
├── main.py                # Main script to run the ETL pipeline        
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Data Schema

The scraped data includes the following fields:

| Field | Description |
|-------|-------------|
| Title | Name of the product |
| Price | Product price in IDR |
| Rating | Product rating (out of 5) |
| Colors | Number of color options available |
| Size | Size of the product (S, M, L, XL, XXL) |
| Gender | Target gender (Men, Women, Unisex) |
| Timestamp | When the data was collected |

### Sample Data:

| Title | Price | Rating | Colors | Size | Gender | Timestamp |
|-------|-------|--------|--------|------|--------|-----------|
| T-shirt 2 | 1634400 | 3,9 | 3 | M | Women | 2025-04-28T21:40:31.497645 |
| Hoodie 3 | 7950080 | 4,8 | 3 | L | Unisex | 2025-04-28T21:40:31.497645 |
| Pants 4 | 7476960 | 3,3 | 3 | XL | Men | 2025-04-28T21:40:31.497645 |
| Outerwear 5 | 5145440 | 3,5 | 3 | XXL | Women | 2025-04-28T21:40:31.497645 |

## Acknowledgments

- [Fashion Studio](https://fashion-studio.dicoding.dev/) for providing the data source
- [Dicoding](https://www.dicoding.com/) for hosting the Fashion Studio website
