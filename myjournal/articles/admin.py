from django.contrib import admin

# Register your models here.
from .models import Articles,Comments,Like,Prompts,Writeups
# Register your models here.
admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Prompts)
admin.site.register(Writeups)
