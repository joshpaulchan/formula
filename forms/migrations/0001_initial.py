# Generated by Django 2.2.5 on 2019-09-02 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', related_query_name='submission', to='forms.Form')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=144)),
                ('value', models.CharField(max_length=144)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', related_query_name='entry', to='forms.Submission')),
            ],
        ),
    ]
