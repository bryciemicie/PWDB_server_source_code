__author__ = 'Bakaboykie'

from django.contrib import admin
from Project_WaifuDB.assets.models import Waifu, WaifuAssetClientPicture, WaifuAssetFileStorage


class PictureInline(admin.TabularInline):
    model = WaifuAssetClientPicture
    fields = ['name', 'picture', 'date_uploaded']


class FileInline(admin.TabularInline):
    model = WaifuAssetFileStorage
    fields = ['name', 'file', 'date_uploaded']


class WaifuAdmin(admin.ModelAdmin):

    def relationships_count_picture(self, obj):
        return obj.waifuassetclientpicture_set.count()

    def relationships_count_file(self, obj):
        return obj.waifuassetfilestorage_set.count()

    relationships_count_picture.short_description = "Related Images"
    relationships_count_file.short_description = "Related Files"

    fieldsets = (
      ('Required fields', {
          'fields': (('picture', 'date_uploaded'), 'name_alphabet')
      }),
      ('Optional fields', {
          'fields': (
                     ('series_alphabet', 'series_japanese'),
                     'name_nickname',
                     'name_kanji',
                     'name_hiragana',
                     'name_katakana',
                     'waifu_birthday',
                      'waifu_age',
                      'waifu_sign',
                     'waifu_job',
                     'blood_type',
                     'waifu_height',
                     'waifu_weight',
                     ('waifu_bust', 'waifu_waist', 'waifu_hip'),
                     'waifu_description'
          )
      }),
   )


    list_display = (
        'admin_image',
        'name_alphabet',
        'name_kanji',
        'name_nickname',
        'waifu_age',
        'waifu_birthday',
        'waifu_height',
        'waifu_weight',
        'waifu_bust',
        'waifu_waist',
        'waifu_hip',
        'series_alphabet',
        'date_uploaded',
        'relationships_count_picture',
        'relationships_count_file',
    )

    inlines = [
        PictureInline,
        FileInline
    ]

admin.site.register(Waifu, WaifuAdmin)

################## UNCOMMENT FOR SEPARATE MODEL FIELDS IN ADMIN ###################
class WaifuAssetClientPictureAdmin(admin.ModelAdmin):
    list_display = ('waifu', 'admin_image', 'name', 'date_uploaded', 'file_checked')

class WaifuAssetFileStorageAdmin(admin.ModelAdmin):
    list_display = ('waifu', 'name', 'admin_display', 'date_uploaded', 'file_checked')

admin.site.register(WaifuAssetClientPicture, WaifuAssetClientPictureAdmin)
admin.site.register(WaifuAssetFileStorage, WaifuAssetFileStorageAdmin)
###################################################################################
