from django.urls import path

# from blogging.views import list_view, stub_view, detail_view
from blogging.views import BloggingListView, stub_view, BloggingDetailView

urlpatterns = [
    path("", BloggingListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BloggingDetailView.as_view(), name="blog_detail"),
]
