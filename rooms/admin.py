from django.contrib import admin
from . import models
from django.utils.html import mark_safe

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    # room의 FK photos admin?을 room admint에서 보여줌
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        ("Space", {"fields": ("guests", "beds", "bedrooms", "baths",)},),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules",),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("price",)

    list_filter = (
        "host__superhost",
        "city",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    # host 행을 id로 보여줌 host명이 아니라
    raw_id_fields = ("host",)

    search_fields = ["=city", "^host__username"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    # super()는 상위 클래스에 접속함, admin을 control, 누가 admin에서 수정했는지 알수있음
    """
    def save_model(self, request, obj, form, change):
        print(obj, change, form)
        super().save_model(request, obj, form, change)
    """

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "count_amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        # 이미지 파일로 보이게 해줌 장고의 mark_safe로 security 처리 막음
        return mark_safe(f'<img width = "50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
