from django.db import models


# Create your models here.

class DriverLog(models.Model):
    statuses = (
            ('s', 'start'),
            ('f', 'finish'),
            ('o', 'off'),
        )
    company_id = models.PositiveIntegerField(verbose_name='company_id')
    create_date = models.DateTimeField(auto_now_add=True)
    driver_id = models.PositiveIntegerField(verbose_name='driver_id')
    status = models.CharField(max_length=1, choices=statuses, default='o', verbose_name='status')

    def __str__(self):
        return str(self.driver_id)

    class Meta:
        verbose_name_plural = 'Drivers'
        verbose_name = 'Driver'
        ordering = ['driver_id']
