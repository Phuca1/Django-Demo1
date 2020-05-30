from django.db import models

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


class LopHoc(models.Model):
    ma_lop = models.CharField(unique=True, max_length=20)
    ten_lop = models.CharField(max_length=50, blank=True, null=True)

class SinhVienLopHoc(models.Model):
    sinh_vien = models.ForeignKey(SinhVien, on_delete= models.CASCADE)
    lop_hoc = models.ForeignKey(LopHoc, on_delete=models.CASCADE)
    gio_hoc = models.IntegerField(default=7)