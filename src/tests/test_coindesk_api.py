import pytest
import requests
from src.config import URL_COINDESK
from src.service.get_today_date import get_today_date


class TestCoinDeskAPI:

    @classmethod
    def setup_class(cls):
        cls.response = requests.get(URL_COINDESK)
        cls.data = cls.response.json()

    def test_should_return_200(self):
        assert self.response.status_code == 200

    def test_should_return_a_json(self):
        assert isinstance(self.data, dict)

    def test_should_not_return_empty_disclaimer(self):
        disclaimer = self.data.get("disclaimer", None)
        assert disclaimer is not None and len(disclaimer) > 0

    def test_response_should_include_a_correct_chart_name(self):
        expected_chart_name = "Bitcoin"
        assert self.response.status_code == 200
        chart_name = self.data.get("chartName", None)
        assert chart_name == expected_chart_name

    def test_should_return_today_date_on_time_object(self):
        normal_date, formatter_date = get_today_date()
        assert self.response.status_code == 200
        time_values = self.data.get("time", {}).values()
        for values in time_values:
            assert str(normal_date) in values or str(formatter_date) in values

    def test_should_include_correct_currencies_on_body_response(self):
        currencies = ["USD", "GBP", "EUR"]
        assert self.response.status_code == 200
        currency_data = self.data.get("bpi", {})
        for currency_code in currency_data:
            assert currency_code in currencies

    def test_should_include_rate_on_body_response(self):
        assert self.response.status_code == 200
        currency_data = self.data.get("bpi", {})
        for values in currency_data.values():
            assert "rate" in values

    def test_should_include_rate_float_on_body_response(self):
        assert self.response.status_code == 200
        currency_data = self.data.get("bpi", {})
        for values in currency_data.values():
            assert "rate_float" in values

    def test_should_include_correct_currencies_symbol_encoding_on_body_response(self):
        expected_symbols = ["&#36;", "&pound;", "&euro;"]
        assert self.response.status_code == 200
        currency_data = self.data.get("bpi", {})
        for values in currency_data.values():
            symbol = values.get("symbol", "")
            assert symbol in expected_symbols
