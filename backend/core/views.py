import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Collection, RecycleMaterial, CollectionRoute


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['collection_count'] = Collection.objects.count()
    ctx['collection_residential'] = Collection.objects.filter(collection_type='residential').count()
    ctx['collection_commercial'] = Collection.objects.filter(collection_type='commercial').count()
    ctx['collection_industrial'] = Collection.objects.filter(collection_type='industrial').count()
    ctx['collection_total_weight_kg'] = Collection.objects.aggregate(t=Sum('weight_kg'))['t'] or 0
    ctx['recyclematerial_count'] = RecycleMaterial.objects.count()
    ctx['recyclematerial_paper'] = RecycleMaterial.objects.filter(material_type='paper').count()
    ctx['recyclematerial_plastic'] = RecycleMaterial.objects.filter(material_type='plastic').count()
    ctx['recyclematerial_glass'] = RecycleMaterial.objects.filter(material_type='glass').count()
    ctx['recyclematerial_total_rate_per_kg'] = RecycleMaterial.objects.aggregate(t=Sum('rate_per_kg'))['t'] or 0
    ctx['collectionroute_count'] = CollectionRoute.objects.count()
    ctx['collectionroute_daily'] = CollectionRoute.objects.filter(frequency='daily').count()
    ctx['collectionroute_weekly'] = CollectionRoute.objects.filter(frequency='weekly').count()
    ctx['collectionroute_biweekly'] = CollectionRoute.objects.filter(frequency='biweekly').count()
    ctx['collectionroute_total_distance_km'] = CollectionRoute.objects.aggregate(t=Sum('distance_km'))['t'] or 0
    ctx['recent'] = Collection.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def collection_list(request):
    qs = Collection.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(collection_id__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(collection_type=status_filter)
    return render(request, 'collection_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def collection_create(request):
    if request.method == 'POST':
        obj = Collection()
        obj.collection_id = request.POST.get('collection_id', '')
        obj.area = request.POST.get('area', '')
        obj.collection_type = request.POST.get('collection_type', '')
        obj.driver = request.POST.get('driver', '')
        obj.vehicle = request.POST.get('vehicle', '')
        obj.scheduled_date = request.POST.get('scheduled_date') or None
        obj.status = request.POST.get('status', '')
        obj.weight_kg = request.POST.get('weight_kg') or 0
        obj.save()
        return redirect('/collections/')
    return render(request, 'collection_form.html', {'editing': False})


@login_required
def collection_edit(request, pk):
    obj = get_object_or_404(Collection, pk=pk)
    if request.method == 'POST':
        obj.collection_id = request.POST.get('collection_id', '')
        obj.area = request.POST.get('area', '')
        obj.collection_type = request.POST.get('collection_type', '')
        obj.driver = request.POST.get('driver', '')
        obj.vehicle = request.POST.get('vehicle', '')
        obj.scheduled_date = request.POST.get('scheduled_date') or None
        obj.status = request.POST.get('status', '')
        obj.weight_kg = request.POST.get('weight_kg') or 0
        obj.save()
        return redirect('/collections/')
    return render(request, 'collection_form.html', {'record': obj, 'editing': True})


@login_required
def collection_delete(request, pk):
    obj = get_object_or_404(Collection, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/collections/')


@login_required
def recyclematerial_list(request):
    qs = RecycleMaterial.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(material_type=status_filter)
    return render(request, 'recyclematerial_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def recyclematerial_create(request):
    if request.method == 'POST':
        obj = RecycleMaterial()
        obj.name = request.POST.get('name', '')
        obj.material_type = request.POST.get('material_type', '')
        obj.rate_per_kg = request.POST.get('rate_per_kg') or 0
        obj.total_collected_kg = request.POST.get('total_collected_kg') or 0
        obj.recycled_kg = request.POST.get('recycled_kg') or 0
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/recyclematerials/')
    return render(request, 'recyclematerial_form.html', {'editing': False})


@login_required
def recyclematerial_edit(request, pk):
    obj = get_object_or_404(RecycleMaterial, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.material_type = request.POST.get('material_type', '')
        obj.rate_per_kg = request.POST.get('rate_per_kg') or 0
        obj.total_collected_kg = request.POST.get('total_collected_kg') or 0
        obj.recycled_kg = request.POST.get('recycled_kg') or 0
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/recyclematerials/')
    return render(request, 'recyclematerial_form.html', {'record': obj, 'editing': True})


@login_required
def recyclematerial_delete(request, pk):
    obj = get_object_or_404(RecycleMaterial, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/recyclematerials/')


@login_required
def collectionroute_list(request):
    qs = CollectionRoute.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(frequency=status_filter)
    return render(request, 'collectionroute_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def collectionroute_create(request):
    if request.method == 'POST':
        obj = CollectionRoute()
        obj.name = request.POST.get('name', '')
        obj.area = request.POST.get('area', '')
        obj.stops = request.POST.get('stops') or 0
        obj.distance_km = request.POST.get('distance_km') or 0
        obj.driver = request.POST.get('driver', '')
        obj.vehicle = request.POST.get('vehicle', '')
        obj.frequency = request.POST.get('frequency', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/collectionroutes/')
    return render(request, 'collectionroute_form.html', {'editing': False})


@login_required
def collectionroute_edit(request, pk):
    obj = get_object_or_404(CollectionRoute, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.area = request.POST.get('area', '')
        obj.stops = request.POST.get('stops') or 0
        obj.distance_km = request.POST.get('distance_km') or 0
        obj.driver = request.POST.get('driver', '')
        obj.vehicle = request.POST.get('vehicle', '')
        obj.frequency = request.POST.get('frequency', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/collectionroutes/')
    return render(request, 'collectionroute_form.html', {'record': obj, 'editing': True})


@login_required
def collectionroute_delete(request, pk):
    obj = get_object_or_404(CollectionRoute, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/collectionroutes/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['collection_count'] = Collection.objects.count()
    data['recyclematerial_count'] = RecycleMaterial.objects.count()
    data['collectionroute_count'] = CollectionRoute.objects.count()
    return JsonResponse(data)
