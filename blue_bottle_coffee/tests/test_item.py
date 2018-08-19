import pytest

from django.db import IntegrityError

from . import *
from ..item.models import Category, Item, ItemDetail

pytestmark = pytest.mark.django_db

class TestItemModel:

    def test_fields(self, item, category_1):
        assert item.sku == ITEM_SKU
        assert item.category == category_1

    def test_sku_required(self, item):
        item.sku = None
        try:
            item.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: item_item.sku'

    def test_sku_uniqueness(self, item):
        item_2 = Item(sku=item.sku)
        try:
            item_2.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: item_item.category_id'        

    def test_category_required(self, item):
        item.category = None
        try:
            item.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: item_item.category_id'

    def test_cascade_on_delete_category(self, item, category_1):
        assert Item.objects.count() == 1
        assert Category.objects.count() == 1
        category_1.delete()
        assert Item.objects.count() == 0
        assert Category.objects.count() == 0

    def test_stringify(self, item):
        assert str(item) == ITEM_SKU



class TestItemDetailModel:

    def test_fields(self, item, item_detail):
        assert item_detail.name == ITEM_NAME
        assert item_detail.price == ITEM_PRICE
        assert item_detail.currency == ITEM_CURRENCY
        assert item_detail.item == item

    def test_name_required(self, item_detail):
        item_detail.name = None
        try:
            item_detail.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: item_itemdetail.name'

    def test_price_required(self, item_detail):
        item_detail.price = None
        try:
            item_detail.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: item_itemdetail.price'

    def test_currency_required(self, item_detail):
        item_detail.currency = None
        try:
            item_detail.save()
        except IntegrityError as e:
            assert str(e) == 'NOT NULL constraint failed: item_itemdetail.currency'

    def test_cascade_on_delete_item(self, item, item_detail):
        assert Item.objects.count() == 1
        assert ItemDetail.objects.count() == 1
        item.delete()
        assert Item.objects.count() == 0
        assert ItemDetail.objects.count() == 0

    def test_stringify(self, item_detail):
        assert str(item_detail) == ITEM_NAME

    def test_get_dollar_amount(self, item_detail):
        assert item_detail.get_dollar_amount().default_currency == ITEM_CURRENCY
