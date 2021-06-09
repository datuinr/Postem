from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index, name="all_posters"),
    path('about/', views.about),
    path('contact/', views.contact),
    # path('posters/', views.all_posters),
    path('posters/<slug:slug>/', views.poster_detail, name="poster_detail"),
    path('search/<slug:category_slug>/', views.category_list, name="category_list"),
    # path('posters/now-trending', views.trending)
]
