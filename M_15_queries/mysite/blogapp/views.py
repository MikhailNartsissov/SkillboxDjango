from .models import Article, Category, Author
from django.views.generic import ListView, DetailView
from django.db.models import Count, Min, Sum, Max, F


class ArticleListView(ListView):
    queryset = (
        Article.objects.defer("content").
        select_related("author", "category").
        prefetch_related("tags")
    )


class ArticleTextView(DetailView):
    template_name = "blogapp/article_text.html"
    queryset = (
        Article.objects.values("title", "content")
    )
    context_object_name = "article_text"


class CategoryStatisticsView(ListView):
    template_name = "blogapp/category_statistics.html"
    queryset = Category.objects.values("name").annotate(
        authors_count=Count("article__author", distinct=True),
        articles_count=Count("article"),
        top_author=Max("article__author__name"),
    )
