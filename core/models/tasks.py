from django.db import models


class Task(models.Model):
    STATUS = (
        ('new', 'new'),
        ('progres', 'progres'),
        ('completed', 'completed')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(
        "CustomUser", on_delete=models.SET_NULL,
        null=True, related_name="assigned_to_employee"
    )
    created_by = models.ForeignKey(
        "CustomUser", on_delete=models.SET_NULL,
        null=True, related_name="created_by_task"
    )
    status = models.CharField(max_length=100, choices=STATUS, default='new')
    deadline = models.DateTimeField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-id",)
