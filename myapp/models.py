from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here.

class SinhVien(models.Model):
    masv = models.CharField(unique=True, max_length=20)
    full_name = models.CharField(max_length=50)
    sex = models.BooleanField(default=False)
    dob = models.DateField(auto_now_add=False)

    # def __str__(self):
    #     return (self.masv,self.full_name,self.sex)
    class Meta:
        verbose_name = 'Sinh vien'
        verbose_name_plural = 'Sinh Vien'

    def __str__(self):
        return self.full_name


class LopHoc(models.Model):
    ma_lop = models.CharField(unique=True, max_length=20)
    ten_lop = models.CharField(max_length=50, blank=True, null=True)


class SinhVienLopHoc(models.Model):
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    lop_hoc = models.ForeignKey(LopHoc, on_delete=models.CASCADE)
    gio_hoc = models.IntegerField(default=7)


class User(AbstractUser):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)


class HangSanXuat(models.Model):
    ten_hang = models.CharField(max_length=255)


class HangHoa(models.Model):
    ten_hang = models.CharField(max_length=255)
    gia_tien = models.IntegerField(default=0)
    hang = models.ForeignKey(HangSanXuat, on_delete=models.CASCADE)


class BaiViet(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
