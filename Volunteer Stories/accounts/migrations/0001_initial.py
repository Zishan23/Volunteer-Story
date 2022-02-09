# Generated by Django 4.0.1 on 2022-01-30 06:13

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
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='website_images', verbose_name='Image')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('is_hero', models.BooleanField(default=False, verbose_name='Is hero')),
                ('is_divider', models.BooleanField(default=False, verbose_name='Is divider')),
                ('is_gallery', models.BooleanField(default=False, verbose_name='Is banner')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('whatsapp', models.CharField(max_length=15, verbose_name='Whatsapp Number')),
                ('social_media', models.CharField(max_length=15, verbose_name='Social Media')),
                ('gender', models.CharField(max_length=20, verbose_name='Gender')),
                ('pronouns', models.CharField(max_length=25, verbose_name='Pronouns')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('country', models.CharField(max_length=25, verbose_name='Country of Residence')),
                ('nationality', models.CharField(max_length=25, verbose_name='Nationality')),
                ('sector', models.CharField(max_length=255, verbose_name='Volunteering Sector')),
                ('mode_of_communication', models.CharField(max_length=50, verbose_name='Preffered Mode of Communication')),
                ('photo_sharing_consent', models.BooleanField(verbose_name='Photo Sharing Consent')),
                ('nominee1_name', models.CharField(max_length=100, verbose_name='Nominee 1 Name')),
                ('nominee1_social_media', models.CharField(max_length=50, verbose_name='Nominee 1 Social Media')),
                ('nominee1_country', models.CharField(max_length=50, verbose_name='Nominee 1 Country')),
                ('nominee1_contact', models.CharField(max_length=50, verbose_name='Nominee 1 Contact')),
                ('nominee2_name', models.CharField(max_length=100, verbose_name='Nominee 2 Name')),
                ('nominee2_social_media', models.CharField(max_length=50, verbose_name='Nominee 2 Social Media')),
                ('nominee2_country', models.CharField(max_length=50, verbose_name='Nominee 2 Country')),
                ('nominee2_contact', models.CharField(max_length=50, verbose_name='Nominee 2 Contact')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='user-placeholder.jpg', null=True, upload_to='thumbnail', verbose_name='Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
