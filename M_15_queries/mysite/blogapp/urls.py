from django.urls import path


from .views import (
    ArticleListView,
    ArticleTextView,
    CategoryStatisticsView,
)

app_name = "blogapp"


urlpatterns = [
    path("", ArticleListView.as_view(), name="index"),
    path("<int:pk>/", ArticleTextView.as_view(), name="article_text"),
    path("stat/", CategoryStatisticsView.as_view(), name="category_statistics"),
]
