# Generated by Django 3.2.3 on 2022-07-26 07:45

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import voc_nps.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('scolor', models.CharField(blank=True, max_length=100, null=True)),
                ('rcolor', models.CharField(blank=True, max_length=100, null=True)),
                ('fcolor', models.CharField(blank=True, max_length=100, null=True)),
                ('bcolor', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('format', models.CharField(blank=True, max_length=50, null=True)),
                ('template_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('text', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Rating',
            },
        ),
        migrations.CreateModel(
            name='Rating_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=250, null=True)),
                ('product', models.CharField(blank=True, max_length=250, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Rating_Report',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintext', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Scale',
            },
        ),
        migrations.CreateModel(
            name='voc_nps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=250)),
                ('product', models.CharField(max_length=250)),
                ('upload', models.ImageField(blank=True, null=True, upload_to='brandlogos/')),
                ('is_accept', models.BooleanField(default=False)),
                ('link', models.CharField(blank=True, max_length=600, null=True)),
                ('username', models.CharField(blank=True, max_length=250, null=True)),
                ('userqrcode', models.ImageField(blank=True, null=True, upload_to='userqrcodes/')),
                ('qrcodename', models.ImageField(blank=True, null=True, upload_to='qrcodes/')),
            ],
            options={
                'db_table': 'voc_nps',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('Super_Admin', 'Super Admin'), ('Company_Lead', 'Company Lead'), ('Org_Lead', 'Orgnisation Lead'), ('Dept_Lead', 'Department Lead'), ('Client_Admin', 'Client Admin'), ('Proj_Lead', 'Project Lead'), ('Team_Member', 'Team Member'), ('Hr', 'Hr'), ('User', 'User')], default='User', max_length=20)),
                ('profile_image', models.ImageField(blank=True, default=voc_nps.models.get_default_profile_image, max_length=255, null=True, upload_to=voc_nps.models.get_profile_image_path)),
                ('teamcode', models.CharField(max_length=20, null=True)),
                ('phonecode', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
