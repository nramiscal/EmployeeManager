from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    manager = models.ForeignKey(
        'self',
        related_name="employees",
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<User {self.id} {self.fname} Manager: {self.manager_id} >"
