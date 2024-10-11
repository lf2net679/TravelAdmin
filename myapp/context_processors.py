from .models import Message

def message_count(request):
    if request.user.is_authenticated:
        new_messages_count = Message.objects.filter(recipient=request.user, is_read=False).count()
        return {'new_messages_count': new_messages_count}
    return {}