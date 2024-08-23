from django.db import models
from task_category_model.models import TaskCategoryModel

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    Description = models.TextField()
    assign_date = models.DateField()
    task_category_model = models.ManyToManyField(TaskCategoryModel) 
    is_completed = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title}'