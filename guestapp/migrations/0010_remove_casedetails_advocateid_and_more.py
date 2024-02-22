# Generated by Django 4.1.6 on 2023-04-12 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestapp', '0009_alter_advocate_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casedetails',
            name='advocateid',
        ),
        migrations.RemoveField(
            model_name='casedetails',
            name='casetypeid',
        ),
        migrations.RemoveField(
            model_name='casedetails',
            name='clientid',
        ),
        migrations.RemoveField(
            model_name='client',
            name='districtid',
        ),
        migrations.RemoveField(
            model_name='client',
            name='locationid',
        ),
        migrations.RemoveField(
            model_name='client',
            name='loginid',
        ),
        migrations.DeleteModel(
            name='Advocate',
        ),
        migrations.DeleteModel(
            name='Casedetails',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
