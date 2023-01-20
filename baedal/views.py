from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Store
from .models import Menu
from .models import Customer
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    """
    store 목록
    """
    page = request.GET.get('page', '1')

    store_list = Store.objects.order_by('id')

    paginator = Paginator(store_list, 10)
    page_obj = paginator.get_page(page)

    context = {'store_list': page_obj}
    return render(request, 'baedal/store_list.html', context)

def detail(request, store_id):
    """
    store 디테일
    """
    menu = Menu.objects.filter(sid=store_id)
    context = {'menu': menu}
    return render(request, 'baedal/store_detail.html', context)

def cart(request):
    """
    장바구니
    """
    if request.method == 'POST':
        menu_list = request.POST.getlist('menu')
        context = {'menu_list': menu_list}

    return render(request, 'baedal/cart.html', context)

def pay(request, order_id):
    """
    결제
    """
    pay = Customer.objects.filter()