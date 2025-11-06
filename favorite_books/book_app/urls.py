from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path("", views.main, name='main'),
    path("add_book",views.add_book,name='add_book'),
    path("add_favorite/<int:book_id>",views.add_favorite,name="add_favorite"),
    path("edit_book/<int:book_id>",views.edit_book,name='edit_book'),
    path("delete_book/<int:book_id>",views.delete_book,name='delete_book'),
    path("view_book/<int:book_id>",views.view_book,name='view_book'),
    path("un_favorite/<int:book_id>",views.un_favorite,name="un_favorite"),
    path("update_book/<int:book_id>",views.update_book,name='update_book')
]
