from django.shortcuts import render

def restaurant_list(request):
    return render(request, 'restaurant_system/list.html')

def restaurant_create(request):
    return render(request, 'restaurant_system/create.html')

def restaurant_category(request):
    return render(request, 'restaurant_system/category.html')