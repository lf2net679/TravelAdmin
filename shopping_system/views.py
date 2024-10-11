from django.shortcuts import render

def product_list(request):
    return render(request, 'shopping_system/product_list.html')

def product_create(request):
    return render(request, 'shopping_system/product_create.html')

def order_management(request):
    return render(request, 'shopping_system/order_management.html')