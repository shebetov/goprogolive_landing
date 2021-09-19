# Generated by Django 3.1.6 on 2021-02-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('ip_addr', models.GenericIPAddressField(verbose_name='E-Mail')),
                ('user_agent', models.CharField(max_length=500, verbose_name='User-Agent')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'Form E-Mail',
                'verbose_name_plural': 'Form E-Mails',
            },
        ),
    ]