import pytest
import requests

from unittest.mock import Mock, patch


class TestApiClient:

    @pytest.mark.parametrize('client', [
        (pytest.lazy_fixture('cafe_client')),
        (pytest.lazy_fixture('category_client')),
        (pytest.lazy_fixture('item_client')),
        (pytest.lazy_fixture('item_detail_en_client')),
        (pytest.lazy_fixture('item_detail_jp_client')),
    ])
    def test_endpoints_200(self, mock_get, client):
        mock_get.return_value.ok = True
        response = client.get_response()
        assert response
