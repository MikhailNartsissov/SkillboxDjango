from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    bio = models.TextField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
