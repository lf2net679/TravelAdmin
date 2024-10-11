from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # 确保这行存在
    path('restaurant/', include('restaurant_system.urls')),
    path('shop/', include('shopping_system.urls')),
    path('trip/', include('trip_planner.urls')),
    path('theme/', include('theme_entertainment.urls')),
    path('forum/', include('forum_system.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)