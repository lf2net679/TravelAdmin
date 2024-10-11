from django.shortcuts import render

def trip_list(request):
    return render(request, 'trip_planner/list.html')

def trip_create(request):
    return render(request, 'trip_planner/create.html')

def trip_category(request):
    return render(request, 'trip_planner/category.html')