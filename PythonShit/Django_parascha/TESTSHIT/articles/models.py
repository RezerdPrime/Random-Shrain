from django.db import models

class Article(models.Model):
    title = models.CharField('название статьи', max_length=20)
    author = models.CharField('автор статьи', max_length=30)
    iq = models.IntegerField('я вумный ггыгыгг', default=-1)

    def __str__(self):
        return str([self.title, self.author, self.iq])

    def met(self):
        return type(self.title)