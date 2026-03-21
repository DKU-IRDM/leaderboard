from django.urls import path

from web.views import (
    api_records_26SpDbA2_view,
    web_26SpDbA2_view,
)


urlpatterns = [
    path('api/records/26SpDbA2/', api_records_26SpDbA2_view),
    path('26SpDbA2/', web_26SpDbA2_view),
]
