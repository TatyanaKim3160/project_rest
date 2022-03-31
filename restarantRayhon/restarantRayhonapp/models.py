from django.db import models


# Create your models here.
class Autorisation(models.Model):
    user = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    e_mail = models.EmailField(max_length=70,blank=True)
    password = models.CharField(max_length=20)
    def __str__(self):
        return str(self.user)


class Comments(models.Model):
    user = models.ForeignKey(Autorisation, on_delete=models.CASCADE)  # выбрать только user
    text = models.TextField()
    score = models.CharField(max_length=20)
    def __str__(self):
        return str(self.user) + ' - ' + str(self.text) + ' - ' + str(self.score)
#

class Restarant(models.Model):
    adress = models.CharField(max_length=20)
    # picture = models.ImageField()      #вывести фото ресторана
    info = models.CharField(max_length=200)
    def __str__(self):
        return str(self.adress)


class Position(models.Model):
    position = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)  # выбрать не целое число
    def __str__(self):
        return str(self.position) + ' - ' + str(self.salary)


class Personal(models.Model):
    fio = models.CharField(max_length=50)
    telephone = models.CharField(max_length=25)  # формат телефона
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    job_adress = models.ForeignKey(Restarant, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.fio)


class Measure(models.Model):
    measure = models.CharField(max_length=20)
    def __str__(self):
        return str(self.measure)


class Store(models.Model):
    ingridients = models.CharField(max_length=50)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    weight = models.CharField(max_length=50)  # не целое
    price_for_measure = models.CharField(max_length=50)  # не целое

    def __str__(self):
        return str(self.ingridients)



class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=20)  # не целое
    weight = models.CharField(max_length=20)  # не целое
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default='SOME STRING')
    picture = models.CharField(max_length=100,default='SOME STRING')
    def __str__(self):
        return str(self.picture)


class Booking(models.Model):
    name_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name_waiter = models.ForeignKey(Personal, on_delete=models.CASCADE)  # выбрать только имя официанта
    price_full = models.CharField(max_length=10)

    # price_bokking=models   #сложить все блюда и вывестиобщую сумму
    def __str__(self):
        return str(self.name_menu) + ' - ' + str(self.name_waiter)

class Artists(models.Model):
    name = models.CharField(max_length=128)
    date_of_start = models.DateField()
    date_of_end = models.DateField()
