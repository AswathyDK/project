# Generated by Django 4.1.6 on 2023-04-12 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestapp', '0012_sitting_remove_advocate_password_and_more'),
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
            model_name='casestatus',
            name='advocateid',
        ),
        migrations.RemoveField(
            model_name='casestatus',
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
        migrations.RemoveField(
            model_name='sitting',
            name='advocateid',
        ),
        migrations.RemoveField(
            model_name='sitting',
            name='casedetailsid',
        ),
        migrations.RemoveField(
            model_name='sitting',
            name='clientid',
        ),
        migrations.RemoveField(
            model_name='sittingpayment',
            name='sittingid',
        ),
        migrations.DeleteModel(
            name='Advocate',
        ),
        migrations.DeleteModel(
            name='Casedetails',
        ),
        migrations.DeleteModel(
            name='Casestatus',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Sitting',
        ),
        migrations.DeleteModel(
            name='SittingPayment',
        ),
    ]