from .models import Article
from django.views.generic import ListView, DetailView


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
