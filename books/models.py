from django.db import models


class Book(models.Model):

    book_authors = models.TextField()
    book_desc = models.TextField(null=True)
    book_edition = models.CharField(max_length=200, null=True)
    book_format = models.CharField(max_length=200, null=True)
    book_isbn = models.CharField(max_length=200, null=True)
    book_pages = models.CharField(max_length=200, null=True)
    book_rating = models.FloatField()
    book_rating_count = models.IntegerField()
    book_review_count = models.IntegerField()
    book_title = models.CharField(max_length=200)
    genres = models.TextField(null=True)
    image_url = models.CharField(max_length=200, null=True)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.book_title

    class Meta:
        db_table = "books"
