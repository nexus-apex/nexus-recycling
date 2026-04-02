from django.contrib import admin
from .models import Collection, RecycleMaterial, CollectionRoute

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["collection_id", "area", "collection_type", "driver", "vehicle", "created_at"]
    list_filter = ["collection_type", "status"]
    search_fields = ["collection_id", "area", "driver"]

@admin.register(RecycleMaterial)
class RecycleMaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "material_type", "rate_per_kg", "total_collected_kg", "recycled_kg", "created_at"]
    list_filter = ["material_type", "status"]
    search_fields = ["name"]

@admin.register(CollectionRoute)
class CollectionRouteAdmin(admin.ModelAdmin):
    list_display = ["name", "area", "stops", "distance_km", "driver", "created_at"]
    list_filter = ["frequency", "status"]
    search_fields = ["name", "area", "driver"]
