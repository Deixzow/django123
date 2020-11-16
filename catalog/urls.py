from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('roles/', views.RoleListView.as_view(), name='roles'),
    path('role/<int:pk>', views.RoleDetailView.as_view(), name='role-detail'),
    path('role/create/', views.RoleCreate.as_view(), name='role_create'),
    path('role/<int:pk>/update/', views.RoleUpdate.as_view(), name='role_update'),
    path('role/<int:pk>/delete/', views.RoleDelete.as_view(), name='role_delete'),
]
