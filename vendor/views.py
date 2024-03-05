from django.shortcuts import render
from .models import Vendor

from django.shortcuts import render

def dashboard_view(request, vendor_id):
    return render(request, 'dashboard/index.html')

def vendor_view(request, vendor_id):
    vendor = Vendor.objects.get(vendor_id=vendor_id)
    context = {'vendor': vendor}
    return render(request, 'vendor-page.html', context)


def vendor_list_view(request):
    vendors = Vendor.objects.filter()
    context = {'vendors': vendors}
    return render(request, 'vendor-listing.html', context)
