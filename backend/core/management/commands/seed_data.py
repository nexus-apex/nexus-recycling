from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Collection, RecycleMaterial, CollectionRoute
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusRecycling with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusrecycling.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Collection.objects.count() == 0:
            for i in range(10):
                Collection.objects.create(
                    collection_id=f"Sample {i+1}",
                    area=f"Sample {i+1}",
                    collection_type=random.choice(["residential", "commercial", "industrial"]),
                    driver=f"Sample {i+1}",
                    vehicle=f"Sample {i+1}",
                    scheduled_date=date.today() - timedelta(days=random.randint(0, 90)),
                    status=random.choice(["scheduled", "in_progress", "completed", "missed"]),
                    weight_kg=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 Collection records created'))

        if RecycleMaterial.objects.count() == 0:
            for i in range(10):
                RecycleMaterial.objects.create(
                    name=f"Sample RecycleMaterial {i+1}",
                    material_type=random.choice(["paper", "plastic", "glass", "metal", "e_waste", "organic"]),
                    rate_per_kg=round(random.uniform(1000, 50000), 2),
                    total_collected_kg=round(random.uniform(1000, 50000), 2),
                    recycled_kg=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["accepting", "full", "not_accepting"]),
                )
            self.stdout.write(self.style.SUCCESS('10 RecycleMaterial records created'))

        if CollectionRoute.objects.count() == 0:
            for i in range(10):
                CollectionRoute.objects.create(
                    name=f"Sample CollectionRoute {i+1}",
                    area=f"Sample {i+1}",
                    stops=random.randint(1, 100),
                    distance_km=round(random.uniform(1000, 50000), 2),
                    driver=f"Sample {i+1}",
                    vehicle=f"Sample {i+1}",
                    frequency=random.choice(["daily", "weekly", "biweekly", "monthly"]),
                    status=random.choice(["active", "suspended"]),
                )
            self.stdout.write(self.style.SUCCESS('10 CollectionRoute records created'))
