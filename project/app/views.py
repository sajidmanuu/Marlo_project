from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Product

from django.shortcuts import render, redirect
from .models import Product, Review
from .forms import ReviewForm

from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Review
from .forms import ReviewForm

from django.shortcuts import render, redirect
from .models import Product, Review

def add_review(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        review = Review(product=product, rating=rating, comment=comment)
        review.save()
    return redirect('index')  # Assuming your product list view is named 'index'


class ProductDetailView(View):
    template_name = 'product_detail.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        reviews = Review.objects.filter(product=product)
        form = ReviewForm()
        return render(request, self.template_name, {'product': product, 'reviews': reviews, 'form': form})

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            Review.objects.create(product=product, rating=rating, comment=comment)
        return redirect('product_detail', pk=pk)

def add_review(request, pk):
    product = Product.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            Review.objects.create(product=product, rating=rating, comment=comment)
            return redirect('index')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'product': product, 'form': form})

def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj}
    # return render(request, 'index.html', context)
    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # for product in products:
    #     product.avg_rating = product.review_set.all().aggregate(avg_rating=Avg('rating'))['avg_rating']

    context = {
        'products': products,
    }

    # return render(request, 'index.html', context)

    return render(request, 'index.html', {'page_obj': page_obj})

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        price = request.POST.get('price')
        available = request.POST.get('available')
        
        product = Product(
            name=name,
            barcode=barcode,
            brand=brand,
            description=description,
            price=price,
            available=available == 'True'
        )
        product.save()
    return redirect('index')
