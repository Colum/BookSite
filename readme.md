This is a Django app exposing a small number of REST endpoints about books.

To Run:

1. Setup database: I used Postgresql because I was having a hard time setting up the django binding for MySQL on OSX.
Install postgres with all the default settings. App uses the default 'postgres' user to connect. Install the Postgres binding:
    > pip3 install psycopg2

2. Create the database from the postgres shell:
    > create database 'books';

2. Checkout the code. Assuming you have python3 and the requirements for django installed, `cd` into the top of the project and run the migrations:
     > python3 manage.py migrate


3. Import data/books.csv from the postgres shell (csv path must be adjusted to your location):
    > COPY books(book_authors, book_desc, book_edition, book_format, book_isbn, book_pages, book_rating, book_rating_count, book_review_count, book_title, genres, image_url, checked_out) FROM 'data/books.csv' DELIMITER ',' CSV HEADER;
    
4. Start the app
    > python3 manage.py runserver
    
    
    


#### Available Endpoints:

GET /books (optional query params; page, rating, orderby=[book_authors | book_format | book_title])

GET /books/{id}

POST /books/checkout/{id}

POST /books/return/{id}