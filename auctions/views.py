from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User,Auction,Category,Bid
from django.core.files.storage import FileSystemStorage
import os, os.path
from .models import User


def index(request):
    return render(request, "auctions/index.html",{
        "auctions":Auction.objects.all(),
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def Create_listing(request):
    if request.method == "POST":
        product = Auction()
        category = Category.objects.get(id=int(request.POST["category"]))

        product.title = request.POST["title"]
        product.seller = request.user
        product.description= request.POST["description"]
        product.active = request.POST["active"]
        product.price = request.POST["price"]
        product.image = request.FILES['image']
        product.selectcategory = category
        product.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html",{
            "categories": Category.objects.all()
        })
def Category_view(request):
    return render(request,"auctions/category.html",{
        "category": Category.objects.all()
    })

def Category_list(request,category_id):
    products = Auction.objects.filter(selectcategory=category_id)
    if len(products) >= 1:
        return render(request, "auctions/category_list.html",{
        "products": products,
    })

    else:
        return render(request, "auctions/category_list.html",{
        "message": "No listings found!"
    })

def Place_bid(request):
    pass

def User_comment(request):
    pass

@login_required
def User_watchlist(request):
    show_products = Watchlist.objects.filter(user = request.user)
    if show_products:
        return render(request, "auctions/watchlist.html", {
            'liked_products': show_products
        })
    else:
        return render(request, "auctions/watchlist.html", {
            'message': 'Empty'
        })

@login_required
def addWatchlist(request, id):
    q = Auction.objects.get(id = id)
    Watchlist.objects.create(user = request.user, product_id = q)
    return HttpResponseRedirect(reverse("index"))



          


        
