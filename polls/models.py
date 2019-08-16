from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


# en los modelos guardo las caracteristicas de mi data
# cada atributo de mi modelo representa un campo de la base de datos


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # esta es la funcion de toString()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# por ejemplo voy  crear un modelo que representa una persona, con sus respectivas caracteristicas, por ejemplo el
# primer nombre y el ultimo cada campo de este modelo se representa como un atributo de la clase (Modelos) y cada
# atributo se conecta (mapea) a la base de datos

class Person(models.Model):
    SHIRT_SIZES = (('S', 'Small'), ('M', 'Medium'), ('L', 'Large'))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    age = models.IntegerField()




# la clase Person que esta arriba crea una base de datos de la siguiente manera:
# esto es perfecto ya que yo no se PostgreSQL sytax
# Yo decido que syntax usa Django en mi settings file, ahora mismo esta usando SQLite 3


''''
 CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
 '''

# Queries and Databases

# Making Queries, queries refer to retrieve data from the database. While being selective on to how much data I want
# returned To save changes to an object that's already in the database one needs to call save()

# To retrieve objects from you db, construct a QuerySet by using the models manager.
# Each model has a manager and it's called objects by default.


# Migrations

# Django way of propagating the changes you make to your models (  adding a field, deleting a model) etc ,
# into the DB Schema .
