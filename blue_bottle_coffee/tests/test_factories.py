import pytest
from unittest.mock import Mock, patch

from ..api_client.factories import (CafeFactory, CategoryFactory,
                                    Factory, ItemFactory,
                                    ItemDetailFactory)
from ..cafe.models import Cafe
from ..item.models import Category, Item, ItemDetail
from . import (MOCK_CAFE_CONTENT, MOCK_CATEGORY_CONTENT,
    MOCK_ITEM_CONTENT, MOCK_ITEM_DETAILS_CONTENT)

pytestmark = pytest.mark.django_db


class TestFactories:

    def test_base_factory(self):
        instance = Mock()
        factory = Factory(content=Mock(), importer=Mock())
        assert factory
        assert factory.content
        assert factory.importer
        assert factory.get_or_create_instance(instance)

    def test_cafe_factory(self, data_importer):
        cafe_factory = CafeFactory(content=MOCK_CAFE_CONTENT, importer=data_importer)
        assert cafe_factory
        assert cafe_factory.content == MOCK_CAFE_CONTENT
        assert Cafe.objects.count() == 0
        cafe_factory.build()
        assert Cafe.objects.count() == 4

    def test_category_factory(self, data_importer):
        category_factory = CategoryFactory(content=MOCK_CATEGORY_CONTENT, 
            importer=data_importer)
        assert category_factory
        assert category_factory.content == MOCK_CATEGORY_CONTENT
        assert Category.objects.count() == 0
        category_factory.build()
        assert Category.objects.count() == 4

    def test_item_factory(self, data_importer, category_factory):
        categories = category_factory.build()
        item_factory = ItemFactory(content=MOCK_ITEM_CONTENT, 
            importer=data_importer)
        assert item_factory
        assert item_factory.content == MOCK_ITEM_CONTENT
        assert Item.objects.count() == 0
        item_factory.build(category_factory.instances)
        assert Item.objects.count() == 10

    def test_item_details_factory(self, data_importer, item_factory, category_factory):
        categories = category_factory.build()
        items = item_factory.build(category_factory.instances)
        item_details_factory = ItemDetailFactory(content=MOCK_ITEM_DETAILS_CONTENT,
            importer=data_importer)
        assert item_details_factory
        assert item_details_factory.content == MOCK_ITEM_DETAILS_CONTENT
        assert ItemDetail.objects.count() == 0
        item_details_factory.build(item_factory.instances)
        assert ItemDetail.objects.count() == 10
