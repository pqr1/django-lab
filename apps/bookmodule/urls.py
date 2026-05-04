from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('html5/links', views.html5_links, name='books.html5_links'),
    path('html5/text/formatting', views.text_formatting, name='books.text_formatting'),
    path('html5/listing', views.listing, name='books.listing'),
    path('html5/tables', views.tables, name='books.tables'),
    path('search', views.search, name='books.search'), #Lab6
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('lab8/task1', views.task1, name='Lab8_task1' ),
    path('lab8/task2', views.task2, name='Lab8_task2'),
    path('lab8/task3', views.task3, name='Lab8_task3'),
    path('lab8/task4', views.task4, name='Lab8_task4'),
    path('lab8/task5', views.task5, name='Lab8_task5'),    
    path('lab8/task7', views.task7, name='Lab8_task7'),
    path('lab9/task1', views.L9task1,name='Lab9_task1'),
    path('lab9/task2', views.L9task2,name='Lab9_task2'),
    path('lab9/task3', views.L9task3,name='Lab9_task3'),
    path('lab9/task4', views.L9task4,name='Lab9_task4'),
    path('lab9/task5', views.L9task5,name='Lab9_task5'),
    path('lab9/task6', views.L9task6,name='Lab9_task6'),
    path('aboutus/', views.aboutus, name="books.aboutus")
    
]
