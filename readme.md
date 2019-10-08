This is a Django app exposing a small number of REST endpoints about books.

Implementation order:

1. create book model

2. Import data csv into postgres:
COPY books(book_authors, book_desc, book_edition, book_format, book_isbn, book_pages, book_rating, book_rating_count, book_review_count, book_title, genres, image_url) FROM 'data/books.csv' DELIMITER ',' CSV HEADER;

3. update book model to accommodate 'checked_out' field

4. implement endpoints '/books/{id}', '/books/checkout/{id}', '/books/return/{id}'

