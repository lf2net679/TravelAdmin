import os
from pathlib import Path

# 建立 BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# 添加 SECRET_KEY 設置
SECRET_KEY = 'your-secret-key-here'  # 請替換為一個長的、隨機的字符串

# 添加 DEBUG 設置
DEBUG = True  # 在開發環境中設置為 True，生產環境中應該設置為 False

# 添加 ALLOWED_HOSTS 設置
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # 添加您的域名或 IP 地址

# 其他應用...

INSTALLED_APPS = [
    'myapp',  # 确保这行在 django.contrib.auth 之前
    'restaurant_system',
    'shopping_system',
    'trip_planner',
    'theme_entertainment',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',  # 添加這行
    'ckeditor',  # 添加 CKEditor
    'forum_system',  # 新增的應用
]

# 添加 MIDDLEWARE 設置
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 註釋掉這一行
]

# 添加 ROOT_URLCONF 設置
ROOT_URLCONF = 'myproject.urls'

# 添加 TEMPLATES 設置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myapp.context_processors.message_count',
            ],
        },
    },
]

# 數據庫設置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'fun'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'P@ssw0rd'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# 添加這行來指定自定義用戶模型
AUTH_USER_MODEL = 'myapp.Member'

# 登入相關設置
LOGIN_URL = '/login/'  # 確保這個路徑與您的登入URL匹配
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# 其他應用...

# 在文件的頂部附近添加這行
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 添加語言和時區設置
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 修改靜態文件設置
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 媒體文件設置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 在文件的底部添加以下內容

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

# 在文件底部添加 CKEditor 配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}