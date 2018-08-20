# Cafes
CAFE_NAME_US = "W.C. Morse"
CAFE_NAME_JP = "Aoyama"
ADDRESS_US = "4270 Broadway, Oakland, CA 94611"
ADDRESS_JP = "3-13-14 Minamiaoyama Minato-ku, Tokyo 107-0062"
COUNTRY_US = "US"
COUNTRY_JP = "JP"

# Category
CATEGORY_NAME_1 = "Beverage"
CATEGORY_NAME_2 = "Coffee Bean"

# Item
ITEM_SKU = "BV-CAP"

# Item Detail
ITEM_NAME = "Cappuccino"
ITEM_PRICE = "3.75"
ITEM_CURRENCY = "USD"

# Client Types
CAFE = 'cafes'
CATEGORY = 'item_categories'
ITEM = 'items'
ITEM_DETAILS = 'item_details'
LANGUAGE_CODE_US = 'en-US'
LANGUAGE_CODE_JP = 'ja-JP'

# Factories
MOCK_CAFE_CONTENT = [
  {"name": "W.C. Morse", "address": "4270 Broadway, Oakland, CA 94611", "countryIsoAlpha2": "US"},
  {"name": "Old Oakland", "address": "480 9th Street, Oakland, CA 94607", "countryIsoAlpha2": "US"},
  {"name": "Aoyama", "address": "3-13-14 Minamiaoyama Minato-ku, Tokyo 107-0062", "countryIsoAlpha2": "JP"},
  {"name": "Nakameguro", "address": "3-23-16 Nakameguro Meguro-ku, Tokyo 153-0061", "countryIsoAlpha2": "JP"}
]
MOCK_CATEGORY_CONTENT = [
  {"name": "Beverage"},
  {"name": "Baked Product"},
  {"name": "Coffee Equipment"},
  {"name": "Coffee Bean"}
]
MOCK_ITEM_CONTENT = [
  {"sku": "BV-CAP", "category": "Beverage"},
  {"sku": "BV-LATTE", "category": "Beverage"},
  {"sku": "BV-ESP", "category": "Beverage"},
  {"sku": "BV-DRIP", "category": "Beverage"},
  {"sku": "BP-SRW-BCKL", "category": "Baked Product"},
  {"sku": "BP-BLGN-WFFL", "category": "Baked Product"},
  {"sku": "CE-CFF-DRP", "category": "Coffee Equipment"},
  {"sku": "CE-BRTZ-CF-GRN", "category": "Coffee Equipment"},
  {"sku": "CB-BL-DNVN", "category": "Coffee Bean"},
  {"sku": "CB-BRN-KNZ", "category": "Coffee Bean"}
]
MOCK_ITEM_DETAILS_CONTENT = [
  {"sku": "BV-CAP", "name": "Cappuccino", "price": "3.75", "currency": "USD"},
  {"sku": "BV-LATTE", "name": "Latte", "price": "4.25", "currency": "USD"},
  {"sku": "BV-ESP", "name": "Espresso", "price": "3.00", "currency": "USD"},
  {"sku": "BV-DRIP", "name": "Drip Coffee", "price": "4.00", "currency": "USD"},
  {"sku": "BP-SRW-BCKL", "name": "Strawberry Buckle", "price": "4.00", "currency": "USD"},
  {"sku": "BP-BLGN-WFFL", "name": "Belgian Waffle", "price": "9.00", "currency": "USD"},
  {"sku": "CE-CFF-DRP", "name": "Coffee Dripper", "price": "25.00", "currency": "USD"},
  {"sku": "CE-BRTZ-CF-GRN", "name": "Baratza Coffee Grinder", "price": "139.00", "currency": "USD"},
  {"sku": "CB-BL-DNVN", "name": "Bella Donovan", "price": "17.00", "currency": "USD"},
  {"sku": "CB-BRN-KNZ", "name": "Burundi Kayanza", "price": "24.00", "currency": "USD"}
]
