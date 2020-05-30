# Generated by Django 3.0.6 on 2020-05-27 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LopHoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_lop', models.CharField(max_length=20, unique=True)),
                ('ten_lop', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masv', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('sex', models.BooleanField(default=False)),
                ('dob', models.DateField()),
            ],
            options={
                'verbose_name': 'Sinh vien',
                'verbose_name_plural': 'Sinh Vien',
            },
        ),
        migrations.CreateModel(
            name='SinhVienLopHoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gio_hoc', models.IntegerField(default=7)),
                ('lop_hoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.LopHoc')),
                ('sinh_vien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.SinhVien')),
            ],
        ),
    ]
