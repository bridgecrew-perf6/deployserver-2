# Generated by Django 4.0.2 on 2022-03-03 19:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
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
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('host', models.CharField(blank=True, max_length=200, null=True)),
                ('displayName', models.CharField(max_length=30)),
                ('github', models.CharField(blank=True, max_length=100, null=True)),
                ('profileImage', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('contentType', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('description', models.CharField(max_length=500)),
                ('visibility', models.CharField(max_length=10)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(default='', max_length=200)),
                ('origin', models.CharField(default='', max_length=200)),
                ('categories', models.CharField(max_length=200)),
                ('unlisted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('object', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_requests', models.ManyToManyField(to='api.FollowRequest')),
                ('posts', models.ManyToManyField(to='api.Post')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
        migrations.AddField(
            model_name='followrequest',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_sent', to='api.author'),
        ),
        migrations.AddField(
            model_name='followrequest',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_received', to='api.author'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('contentType', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=200)),
                ('published', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
    ]