# Annual-Report-Table-Miner
Pull key tables (volumes, costs, capex) from company PDFs and turn them into clean, analysis-ready CSVs with one click.

## Annual-Report Table Miner (Python + PDF → Clean CSV/Excel)
Extracts tabular data from annual reports / investor PDFs, cleans headers & units, normalizes schema, validates totals/percentages, and exports a tidy dataset. Comes with a Streamlit UI for one‑click use.


### Why this project?
Analysts waste time copy‑pasting tables from PDFs. This tool automates: detect → extract → clean → normalize → validate → export.


### Features
- Auto page‑finder via keyword scan (e.g., "Saleable Steel", "EBITDA", "Capex").
- Robust extraction using `pdfplumber`; optional `camelot` fallback.
- Header repair: multi‑row headers merged, footnotes stripped.
- Unit normalization: ₹, ₹ Cr, ₹ Mn → consistent base.
- Schema normalizer → tidy table: `company, source_file, fy, metric, submetric, unit, value`.
- Data validation: totals ≈ sum of parts, % columns in [0, 100], non‑negatives.
- Streamlit app: drag‑and‑drop PDFs, preview, export CSV/Excel, audit JSON.


### Tech Stack
- Python 3.10+
- pdfplumber, pandas, regex, openpyxl, streamlit

### Quickstart
```bash
# 1) Create env
python -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate


# 2) Install
pip install -r requirements.txt


# 3) Run the UI
streamlit run app.py


# 4) Or run CLI
python -m cli input_pdfs/ --company "SAIL" --keywords "Saleable steel, EBITDA, Capex" --out outputs/
```


### Repo Structure
```
annual-report-table-miner/
app.py # Streamlit web UI
cli.py # Simple CLI wrapper
extractor.py # pdf→raw tables
cleaner.py # header fix, type/unit cleanup
normalizer.py # map → tidy schema
validators.py # sanity checks & audit log
utils.py # helpers (units, fuzzy match, io)
config/
keywords.yml # default keyword sets per domain/company
templates.yml # optional per-company header->schema maps
data_samples/ # put sample PDFs here (not included)
outputs/ # CSV/Excel/audit logs written here
tests/
test_units.py
test_headers.py
requirements.txt


### How it works (pipeline)
1. **Scan**: search each page for any keyword hit → candidate pages.
2. **Extract**: use `pdfplumber` to pull tables; if none found, try `camelot` (lattice/stream).
3. **Clean**: merge multi‑row headers; drop empty cols/rows; coerce dtypes; normalize units.
4. **Normalize**: reshape to tidy rows and standard column names.
5. **Validate**: compute audit checks; flag issues with row references.
6. **Export**: CSV, Excel; JSON audit report; preview in Streamlit.
