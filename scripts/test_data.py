import decimal
import logging
import os
import sys

from decimal import Decimal
from django.db import transaction

from blue_bottle_coffee.constants import *

logger = logging.getLogger(__name__)


class BasicImportHelper(object):

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def attempt_save(self, instance):
        try:
            instance.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(instance.__class__)
            print(" ")
            print(instance.__dict__)
            print(" ")
            print(instance)
            print(" ")
            print("---------------")

            instance = self.locate_object(instance)
        return instance


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper), {})()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)


def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()


def import_data():
    # from blue_bottle_coffee.constants import (LANGUAGE_CODE_JPN, LANGUAGE_CODE_US)
    
    # Client import
    from blue_bottle_coffee.api_client.clients import Client, CountryClient

    cafe_content = Client(model='cafes').get_content()
    categories_content = Client(model='item_categories').get_content()
    item_content = Client(model='items').get_content()
    item_details_jp = CountryClient(model='item_details', 
        language_code=LANGUAGE_CODE_JPN).get_content()
    item_details_us = CountryClient(model='item_details', 
        language_code=LANGUAGE_CODE_US).get_content()

    from blue_bottle_coffee.api_client.factories import (CafeFactory,
        CategoryFactory, ItemFactory, ItemDetailFactory)
    
    cafe_factory = CafeFactory(content=cafe_content, importer=importer)
    cafe_factory.build()

    category_factory = CategoryFactory(content=categories_content, 
        importer=importer)
    category_factory.build()

    item_factory = ItemFactory(content=item_content, importer=importer)
    item_factory.build(categories=category_factory.instances)

    item_details_jp = ItemDetailFactory(content=item_details_jp, importer=importer)
    item_details_jp.build(item_factory.instances)

    item_details_us = ItemDetailFactory(content=item_details_us, importer=importer)
    item_details_us.build(item_factory.instances)
