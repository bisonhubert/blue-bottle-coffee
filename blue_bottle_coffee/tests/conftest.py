import pytest

from . import *

from ..api_client.clients import Client, CountryClient
from ..api_client.factories import CategoryFactory, ItemFactory
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

@pytest.fixture
def cafe_client():
    return Client(model=CAFE)

@pytest.fixture
def category_client():
    return Client(model=CATEGORY)

@pytest.fixture
def item_client():
    return Client(model=ITEM)

@pytest.fixture
def item_detail_en_client():
    return CountryClient(model=ITEM_DETAILS, language_code=LANGUAGE_CODE_US)

@pytest.fixture
def item_detail_jp_client():
    return CountryClient(model=ITEM_DETAILS, language_code=LANGUAGE_CODE_JP)

@pytest.fixture
def data_importer():
    class DummyImportHelper(object):
        def run_import(self, import_data):
            import_data()

        def attempt_save(self, instance):
            try:
                instance.save()
            except:
                raise
            return instance

    return DummyImportHelper()


@pytest.fixture
def category_factory(data_importer):    
    return CategoryFactory(content=MOCK_CATEGORY_CONTENT,
        importer=data_importer)


@pytest.fixture
def item_factory(data_importer):
    return ItemFactory(content=MOCK_ITEM_CONTENT,
        importer=data_importer)
