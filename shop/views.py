from django.shortcuts import render
from .models import  Product


def index(request):
	products = Product.objects.all()

	product_name = request.GET.get('item_name')
	if product_name!='' and product_name is not None:
		products=Product.objects.filter(title__icontains=product_name)


	return render(request,"shop/index.html",{'products':products})

