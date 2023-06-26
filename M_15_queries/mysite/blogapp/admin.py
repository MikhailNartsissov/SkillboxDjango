from django.contrib import admin

from .models import Article


class ArticleInline(admin.TabularInline):
    model = Article.tags.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleInline,
    ]
    list_display = "title", "content", "pub_date"

    def get_queryset(self, request):
        return Article.objects.select_related("author", "category").prefetch_related("tags")

