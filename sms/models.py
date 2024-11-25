from django.db import models

# Create your models here.

class SMSRecord(models.Model):
    recipient = models.CharField(max_length=15)  # Store phone numbers
    message = models.TextField()
    status = models.CharField(max_length=20, default="Pending")  # Track status (e.g., Sent, Failed)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.recipient}, Status: {self.status}"
