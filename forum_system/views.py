from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Article, Category, Comment
from .forms import ArticleForm, CategoryForm

def forum_home(request):
    return render(request, 'forum_system/home.html')

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def forum_article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'forum_system/article_list.html', {'articles': articles})

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def forum_article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('forum_article_list')
    else:
        form = ArticleForm()
    return render(request, 'forum_system/article_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def forum_category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum_system/category_list.html', {'categories': categories})

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def forum_comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'forum_system/comment_list.html', {'comments': comments})