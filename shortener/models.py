from django.db import models

class Url(models.Model):
    url=models.URLField()
    slug=models.CharField(max_length=120)
    visit=models.IntegerField(default=0)
    create_time=models.DateTimeField(auto_now_add=True)
    class Meta():
        ordering= ("-create_time",)
        
    def __str__(self):
      return f"{self.slug}"

