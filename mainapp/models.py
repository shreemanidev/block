from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='Image')
    content = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title 