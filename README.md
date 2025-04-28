# Fashion Studio Web Scraping Project

This repository contains code for scraping product data from the [Fashion Studio](https://fashion-studio.dicoding.dev/) website and performing ETL (Extract, Transform, Load) operations on the collected data.

## Project Overview

This project scrapes product information from the Fashion Studio e-commerce website, processes the data, and stores it in a structured format. The data collected includes product names, prices, categories, ratings, and images.

## Features

- Web scraping of product information from Fashion Studio
- Data extraction from multiple product categories
- Data transformation and cleaning
- Data loading into structured formats
- ETL pipeline for automated data processing

## Technologies Used

- Python
- BeautifulSoup for web scraping
- Pandas for data manipulation
- Requests for HTTP requests
- Git for version control

## Installation

1. Clone this repository:
```
git clone https://github.com/EvanArlen194/fashion-studio-web-scrapping.git
```

2. Navigate to the project directory:
```
cd fashion-studio-web-scrapping
```

3. Install required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the scraper to collect data:
```
python scraper.py
```

2. Process the collected data using the ETL pipeline:
```
python etl.py
```

3. The processed data will be available in the `data` directory.

## Project Structure

```
fashion-studio-web-scrapping/
├── data/                  # Directory for storing scraped and processed data
├── notebooks/             # Jupyter notebooks for data analysis
├── src/                   # Source code
│   ├── scraper.py         # Web scraping script
│   ├── etl.py             # ETL processing script
│   └── utils.py           # Utility functions
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Data Schema

The scraped data includes the following fields:

- `product_id`: Unique identifier for each product
- `product_name`: Name of the product
- `price`: Product price
- `category`: Product category (e.g., Men, Women, Accessories)
- `rating`: Product rating (if available)
- `image_url`: URL to product image
- `description`: Product description
- `availability`: Stock availability information

## Acknowledgments

- [Fashion Studio](https://fashion-studio.dicoding.dev/) for providing the data source
- Dicoding for hosting the Fashion Studio website
