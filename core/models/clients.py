from django.db import models


class Client(models.Model):
    f_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        "CustomUser", on_delete=models.SET_NULL,
        null=True, related_name="clients")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name

    class Meta:
        ordering = ("-id",)
