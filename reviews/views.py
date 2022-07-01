from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def show_reviews(request):
    """ A view to show the user's product reviews """
    reviews = Review.objects.filter(author=request.user)

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Display form to add a review to a product """
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.product = product
            form.save()
            messages.success(request, 'Your product review has been submitted')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to submit the review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)
