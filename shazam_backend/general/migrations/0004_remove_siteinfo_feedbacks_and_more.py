# Generated by Django 4.1.5 on 2023-02-08 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_sitesocial_siteinfo_created_at_siteinfo_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteinfo',
            name='feedbacks',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='site_reviews',
        ),
    ]
