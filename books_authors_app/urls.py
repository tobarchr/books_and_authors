from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	   
    path('add_book',views.add_book),
    path('authors',views.authors),
    path('add_author',views.add_author),
    path('books/<int:id_from_route>',views.book_details),
    path('authors/<int:author_id>',views.author_details),
    path('authors/assign_book',views.assign_book),
    path('books/assign_author',views.assign_author)
]