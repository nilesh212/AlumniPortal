from django.contrib import admin
from app.models import SignUpModel,PostModel,EventModel,EventComment
# Register your models here.
admin.site.register(SignUpModel)
admin.site.register(PostModel)
admin.site.register(EventModel)
admin.site.register(EventComment)
