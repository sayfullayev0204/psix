# Generated by Django 5.1.6 on 2025-04-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_video_url_video_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='books/')),
            ],
            options={
                'verbose_name': 'Kitoblar ',
                'verbose_name_plural': 'Kitoblar ',
            },
        ),
        migrations.AlterModelOptions(
            name='guide',
            options={'verbose_name': 'Maqolalar ', 'verbose_name_plural': 'Maqolalar '},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name': 'Musiqalar ', 'verbose_name_plural': 'Musiqalar '},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Testlar ', 'verbose_name_plural': 'Testlar '},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Videolar ', 'verbose_name_plural': 'Videolar '},
        ),
    ]
