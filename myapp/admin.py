from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member, Article, Message, Restaurant, Product, ProductReview, ArticleReview, RestaurantReview

class CustomUserAdmin(UserAdmin):
    model = Member
    list_display = ('username', 'email', 'full_name', 'level', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('level', 'is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('個人信息', {'fields': ('full_name', 'avatar')}),
        ('權限', {'fields': ('level', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Google認證', {'fields': ('google_id',)}),
        ('重要日期', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'password1', 'password2', 'level', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'full_name')
    ordering = ('-date_joined',)

admin.site.register(Member, CustomUserAdmin)
admin.site.register(Article)
admin.site.register(Message)
admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(ArticleReview)
admin.site.register(RestaurantReview)