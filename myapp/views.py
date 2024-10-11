from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, MemberForm, ProfileUpdateForm, MessageForm, CustomPasswordChangeForm, ProductReviewForm, ArticleReviewForm, RestaurantReviewForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Member, Article, Message, Product, Restaurant
import logging
import requests
from django.db.models import Count
from django.db.models.functions import TruncDate
import json
from datetime import timedelta
from django.utils import timezone

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "用戶名或密碼不正確")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "註冊成功！")
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.level == 'admin':
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')

def is_admin(user):
    return user.level == 'admin'

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def admin_dashboard(request):
    users = Member.objects.all().order_by('-date_joined')
    # 獲取最新收到的訊息
    latest_messages = Message.objects.filter(recipient=request.user).order_by('-created_at')[:5]

    # 獲取最近發送的訊息
    sent_messages = Message.objects.filter(sender=request.user).order_by('-created_at')[:5]

    context = {
        'users': users,
        'latest_messages': latest_messages,
        'sent_messages': sent_messages,
    }
    return render(request, 'admin-dashboard/dashboard.html', context)

@login_required
def user_dashboard(request):
    # 獲取天氣資訊（這裡使用 OpenWeatherMap API 作為示例）
    api_key = "YOUR_API_KEY"  # 替換為您的 API 密鑰
    city = "Taipei"  # 可以根據用戶的位置動態設置
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
    except requests.RequestException:
        weather_data = {"name": "N/A", "main": {"temp": "N/A"}, "weather": [{"description": "N/A"}]}

    # 獲取用戶的文章
    user_articles = Article.objects.filter(author=request.user).order_by('-pub_date')[:5]

    # 獲取新消息數量
    new_messages_count = Message.objects.filter(recipient=request.user, is_read=False).count()

    # 這裡您需要根據實際情況獲取新歌曲的數量
    new_songs_count = 0  # 示例值，請根據實際情況修改

    # 獲取喜好的餐廳（假設您有一個 Restaurant 模型和相關的 ManyToMany 關係）
    favorite_restaurants = request.user.favorite_restaurants.all()[:5] if hasattr(request.user, 'favorite_restaurants') else []

    # 獲取喜愛的商品（假設您有一個 Product 模型和相關的 ManyToMany 關係）
    favorite_products = request.user.favorite_products.all()[:5] if hasattr(request.user, 'favorite_products') else []

    # 獲取最新收到的訊息
    latest_messages = Message.objects.filter(recipient=request.user).order_by('-created_at')[:5]

    # 獲取最近發送的訊息
    sent_messages = Message.objects.filter(sender=request.user).order_by('-created_at')[:5]

    # 獲取新通知數量（如果您有通知系統）
    new_notifications_count = 0  # 替換為實際的通知計數邏輯

    context = {
        'weather': weather_data,
        'user_articles': user_articles,
        'new_messages_count': new_messages_count,
        'new_songs_count': new_songs_count,
        'favorite_restaurants': favorite_restaurants,
        'favorite_products': favorite_products,
        'latest_messages': latest_messages,
        'new_notifications_count': new_notifications_count,
        'sent_messages': sent_messages,
    }
    return render(request, 'user_dashboard.html', context)

@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)  # 重要，更新session，不然會登出
            messages.success(request, '您的個人資料和密碼已更新！')
            return redirect('user_dashboard')
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request, '您的個人資料已更新！')
            return redirect('user_dashboard')
    else:
        profile_form = ProfileUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)
    
    context = {
        'profile_form': profile_form,
        'password_form': password_form,
    }
    return render(request, 'profile_update.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def member_list(request):
    members = Member.objects.all().order_by('-date_joined')
    return render(request, 'member_list.html', {'users': members})

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'member_detail.html', {'member': member})

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '用戶創建成功')
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, '用戶資訊更新成功')
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.level == 'admin')
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        messages.success(request, '用戶刪除成功')
        return redirect('member_list')
    return render(request, 'member_confirm_delete.html', {'member': member})

def set_admin(request):
    email = 'lf2net67983@gmail.com'
    try:
        user = Member.objects.get(email=email)
        user.level = 'admin'
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return HttpResponse(f'成功將用戶 {user.username} 設置為管理員')
    except Member.DoesNotExist:
        return HttpResponse(f'電子郵件為 {email} 的用戶不存在', status=404)

def index(request):
    return render(request, 'home.html')

def sweetalert_view(request):
    return render(request, 'sweetalert.html')

def register_v2_view(request):
    return render(request, 'register_v2.html')

# 為其他 H-v4 HTML 文件添加類似的視圖函數

@login_required
def inbox(request):
    received_messages = Message.objects.filter(recipient=request.user).order_by('-created_at')
    unread_count = received_messages.filter(is_read=False).count()
    return render(request, 'messages/inbox.html', {
        'messages': received_messages,
        'unread_count': unread_count
    })

@login_required
def sent_messages(request):
    sent_messages = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'messages/sent.html', {'messages': sent_messages})

@login_required
def compose_message(request):
    reply_to_id = request.GET.get('reply_to')
    quote = request.GET.get('quote') == 'true'
    
    if request.method == 'POST':
        form = MessageForm(request.POST, sender=request.user)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            if recipient_email == 'admin':
                admin_recipients = Member.objects.filter(level='admin')
                for admin in admin_recipients:
                    Message.objects.create(
                        sender=request.user,
                        recipient=admin,
                        subject=form.cleaned_data['subject'],
                        content=form.cleaned_data['content']
                    )
                messages.success(request, '訊息已成功發送給所有管理員。')
            else:
                message = form.save(commit=False)
                message.sender = request.user
                recipient = Member.objects.get(email=recipient_email)
                message.recipient = recipient
                if reply_to_id and quote:
                    quoted_message = Message.objects.get(id=reply_to_id)
                    message.quoted_message = quoted_message
                message.save()
                messages.success(request, '訊息已成功發送。')
            return redirect('inbox')
    else:
        initial = {}
        if reply_to_id:
            replied_message = Message.objects.get(id=reply_to_id)
            initial['recipient_email'] = '管理員' if replied_message.sender.level == 'admin' else replied_message.sender.email
            initial['subject'] = f"Re: {replied_message.subject}"
            if quote:
                initial['content'] = f"\n\n--- 原始訊息 ---\n{replied_message.content}"
        form = MessageForm(initial=initial, sender=request.user)
    
    return render(request, 'messages/compose.html', {'form': form})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.recipient == request.user and not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'messages/detail.html', {'message': message})

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.recipient == request.user or message.sender == request.user:
        message.delete()
        messages.success(request, '訊息已成功刪除。')
    else:
        messages.error(request, '您沒有權限刪除這條訊息。')
    return redirect('inbox')

@login_required
def some_view_function(request):
    # 獲取最新的5條訊息
    latest_messages = Message.objects.filter(recipient=request.user).order_by('-created_at')[:5]
    new_messages_count = Message.objects.filter(recipient=request.user, is_read=False).count()
    
    # 其他視圖邏輯...
    
    context = {
        'latest_messages': latest_messages,
        'new_messages_count': new_messages_count,
        # 其他上下文數據...
    }
    return render(request, 'some_template.html', context)

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all().order_by('-created_at')
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductReviewForm()
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews, 'form': form})

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    reviews = article.reviews.all().order_by('-created_at')
    if request.method == 'POST':
        form = ArticleReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.article = article
            review.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleReviewForm()
    return render(request, 'article_detail.html', {'article': article, 'reviews': reviews, 'form': form})

@login_required
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all().order_by('-created_at')
    if request.method == 'POST':
        form = RestaurantReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
    else:
        form = RestaurantReviewForm()
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'reviews': reviews, 'form': form})