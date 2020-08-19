from Ghost_App import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('addpost/', views.add_post),
    path('like/<int:post_id>/', views.like_post),
    path('dislike/<int:post_id>/', views.dislike_post),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
    path('rank/', views.score_rank)
]
