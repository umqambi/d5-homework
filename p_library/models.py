from django.db import models
from datetime import date

class Author(models.Model):  
    full_name = models.TextField(verbose_name="ФИО Автора")  
    birth_year = models.SmallIntegerField(verbose_name="Дата рождения")  
    country = models.CharField(
        max_length=2, 
        verbose_name="Страна автора", 
        help_text="Введите двубуквенный код страны"
        )
    def __str__(self):
        return self.full_name


class Redaction(models.Model):
    red_name = models.TextField(verbose_name="Название издательства")
    red_region = models.TextField(verbose_name="Регион издательства", help_text="Введите код страны/региона")
    reg_contact = models.TextField(verbose_name="Контакты")
    reg_site = models.TextField(verbose_name="Сайт издательства")
    def __str__(self):
        return self.red_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13, help_text="Введите 13ти значный ISBN код книги(только цифры)")  
    title = models.TextField(verbose_name="Название")  
    description = models.TextField(verbose_name="Описание")  
    year_release = models.SmallIntegerField(verbose_name="Год издания")  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE, verbose_name="Издательство")
    copy_count = models.SmallIntegerField(default=1, verbose_name="Кольчество копий")
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name="Цена")
    def __str__(self):
        return self.title

class Friend(models.Model):
    fr_name = models.CharField(max_length=60, help_text="Введи ФИО друга", verbose_name="ФИО")
    fr_mail = models.EmailField(help_text="Введи EMAIL друга", verbose_name="Электронная почта")
    def __str__(self):
        return self.fr_name

class BooksRent(models.Model):
    rented_book = models.OneToOneField(
        Book, 
        on_delete=models.PROTECT,
        verbose_name="Арендованная книга",
        help_text="Помните, что книги нельзя сздать в аренду дважды"
        )
    # book_tenants = models.ForeignKey(
    #     Friend, 
    #     verbose_name="Арендатор",
    #     on_delete=models.PROTECT
    #     )
    book_renter = models.OneToOneField(
        Friend, 
        verbose_name="Арендатор", 
        on_delete=models.PROTECT, 
        blank=True,
        null=True,
        help_text="Помните, что 1 пользователь может взять 1 книгу!")
    return_date = models.DateField(
        auto_now=False, 
        auto_now_add=False, 
        blank=True, 
        default=date.today,
        verbose_name="Дата возврата"
        )