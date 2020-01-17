from django.db import models

class Solution(models.Model):
    book = models.TextField()
    number_of_task = models.IntegerField()
    image = models.TextField()

    def __str__(self):
        return f'Учебник :{self.book}'