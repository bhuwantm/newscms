from django.urls import path

from website import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('news/<int:pk>', views.SinglePage.as_view(), name='single_page'),
    path('category/<int:pk>', views.CategoryPage.as_view(), name='category_page'),
]
