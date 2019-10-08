1. create book model

2. IMPORT csv into postgres:
COPY books(book_authors, book_desc, book_edition, book_format, book_isbn, book_pages, book_rating, book_rating_count, book_review_count, book_title, genres, image_url) FROM 'data/books.csv' DELIMITER ',' CSV HEADER;

