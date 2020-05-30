from django.contrib import admin
from .models import SinhVienLopHoc,SinhVien,LopHoc
# Register your models here.

class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('masv', 'full_name', 'sex',)


admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(LopHoc)
admin.site.register(SinhVienLopHoc)
