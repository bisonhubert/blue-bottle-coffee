import pytest

from django.db import IntegrityError

from . import *

pytestmark = pytest.mark.django_db

class TestCategoryModel:

    def test_fields(self, category_1, category_2):
        assert category_2.name == CATEGORY_NAME_2
        assert category_2.parent == category_1

    def test_name_required(self, category_1):
        category_1.name = None
        try:
            category_1.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: item_category.name'

    def test_parent_null(self, category_2):
        category_2.parent = None
        category_2.save()
        assert not category_2.parent

    def test_stringify(self, category_1):
        assert str(category_1) == CATEGORY_NAME_1
