import pytest

from . import *

from ..cafe.models import Cafe
from ..item.models import Category, Item, ItemDetail

@pytest.fixture
def cafe_1():
    cafe = Cafe.objects.create(
        name=CAFE_NAME_US, 
        address=ADDRESS_US, 
        country=COUNTRY_US)
    return cafe

@pytest.fixture
def cafe_2():
    cafe = Cafe.objects.create(
        name=CAFE_NAME_JP, 
        address=ADDRESS_JP, 
        country=COUNTRY_JP)
    return cafe

@pytest.fixture
def category_1():
    category = Category.objects.create(
        name=CATEGORY_NAME_1)
    return category

@pytest.fixture
def category_2(category_1):
    category = Category.objects.create(
        name=CATEGORY_NAME_2,
        parent=category_1)
    return category

@pytest.fixture
def item(category_1):
    item = Item.objects.create(
        sku=ITEM_SKU,
        category=category_1)
    return item

@pytest.fixture
def item_detail(item):
    item_detail = ItemDetail.objects.create(
        item=item,
        name=ITEM_NAME,
        price=ITEM_PRICE,
        currency=ITEM_CURRENCY)
    return item_detail
