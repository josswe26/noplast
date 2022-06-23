from django.shortcuts import render
from products.models import Product


def show_favorites(request):
    """ A view to show the user's favorite products"""
    favorite_products = Product.objects.filter(users_favorite=request.user)

    context = {
        'favorite_products': favorite_products,
    }

    return render(request, 'favorites/favorites.html', context)
