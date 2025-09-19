from cleaner import _merge_header_rows


def test_merge_headers():
rows = [
['Metric', 'FY23', 'FY24'],
['', '(₹ Cr)', '(₹ Cr)']
]
merged = _merge_header_rows(rows, 2)
assert merged == ['Metric', 'FY23 (₹ Cr)', 'FY24 (₹ Cr)']
