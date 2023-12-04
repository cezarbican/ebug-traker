from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=500, unique=False)
    description = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

# class Register(models.Model):
#     firstname = models.CharField(max_length=500, unique=False)
#     lastname = models.CharField(max_length=500, unique=False)
#     email = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=200, unique=False)
#     created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
#     edited_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.firstname 