from .clients import Client, CountryClient
from ..cafe.models import Cafe
from ..item.models import Category, Item, ItemDetail

class Factory(object):

    def __init__(self, **kwargs):
        self.instances = None
        self.content = kwargs.get('content')
        self.importer = kwargs.get('importer')

    def get_or_create_instance(self, instance):
        # import pdb
        # pdb.set_trace()
        instance = self.importer.attempt_save(instance)
        if self.instances:
            self.instances.append(instance)
        else:
            self.instances = [instance]
        return instance


class CafeFactory(Factory):

    def get_fields(self, cafe):
        return {
            'name': cafe.get('name'),
            'address': cafe.get('address'),
            'country': cafe.get('countryIsoAlpha2'),
        }
    
    def build(self):
        for cafe in self.content:
            instance = Cafe(**self.get_fields(cafe))
            self.get_or_create_instance(instance)
        return self.instances


class CategoryFactory(Factory):

    def get_fields(self, category):
        return {
            'name': category.get('name'),
        }

    def build(self):
        for category in self.content:
            instance = Category(**self.get_fields(category))
            self.get_or_create_instance(instance)
        return self.instances


class ItemFactory(Factory):

    def get_category(self, item, categories):
        category_list = [category for category in categories 
            if category.name.lower() == item.get('category').lower()]
        return category_list[0] if category_list else None

    def get_fields(self, item, category):
        return {
            'sku': item.get('sku'),
            'category': category,
        }

    def build(self, categories=None):
        for item in self.content:
            category = self.get_category(item, categories) if categories else None
            instance = Item(**self.get_fields(item, category))
            self.get_or_create_instance(instance)
        return self.instances


class ItemDetailFactory(Factory):

    def get_item(self, details, items):
        items_list = [item for item in items
            if item.sku.lower() == details.get('sku').lower()]
        return items_list[0] if items_list else None

    def get_fields(self, details, item):
        return {
            'item': item,
            'name': details.get('name'),
            'price': details.get('price'),
            'currency': details.get('currency'),
        }

    def build(self, items):
        for details in self.content:
            item = self.get_item(details, items)
            instance = ItemDetail(**self.get_fields(details, item))
            self.get_or_create_instance(instance)
        return self.instances

