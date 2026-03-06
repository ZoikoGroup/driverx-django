from django.db import models


class JobApplication(models.Model):

    POSITION_CHOICES = [
        ("sales_marketing", "Sales & Marketing"),
        ("customer_support", "Customer Support"),
        ("technology_dev", "Technology & Development"),
        ("operations_mgmt", "Operations & Management"),
        ("business_dev", "Business Development"),
        ("field_sales", "Field Sales"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    position_applied = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES
    )

    resume = models.FileField(upload_to="resumes/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_position_applied_display()}"