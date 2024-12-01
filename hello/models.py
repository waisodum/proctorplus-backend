from django.db import models

class Greeting(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message