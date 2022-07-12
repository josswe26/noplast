from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product


@login_required
def show_favorites(request):
    """ A view to show the user's favorite products"""
    favorite_products = Product.objects.filter(users_favorite=request.user)

    context = {
        'favorite_products': favorite_products,
    }

    return render(request, 'favorites/favorites.html', context)


@login_required
def add_or_remove_favorite(request, product_id):
    """ Add product to the user's favorites """
    product = get_object_or_404(Product, id=product_id)

    if product.users_favorite.filter(id=request.user.id).exists():
        product.users_favorite.remove(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         removed from your favorites.')
    else:
        product.users_favorite.add(request.user)
        messages.success(request,
                         f'{product.name} has been \
                         added to your favorites.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
