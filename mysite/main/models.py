from django.db import models

# Create your models here.
class Google(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    main_pic = models.CharField(max_length=200)
    wiki = models.CharField(max_length=200)
    location = models.CharField(max_length=50, default='')

    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)

    inout = models.CharField(max_length=50, blank=True, null=True)
    charge = models.CharField(max_length=50, blank=True, null=True)

    popular = models.IntegerField(null=False)
    def __str__(self):
        return self.name

    theme = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
      	ordering = ['-popular']

class Write(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=1000, null=True, blank=True)
    contents = models.TextField(default='SOME STRING')
    google = models.ForeignKey(to='main.Google', on_delete=models.CASCADE)
    hits = models.PositiveIntegerField(default=0)
    mainphoto = models.ImageField(blank=True, null=True)
    #wite_dttm = models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')
    #update_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')

    category = models.ForeignKey(to='main.Category', null=True, on_delete=models.SET_NULL)
    url = models.CharField(max_length=100)
    def __str__(self):
        return f'[{self.pk}] {self.google} :: {self.name}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Choice(models.Model):
    select = models.CharField(max_length=100)
    store = models.ForeignKey(to='main.Write', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.select} {self.store}'