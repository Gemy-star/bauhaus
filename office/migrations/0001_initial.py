# Generated by Django 3.1 on 2020-10-29 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='العنوان')),
                ('message', models.TextField(blank=True, null=True, verbose_name='الرساله')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الألكترونى')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم الجوال')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='المدينه')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='المحافظه')),
                ('category', models.CharField(choices=[('1', 'طلب خدمة'), ('2', 'طلب انضمام'), ('3', 'شكاوى'), ('4', 'مقترحات')], max_length=5, verbose_name='االتصنيفات')),
            ],
            options={
                'verbose_name': 'العمل ',
                'verbose_name_plural': 'الأعمال ',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='الأسم')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
            ],
            options={
                'verbose_name': 'الخدمه',
                'verbose_name_plural': 'الخدمات',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='الأسم')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('engineer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'العمل ',
                'verbose_name_plural': 'الأعمال ',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='اللون المفضل')),
                ('interests', models.CharField(blank=True, max_length=255, null=True, verbose_name='الاهتمامات')),
                ('quote', models.CharField(blank=True, max_length=255, null=True, verbose_name='نبذه')),
                ('service_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.service', verbose_name='نوع الخدمه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='العميل')),
            ],
            options={
                'verbose_name': 'استطلاع رأى',
                'verbose_name_plural': 'استطلاعات الرأى',
                'ordering': ['color'],
            },
        ),
        migrations.CreateModel(
            name='RequestWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='الأسم')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='صورة الموقع')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='العنوان')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.service')),
            ],
            options={
                'verbose_name': 'طلب عمل',
                'verbose_name_plural': 'طلبات عمل',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RequestMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='العنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.service', verbose_name='الخدمه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='العميل')),
            ],
            options={
                'verbose_name': 'طلب مقايسه',
                'verbose_name_plural': ' طلبات مقايسه',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_message', models.TextField(blank=True, null=True, verbose_name='الأجابه')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='العميل', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'الرد',
                'verbose_name_plural': 'الردود',
                'ordering': ['reply_message'],
            },
        ),
        migrations.CreateModel(
            name='ContactEngineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='العنوان')),
                ('message', models.TextField(blank=True, null=True, verbose_name='الرساله')),
                ('sender_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الألكترونى الخاص بالمرسل')),
                ('sender_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم المرسل')),
                ('engineer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المهندس')),
            ],
            options={
                'verbose_name': 'المرسل',
                'verbose_name_plural': 'المرسلات',
                'ordering': ['title'],
            },
        ),
    ]
