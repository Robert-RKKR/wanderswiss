# Generated by Django 5.0.7 on 2024-09-12 12:41

import uuid
import wanderswiss.base.validators.base_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('name', models.CharField(error_messages={'invalid': 'Enter a valid name. It must contain 3 to 64 digits, letters, or special characters -, _ or spaces.'}, help_text='Unique name for the object. Must be between 3 and 64 characters long, and can include letters, digits, spaces, or special characters such as -, _.', max_length=64, validators=[wanderswiss.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='Unique slug representation of the object. Generated automatically from the name.', max_length=128, verbose_name='Slug')),
                ('description', models.CharField(blank=True, error_messages={'invalid': 'Enter a valid description. It must contain 8 to 256 digits, letters, and special characters -, _, . or spaces.'}, help_text='Detailed description of the object. Must be between 8 and 256 characters long and can include letters, digits, spaces, and special characters -, _, .', max_length=256, null=True, validators=[wanderswiss.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.CharField(choices=[('fa-regular fa-user', 'Administrator'), ('bi bi-1-circle', 'Circle')], default='fa-regular fa-user', help_text='Graphical representation of the object. Default value is Administrator icon.', max_length=64, verbose_name='Object ico')),
                ('is_dynamic', models.BooleanField(default=False, help_text='Indicates if this device was dynamically created. Dynamic devices are often generated based on specific conditions or user input at runtime.', verbose_name='Is dynamic')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indicates if the object is marked as deleted. Deleted objects are not removed from the database.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Indicates if the object is a root object. Root objects cannot be deleted or modified.', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates if the object is active. Inactive objects have limited functionality and may not appear in queries.', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time when the object was created. This timestamp is automatically set when the object is created.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time when the object was last updated. This timestamp is automatically updated whenever the object is modified.', verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-created'],
                'permissions': (('read_write', 'Read and write access.'), ('read_only', 'Read only access')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MultiDayTrialModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('name', models.CharField(error_messages={'invalid': 'Enter a valid name. It must contain 3 to 64 digits, letters, or special characters -, _ or spaces.'}, help_text='Unique name for the object. Must be between 3 and 64 characters long, and can include letters, digits, spaces, or special characters such as -, _.', max_length=64, validators=[wanderswiss.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='Unique slug representation of the object. Generated automatically from the name.', max_length=128, verbose_name='Slug')),
                ('description', models.CharField(blank=True, error_messages={'invalid': 'Enter a valid description. It must contain 8 to 256 digits, letters, and special characters -, _, . or spaces.'}, help_text='Detailed description of the object. Must be between 8 and 256 characters long and can include letters, digits, spaces, and special characters -, _, .', max_length=256, null=True, validators=[wanderswiss.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.CharField(choices=[('fa-regular fa-user', 'Administrator'), ('bi bi-1-circle', 'Circle')], default='fa-regular fa-user', help_text='Graphical representation of the object. Default value is Administrator icon.', max_length=64, verbose_name='Object ico')),
                ('is_dynamic', models.BooleanField(default=False, help_text='Indicates if this device was dynamically created. Dynamic devices are often generated based on specific conditions or user input at runtime.', verbose_name='Is dynamic')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indicates if the object is marked as deleted. Deleted objects are not removed from the database.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Indicates if the object is a root object. Root objects cannot be deleted or modified.', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates if the object is active. Inactive objects have limited functionality and may not appear in queries.', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time when the object was created. This timestamp is automatically set when the object is created.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time when the object was last updated. This timestamp is automatically updated whenever the object is modified.', verbose_name='Updated')),
                ('days', models.IntegerField(help_text='Number of days for the multi day trial.', verbose_name='Days')),
            ],
            options={
                'verbose_name': 'Multi day trial',
                'verbose_name_plural': 'Multi day trials',
                'ordering': ['-created'],
                'permissions': (('read_write', 'Read and write access.'), ('read_only', 'Read only access')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MultiDayTrialTrialModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('order', models.IntegerField(help_text='Order of the trial within the multi day trial.', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'BaseM2mModel',
                'verbose_name_plural': 'BaseM2mModels',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RouteModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('name', models.CharField(error_messages={'invalid': 'Enter a valid name. It must contain 3 to 64 digits, letters, or special characters -, _ or spaces.'}, help_text='Unique name for the object. Must be between 3 and 64 characters long, and can include letters, digits, spaces, or special characters such as -, _.', max_length=64, validators=[wanderswiss.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='Unique slug representation of the object. Generated automatically from the name.', max_length=128, verbose_name='Slug')),
                ('description', models.CharField(blank=True, error_messages={'invalid': 'Enter a valid description. It must contain 8 to 256 digits, letters, and special characters -, _, . or spaces.'}, help_text='Detailed description of the object. Must be between 8 and 256 characters long and can include letters, digits, spaces, and special characters -, _, .', max_length=256, null=True, validators=[wanderswiss.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.CharField(choices=[('fa-regular fa-user', 'Administrator'), ('bi bi-1-circle', 'Circle')], default='fa-regular fa-user', help_text='Graphical representation of the object. Default value is Administrator icon.', max_length=64, verbose_name='Object ico')),
                ('is_dynamic', models.BooleanField(default=False, help_text='Indicates if this device was dynamically created. Dynamic devices are often generated based on specific conditions or user input at runtime.', verbose_name='Is dynamic')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indicates if the object is marked as deleted. Deleted objects are not removed from the database.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Indicates if the object is a root object. Root objects cannot be deleted or modified.', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates if the object is active. Inactive objects have limited functionality and may not appear in queries.', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time when the object was created. This timestamp is automatically set when the object is created.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time when the object was last updated. This timestamp is automatically updated whenever the object is modified.', verbose_name='Updated')),
                ('gps_data', models.TextField(help_text='GPS data in XML format.', verbose_name='GPS Data')),
                ('distance', models.FloatField(help_text='Distance of the route in kilometers.', verbose_name='Distance (km)')),
                ('ascents', models.FloatField(help_text='Total ascents in meters.', verbose_name='Ascents (m)')),
                ('descents', models.FloatField(help_text='Total descents in meters.', verbose_name='Descents (m)')),
                ('min_elevation', models.FloatField(help_text='Minimum elevation in meters.', verbose_name='Minimum Elevation (m)')),
                ('max_elevation', models.FloatField(help_text='Maximum elevation in meters.', verbose_name='Maximum Elevation (m)')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
                'ordering': ['-created'],
                'permissions': (('read_write', 'Read and write access.'), ('read_only', 'Read only access')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TrialModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('name', models.CharField(error_messages={'invalid': 'Enter a valid name. It must contain 3 to 64 digits, letters, or special characters -, _ or spaces.'}, help_text='Unique name for the object. Must be between 3 and 64 characters long, and can include letters, digits, spaces, or special characters such as -, _.', max_length=64, validators=[wanderswiss.base.validators.base_validator.NameValueValidator()], verbose_name='Name')),
                ('slug', models.CharField(help_text='Unique slug representation of the object. Generated automatically from the name.', max_length=128, verbose_name='Slug')),
                ('description', models.CharField(blank=True, error_messages={'invalid': 'Enter a valid description. It must contain 8 to 256 digits, letters, and special characters -, _, . or spaces.'}, help_text='Detailed description of the object. Must be between 8 and 256 characters long and can include letters, digits, spaces, and special characters -, _, .', max_length=256, null=True, validators=[wanderswiss.base.validators.base_validator.DescriptionValueValidator()], verbose_name='Description')),
                ('ico', models.CharField(choices=[('fa-regular fa-user', 'Administrator'), ('bi bi-1-circle', 'Circle')], default='fa-regular fa-user', help_text='Graphical representation of the object. Default value is Administrator icon.', max_length=64, verbose_name='Object ico')),
                ('is_dynamic', models.BooleanField(default=False, help_text='Indicates if this device was dynamically created. Dynamic devices are often generated based on specific conditions or user input at runtime.', verbose_name='Is dynamic')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indicates if the object is marked as deleted. Deleted objects are not removed from the database.', verbose_name='Deleted')),
                ('is_root', models.BooleanField(default=False, help_text='Indicates if the object is a root object. Root objects cannot be deleted or modified.', verbose_name='Root')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates if the object is active. Inactive objects have limited functionality and may not appear in queries.', verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time when the object was created. This timestamp is automatically set when the object is created.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time when the object was last updated. This timestamp is automatically updated whenever the object is modified.', verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Trial',
                'verbose_name_plural': 'Trials',
                'ordering': ['-created'],
                'permissions': (('read_write', 'Read and write access.'), ('read_only', 'Read only access')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TrialRouteModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'BaseM2mModel',
                'verbose_name_plural': 'BaseM2mModels',
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserEventModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for this object. It is automatically generated and cannot be modified.', primary_key=True, serialize=False)),
                ('participant_id', models.CharField(help_text='Unique ID assigned to the participant by the event organizer. This ID is specific to the walk event, used for tracking, communication, and identification. It ensures proper registration and identification of each participant throughout the event.', max_length=64, verbose_name='Event Participant Identification Number')),
            ],
            options={
                'verbose_name': 'User Event relation',
                'verbose_name_plural': 'User Event relations',
            },
        ),
    ]
