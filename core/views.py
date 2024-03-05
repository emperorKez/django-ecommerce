from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, ProductImage, Category, ProductVariation
from vendor.models import VendorProduct

# f = {'Operating_Status__icontains': "Active", 'Legal_Name__icontains': "fruit"}
# a = q.filter(**f)
# mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
# mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

def index_view(request):
    top_category = Category.objects.filter()
    deal_product = Product.objects.filter()
    deals= []
    for item in deal_product:
        deal_item = {
        'product': item,
        'image': ProductImage.objects.filter(product=item).first()
        }
        deals.append(deal_item)
    
    context={'deals': deals,
             'top_category': top_category}
    return render(request, 'index.html', context)


def cart_view(request):
    context={}
    return render(request, 'cart.html', context)


def checkout_view(request):
    context={}
    return render(request, 'checkout.html', context)


def product_view(request, product_id):
    # product = Product.objects.get(product_id=product_id)
    vendor_product = VendorProduct.objects.filter(product__product_id=product_id),
    # product_images = ProductImage.objects.filter(product=product)
    context={'product': vendor_product,
            #  'product_images': product_images
             }
    return render(request, 'product.html', context)


def order_view(request):
    context={}
    return render(request, 'order.html', context)


@login_required
def wishlist_view(request):
    context={}
    return render(request, 'wishlist.html', context)


def category_view(request):
    context={}
    return render(request, 'category.html', context)

