# FinVista DataHarvest

Welcome to the Financial News Scraper project, a Django web application that leverages Django, Selenium, Celery, Redis, and PostgreSQL to scrape and provide the latest financial market news. This project automates the web scraping process, preprocesses the data, stores it in a PostgreSQL database, and utilizes Redis for efficient caching. The scraped and processed information is then presented on a user-friendly web page with search and filtering options for an enhanced user experience.

## Technologies Used

- **Django:** A high-level Python web framework for rapid development.
- **Selenium:** Used for web scraping to gather financial news from specified websites.
- **Celery:** A distributed task queue system for handling periodic scraping tasks.
- **Redis:** In-memory data structure store for caching scraped data.
- **PostgreSQL:** A powerful, open-source relational database system for storing financial market news.

## Features

### 1. Web Scraping

- **Automated Scraping:** Daily scraping of financial websites for the latest news using Selenium and Celery.
- **Data Preprocessing:** Cleaning and organizing scraped data before storage.

### 2. Database Management

- **Data Storage:** Save preprocessed financial news information in a PostgreSQL database.
- **Automated Updates:** Daily updates to the database to ensure the latest information is available.

### 3. Caching with Redis

- **Efficient Caching:** Utilize Redis for caching to enhance the performance of data retrieval.

### 4. Web Interface

- **User-Friendly Display:** Present the scraped financial news on a web page.
- **Search and Filtering:** Implement search and filtering options for users to easily interact with the information.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/financial-scraper.git`
2. Navigate to the project directory: `cd financial-scraper`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up the PostgreSQL database and update the database configuration in the `settings.py` file.
5. Set up Redis and update the configuration accordingly.
6. Run migrations: `python manage.py migrate`
7. Start the Celery worker: `celery -A yourprojectname worker --loglevel=info`
8. Run the development server: `python manage.py runserver`

Access the application at `http://localhost:8000` in your browser.

## Usage

1. Visit the web page to view the latest financial market news.
2. Utilize the search and filtering options to interact with the information as needed.

## Contributions

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
