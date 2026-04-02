from django.db import models

class Collection(models.Model):
    collection_id = models.CharField(max_length=255)
    area = models.CharField(max_length=255, blank=True, default="")
    collection_type = models.CharField(max_length=50, choices=[("residential", "Residential"), ("commercial", "Commercial"), ("industrial", "Industrial")], default="residential")
    driver = models.CharField(max_length=255, blank=True, default="")
    vehicle = models.CharField(max_length=255, blank=True, default="")
    scheduled_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("scheduled", "Scheduled"), ("in_progress", "In Progress"), ("completed", "Completed"), ("missed", "Missed")], default="scheduled")
    weight_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.collection_id

class RecycleMaterial(models.Model):
    name = models.CharField(max_length=255)
    material_type = models.CharField(max_length=50, choices=[("paper", "Paper"), ("plastic", "Plastic"), ("glass", "Glass"), ("metal", "Metal"), ("e_waste", "E Waste"), ("organic", "Organic")], default="paper")
    rate_per_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_collected_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    recycled_kg = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("accepting", "Accepting"), ("full", "Full"), ("not_accepting", "Not Accepting")], default="accepting")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class CollectionRoute(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255, blank=True, default="")
    stops = models.IntegerField(default=0)
    distance_km = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    driver = models.CharField(max_length=255, blank=True, default="")
    vehicle = models.CharField(max_length=255, blank=True, default="")
    frequency = models.CharField(max_length=50, choices=[("daily", "Daily"), ("weekly", "Weekly"), ("biweekly", "Biweekly"), ("monthly", "Monthly")], default="daily")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("suspended", "Suspended")], default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
