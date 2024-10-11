from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Member, Message, ProductReview, ArticleReview, RestaurantReview
from ckeditor.widgets import CKEditorWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '電子郵箱'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '全名'}), required=True)
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}), label='我的頭像')
    
    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ('username', 'full_name', 'email', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': '帳號'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': '密碼'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': '確認密碼'})
        self.fields['full_name'].required = True
        self.fields['full_name'].label = '全名'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'avatar', 'address']
        labels = {
            'full_name': '全名',
            'avatar': '我的頭像',
            'address': '地址',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control-file'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'full_name', 'email', 'level', 'is_active', 'is_staff', 'avatar']
        labels = {
            'username': '帳號',
            'full_name': '全名',
            'email': '電子郵件',
            'level': '等級',
            'is_active': '是否啟用',
            'is_staff': '是否為工作人員',
            'avatar': '我的頭像',
        }

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].widget = forms.CheckboxInput(attrs={'class': 'i-checks'})
        self.fields['is_staff'].widget = forms.CheckboxInput(attrs={'class': 'i-checks'})

class MessageForm(forms.ModelForm):
    recipient_email = forms.CharField(label="收件人")
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Message
        fields = ['recipient_email', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender', None)
        super().__init__(*args, **kwargs)

    def clean_recipient_email(self):
        recipient = self.cleaned_data['recipient_email']
        if recipient.lower() == '管理員':
            return 'admin'
        try:
            Member.objects.get(email=recipient)
        except Member.DoesNotExist:
            raise forms.ValidationError("找不到使用此電子郵件的用戶。")
        return recipient

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ['content', 'rating']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProductReviewForm(ReviewForm):
    class Meta(ReviewForm.Meta):
        model = ProductReview

class ArticleReviewForm(ReviewForm):
    class Meta(ReviewForm.Meta):
        model = ArticleReview

class RestaurantReviewForm(ReviewForm):
    class Meta(ReviewForm.Meta):
        model = RestaurantReview