from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('Create_listing', views.Create_listing, name='Create_listing'),
    path('Category_view', views.Category_view, name='Category_view'),
   path("<str:category_id>", views.Category_list, name='Category_list'),
   path("Bid", views.Place_bid, name="Bid"),
   path("Comment", views.User_comment, name="User_comment"),
   path("Watchlist", views.User_watchlist, name="User_watchlist"),
]
