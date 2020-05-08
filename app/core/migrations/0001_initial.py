# Generated by Django 3.0.5 on 2020-05-07 22:05

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_activate', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('zipcode', models.CharField(blank=True, max_length=15)),
                ('cell_phone', models.CharField(max_length=15)),
                ('typeuser', models.BooleanField(default=True)),
                ('cnpj', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=50)),
                ('address_company', models.CharField(max_length=50)),
                ('phone_company', models.CharField(max_length=15)),
                ('email_company', models.CharField(max_length=250)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileBuyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('zipcode', models.CharField(blank=True, max_length=15)),
                ('cell_phone', models.CharField(max_length=15)),
                ('typeuser', models.BooleanField(default=False)),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title')),
                ('excerpt', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('descount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('coupon', models.CharField(blank=True, default=0, max_length=10)),
                ('stock', models.IntegerField(default=0)),
                ('stock_min', models.IntegerField(default=0)),
                ('stock_max', models.IntegerField(default=0)),
                ('enable', models.BooleanField(default=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
        ),
    ]
