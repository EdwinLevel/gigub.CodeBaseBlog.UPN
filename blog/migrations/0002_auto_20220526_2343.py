# Generated by Django 3.1.14 on 2022-05-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='ingredientes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='servidor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='post',
            name='nombre_autor',
            field=models.CharField(default=50, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pasos',
            field=models.TextField(default=500),
            preserve_default=False,
        ),
    ]