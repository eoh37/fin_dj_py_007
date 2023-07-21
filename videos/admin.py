from django.contrib import admin

from videos.models import TBL_Usuario, TBL_Video, TBL_Video_Usuario

admin.site.register(TBL_Usuario)
admin.site.register(TBL_Video)
admin.site.register(TBL_Video_Usuario)
