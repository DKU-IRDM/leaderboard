from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import (
    F,
    Window,
)
from django.db.models.functions import Rank
from django.views.decorators.csrf import csrf_exempt

from api.settings import (
    APP_PASSWORD,
    WEB_PASSWORD,
)
from web.models import (
    Record26SpDbA2,
    Record26SpDbA3,
)


def star(text, last):
    return '*' * (len(text) - last) + text[-last:]


@csrf_exempt
def api_records_26SpDbA2_view(request):
    if request.method != 'POST':
        return JsonResponse({}, status=405)
    password = request.POST.get('password')
    if password != APP_PASSWORD:
        return JsonResponse({}, status=401)
    sid = request.POST.get('sid')
    similarity = request.POST.get('similarity')
    latency = request.POST.get('latency')
    record, _ = Record26SpDbA2.objects.get_or_create(sid=sid)
    record.similarity = similarity
    record.latency = latency
    record.save()
    return JsonResponse({}, status=200)


@csrf_exempt
def api_records_26SpDbA3_view(request):
    if request.method != 'POST':
        return JsonResponse({}, status=405)
    password = request.POST.get('password')
    if password != APP_PASSWORD:
        return JsonResponse({}, status=401)
    sid = request.POST.get('sid')
    score = request.POST.get('score')
    record, _ = Record26SpDbA3.objects.get_or_create(sid=sid)
    record.score = score
    record.save()
    return JsonResponse({}, status=200)


def web_26SpDbA2_view(request):
    password = request.GET.get('password')
    if password != WEB_PASSWORD:
        return render(request, 'na.html')
    records = Record26SpDbA2.objects.annotate(
        rank=Window(
            expression=Rank(),
            order_by=[
                F('similarity').desc(),
                F('latency').asc(),
            ],
        ),
    ).order_by('-similarity', 'latency', 'sid')
    rows = []
    for record in records:
        rows.append({
            'rank': record.rank,
            'sid': star(record.sid, 4),
            'similarity': record.similarity,
            'latency': record.latency,
            'updated_at': record.updated_at,
        })
    return render(request, 'views/26SpDbA2.html', {
        'rows': rows,
    })


def web_26SpDbA3_view(request):
    password = request.GET.get('password')
    if password != WEB_PASSWORD:
        return render(request, 'na.html')
    records = Record26SpDbA3.objects.annotate(
        rank=Window(
            expression=Rank(),
            order_by=[
                F('score').desc(),
            ],
        ),
    ).order_by('-score', 'sid')
    rows = []
    for record in records:
        rows.append({
            'rank': record.rank,
            'sid': star(record.sid, 4),
            'score': record.score,
            'updated_at': record.updated_at,
        })
    return render(request, 'views/26SpDbA3.html', {
        'rows': rows,
    })
