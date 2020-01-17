from django.db import models

class Solution(models.Model):
    book = models.TextField()
    number_of_task = models.IntegerField()
    image = models.ImageField(upload_to='image_solution', blank=True)

    def __str__(self):
        return f'Учебник :{self.book}'