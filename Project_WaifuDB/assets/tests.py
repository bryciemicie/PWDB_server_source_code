"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.files import File
# import unittest
from Project_WaifuDB.assets.models import Waifu, WaifuAssetClientPicture, WaifuAssetFileStorage


class WaifuTestCase(TestCase):

    def setUp(self):

        self.waifu1 = Waifu.objects.create(
            picture=File(open("/files/waifu_testcase/test_profile.jpg")),
            name_alphabet="Testcase1",
            name_nickname="Testobject1",
            name_kanji="検査",
            name_hiragana="けんそ",
            name_katakana="テスト",
            waifu_birthday=None,
            waifu_age=10,
            waifu_sign="Test",
            waifu_job="Testing",
            blood_type="A",
            waifu_height=10,
            waifu_weight=10,
            waifu_bust=10,
            waifu_waist=10,
            waifu_hip=10,
            series_alphabet="Testcase Series 1",
            series_japanese="けんそ 1",
            waifu_description="Test description",
            date_uploaded=None,
            count_favorites=0,
            count_downloaded=0
        )

        self.waifu2 = Waifu.objects.create(
            picture=File(open("/files/waifu_testcase/test_profile.jpg")),
            name_alphabet="Testcase2",
            name_nickname="Testobject2",
            name_kanji="検査",
            name_hiragana="けんそ",
            name_katakana="テスト",
            waifu_birthday=None,
            waifu_age=10,
            waifu_sign="Test",
            waifu_job="Testing",
            blood_type="A",
            waifu_height=10,
            waifu_weight=10,
            waifu_bust=10,
            waifu_waist=10,
            waifu_hip=10,
            series_alphabet="Testcase Series 2",
            series_japanese="けんそ 2",
            waifu_description="Test description",
            date_uploaded=None,
            count_favorites=0,
            count_downloaded=0
        )

    def test_fileserving(self):
        resp = self.client.get("/files/waifu_profile_picture/test_profile.jpg")
        self.assertEqual(resp.status_code, 200)

