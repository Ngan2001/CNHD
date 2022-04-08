from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to = 'uploads/%Y/%m')

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name
class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='course/%Y/%m', default=None)
    created_date = models.DateField(auto_now_add=True)
    upp_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject



class Course(ItemBase):
    class Meta:
        unique_together = ('subject','category')
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject','course')
        ordering = ["id"]
    content = models.TextField()
    course = models.ForeignKey(Course,related_name="lesson", on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', blank=True)


class Tag(models.Model):
    name =models.CharField(max_length=58, unique=True)

    def __str__(self):
        return self.name


