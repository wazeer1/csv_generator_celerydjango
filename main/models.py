from hashlib import blake2b
import uuid
from django.db import models

# Create your models here.
class CsvFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="media/csv",blank=True, null=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table ='csv_generated'
        verbose_name = 'csv'
        verbose_name_plural = 'csvs'
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
