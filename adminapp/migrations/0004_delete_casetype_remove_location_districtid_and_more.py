# Generated by Django 4.1.6 on 2023-04-12 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestapp', '0010_remove_casedetails_advocateid_and_more'),
        ('adminapp', '0003_casetype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Casetype',
        ),
        migrations.RemoveField(
            model_name='location',
            name='districtid',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]