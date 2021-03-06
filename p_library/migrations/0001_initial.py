# Generated by Django 2.2.7 on 2019-11-13 12:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='ФИО Автора')),
                ('birth_year', models.SmallIntegerField(verbose_name='Дата рождения')),
                ('country', models.CharField(help_text='Введите двубуквенный код страны', max_length=2, verbose_name='Страна автора')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(help_text='Введите 13ти значный ISBN код книги(только цифры)', max_length=13)),
                ('title', models.TextField(verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('year_release', models.SmallIntegerField(verbose_name='Год издания')),
                ('copy_count', models.SmallIntegerField(default=1, verbose_name='Кольчество копий')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author', verbose_name='Актор')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr_name', models.CharField(help_text='Введи ФИО друга', max_length=60, verbose_name='ФИО')),
                ('fr_mail', models.EmailField(help_text='Введи EMAIL друга', max_length=254, verbose_name='Электронная почта')),
            ],
        ),
        migrations.CreateModel(
            name='Redaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_name', models.TextField(verbose_name='Название издательства')),
                ('red_region', models.TextField(help_text='Введите код страны/региона', verbose_name='Регион издательства')),
                ('reg_contact', models.TextField(verbose_name='Контакты')),
                ('reg_site', models.TextField(verbose_name='Сайт издательства')),
            ],
        ),
        migrations.CreateModel(
            name='BooksRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateField(blank=True, default=datetime.date.today, verbose_name='Дата возврата')),
                ('book_tenants', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='p_library.Friend', verbose_name='Арендатор')),
                ('rented_book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='p_library.Book', verbose_name='Арендованная книга')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='redaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Redaction', verbose_name='Издательство'),
        ),
    ]
