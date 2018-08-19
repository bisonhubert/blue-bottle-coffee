import pytest

from django.db import DataError, IntegrityError

from . import *

pytestmark = pytest.mark.django_db

class TestCafeModel:

    def test_fields(self, cafe_1):
        cafe_1.save()
        assert cafe_1.name == CAFE_NAME_US
        assert cafe_1.address == ADDRESS_US
        assert cafe_1.country == COUNTRY_US

    def test_name_required(self, cafe_1):
        cafe_1.name = None
        try:
            cafe_1.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: cafe_cafe.name'

    def test_address_required(self, cafe_1):
        cafe_1.address = None
        try:
            cafe_1.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: cafe_cafe.address'

    def test_country_iso_alpha_2_required(self, cafe_1):
        cafe_1.country = None
        try:
            cafe_1.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: cafe_cafe.country'

    def test_stringify(self, cafe_1):
        assert str(cafe_1) == cafe_1.name
