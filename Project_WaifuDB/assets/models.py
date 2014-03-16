__author__ = 'Bakaboykie'

from django.db import models
import datetime
from django.utils import timezone

class Waifu(models.Model):

    picture = models.ImageField(upload_to='waifu_profile_picture')

    name_alphabet = models.CharField(max_length=100, verbose_name='Name')
    name_nickname = models.CharField(max_length=100, blank=True, verbose_name='Nickname')
    name_kanji = models.CharField(max_length=100, blank=True, verbose_name='Name in Kanji')
    name_hiragana = models.CharField(max_length=100, blank=True, verbose_name='Name in Hiragana')
    name_katakana = models.CharField(max_length=100, blank=True, verbose_name='Name in Katakana')

    waifu_birthday =  models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Birthday')
    waifu_age = models.IntegerField(blank=True, null=True, verbose_name='Age')
    waifu_sign = models.CharField(max_length=30, blank=True, verbose_name='Sign')
    waifu_job = models.CharField(max_length=150, blank=True, verbose_name='Job')

    A = 'A'
    B = 'B'
    AB = 'AB'
    O = 'O'
    blood_type_choices = (
        (A, 'Blood Type A'),
        (B, 'Blood Type B'),
        (AB, 'Blood Type AB'),
        (O, 'Blood type O')
    )

    blood_type = models.CharField(blank=True, max_length=2, choices=blood_type_choices, default=4, verbose_name='Blood Type')

    waifu_height = models.IntegerField(blank=True, null=True, verbose_name='Height (cm)')
    waifu_weight = models.IntegerField(blank=True, null=True, verbose_name='Weight (kg)')

    waifu_bust = models.IntegerField(blank=True, null=True, verbose_name='Bust Size (cm)')
    waifu_waist = models.IntegerField(blank=True, null=True, verbose_name='Waist Size (cm)')
    waifu_hip = models.IntegerField(blank=True, null=True, verbose_name='Hip Size (cm)')

    series_alphabet = models.CharField(max_length=100, blank=True, verbose_name='Series Name')
    series_japanese = models.CharField(max_length=100, blank=True, verbose_name='Series Name (Japanese)')

    waifu_description = models.TextField(max_length=10000, blank=True, verbose_name='Description')

    # This is not editable!
    date_uploaded = models.DateField(auto_now_add=False, null=True, verbose_name='Upload Date')

    # downloaded x times
    count_favorited = models.IntegerField(blank=True, null=True, verbose_name="Times Favorited")
    count_downloaded = models.IntegerField(blank=True, null=True, verbose_name="Times Downloaded")
    # mal page rip text
    # all other misc variables

    def admin_image(self):
        return '<img src="%s" style="max-height:130px;"/>' % self.picture.url
    admin_image.allow_tags = True

    def __str__(self):
        return self.name_alphabet

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_uploaded < now


class WaifuAssetClientPicture(models.Model):

    waifu = models.ForeignKey(Waifu)
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='waifu_pictures')

    file_checked = models.BooleanField(default=False)

    date_uploaded = models.DateField(auto_now_add=False, null=True, verbose_name='Upload Date')

    def admin_image(self):
        return '<img src="%s" style="max-height:100px;"/>' % self.picture.url
    admin_image.allow_tags = True


class WaifuAssetFileStorage(models.Model):

    waifu = models.ForeignKey(Waifu)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='waifu_files')

    file_checked = models.BooleanField(default=False)

    date_uploaded = models.DateField(auto_now_add=False, null=True, verbose_name='Upload Date')

    def admin_display(self):
        return '<a href="%s">%s</a>' % (self.file.url, self.file.name)
    admin_display.allow_tags = True