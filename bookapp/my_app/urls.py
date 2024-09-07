from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='book_index'),
    # path('bookss/', views.book_index, name='book_index'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('books/<int:pk>/add-recommendation/', views.add_recommendation, name='add-recommendation'),
    path('reviews/create/', views.ReviewCreate.as_view(), name='review-create'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-index'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review-delete'),
    path('books/<int:book_id>/associate-review/', views.associate_review, name='associate-review'),
    path('books/<int:book_id>/remove-review/<int:review_id>/', views.remove_review, name='remove-review'),
    path('accounts/signup/', views.signup, name='signup'),
]

