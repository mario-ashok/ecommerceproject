from django.shortcuts import render
from .models import  Product
from django.core.paginator import Paginator


def index(request):
	products = Product.objects.all()

	product_name = request.GET.get('item_name')
	if product_name!='' and product_name is not None:
		products=Product.objects.filter(title__icontains=product_name)


	paginator = Paginator(products,2)
	page = request.GET.get('page')
	products=paginator.get_page(page)
	return render(request,"shop/index.html",{'products':products})

