import pytest
from utils import to_number, detect_unit, normalize_fy


def test_to_number_basic():
assert to_number('1,234.50') == 1234.5
assert to_number('(1,000)') == -1000
assert to_number('-') is None




def test_detect_unit():
u = detect_unit('₹ in Crore')
assert u.is_currency and u.scale_to_cr == 1.0




def test_normalize_fy():
assert normalize_fy('FY24') == 'FY2024/2025'
assert normalize_fy("FY'23-24") == 'FY2023/2024'
