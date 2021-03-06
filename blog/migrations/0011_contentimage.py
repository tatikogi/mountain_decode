# Generated by Django 2.2 on 2020-06-06 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200606_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_image', models.ImageField(upload_to='post_content_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post')),
            ],
        ),
    ]
