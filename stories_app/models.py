from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/")
    body = models.TextField()

    def __str__(self):
        idS = str(self.id)
        title = str(self.title)
        date = str(self.pub_date)
        return str(idS + ' | ' + title + ' | ' + date) # this is quiery by any fields and show it in admin center

    def data_time(self):
        return self.pub_date.strftime("%b %d %Y") # Just a method wich convers data view

    def summary(self):
        return self.body[:100] # Limititng the lenght of characters

class News(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        idS = str(self.id)
        title = str(self.title)
        date = str(self.pub_date)
        return str(idS + ' | ' + title + ' | ' + date) # this is quiery by any fields and show it in admin center

class NewsImgs(models.Model):
    newsKey = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="media/news/")
