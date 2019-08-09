# Generated by Django 2.2.3 on 2019-07-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                # primary_key가 자동 생성 (id라는 컬럼이 자동으로 만들어진 것), auto_created : 자동증가
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]