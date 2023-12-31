# Generated by Django 4.2.6 on 2023-12-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0007_course_code_department_code_alter_course_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='code',
        ),
        migrations.RemoveField(
            model_name='department',
            name='code',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='purpose',
            field=models.CharField(choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')], max_length=50),
        ),
    ]
