from django.shortcuts import render

def theme_list(request):
    return render(request, 'theme_entertainment/list.html')

def theme_create(request):
    return render(request, 'theme_entertainment/create.html')

def activity_management(request):
    return render(request, 'theme_entertainment/activity_management.html')