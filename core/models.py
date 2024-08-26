from django.db import models
#models according to the my uml diagram
class task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    def __str__(self):
        return self.title

class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class login(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email