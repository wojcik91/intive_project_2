from django.db import models


class Salary(models.Model):
    years = models.FloatField()
    salary = models.FloatField()

    def __str__(self):
        return f'Worked years: {self.years} - salary: {self.salary}'
