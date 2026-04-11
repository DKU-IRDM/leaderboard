from django.contrib import admin

from import_export import resources  # type: ignore
from import_export.admin import ImportExportModelAdmin  # type: ignore

from web.models import (
    Record26SpDbA2,
    Record26SpDbA3,
)


class Record26SpDbA2Resource(resources.ModelResource):

    class Meta:
        model = Record26SpDbA2
        fields = ('sid', 'similarity', 'latency')


@admin.register(Record26SpDbA2)
class Record26SpDBAdmin(ImportExportModelAdmin):

    resource_class = Record26SpDbA2Resource
    list_display = ('sid', 'similarity', 'latency', 'created_at', 'updated_at')
    search_fields = ('sid',)


class Record26SpDbA3Resource(resources.ModelResource):

    class Meta:
        model = Record26SpDbA3
        fields = ('sid', 'score')


@admin.register(Record26SpDbA3)
class Record26SpDbA3Admin(ImportExportModelAdmin):

    resource_class = Record26SpDbA3Resource
    list_display = ('sid', 'score', 'created_at', 'updated_at')
    search_fields = ('sid',)
