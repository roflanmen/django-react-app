from django.db import models

# Create your models here.


# advertisement model
class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
