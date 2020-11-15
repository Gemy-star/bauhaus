# Generated by Django 3.1.3 on 2020-11-15 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_auto_20201029_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['birthday'], 'verbose_name': 'استطلاع رأى', 'verbose_name_plural': 'استطلاعات الرأى'},
        ),
        migrations.RemoveField(
            model_name='survey',
            name='color',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='service_type',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='user',
        ),
        migrations.AddField(
            model_name='survey',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='العنوان'),
        ),
        migrations.AddField(
            model_name='survey',
            name='birthday',
            field=models.CharField(max_length=255, null=True, verbose_name='تاريخ الميلاد'),
        ),
        migrations.AddField(
            model_name='survey',
            name='color_q',
            field=models.BooleanField(default=False, verbose_name='هل انت من مفضلين الألوان المبهجة ام القاتمة'),
        ),
        migrations.AddField(
            model_name='survey',
            name='design_q',
            field=models.BooleanField(default=False, verbose_name='هل انت من محبين التصميم الحديث العصري'),
        ),
        migrations.AddField(
            model_name='survey',
            name='hobby_q',
            field=models.BooleanField(default=False, verbose_name='هل انت من محبين التأمل والقراءة'),
        ),
        migrations.AddField(
            model_name='survey',
            name='hotcolor_q',
            field=models.BooleanField(default=False, verbose_name='هل انت من مفضلين الألوان الحارة , مثل : الأحمر , الأصفر'),
        ),
        migrations.AddField(
            model_name='survey',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='الأسم'),
        ),
        migrations.AddField(
            model_name='survey',
            name='personal_q',
            field=models.BooleanField(default=False, verbose_name='هل شخصيتك من الشخصيات متغيرة الاطباع '),
        ),
        migrations.AddField(
            model_name='survey',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='الهاتف'),
        ),
        migrations.AddField(
            model_name='survey',
            name='shape_q',
            field=models.BooleanField(default=False, verbose_name='هل انت من مفضلين الأشكال الانسيابية ام المنظمة'),
        ),
        migrations.AddField(
            model_name='survey',
            name='though_q',
            field=models.BooleanField(default=False, verbose_name='هل شخصيتك تؤمن بعلم طاقة وتأثيرها على الإنسان'),
        ),
    ]