from __future__ import annotations
from cleaner import clean_table
from normalizer import to_tidy
from validators import check_percentages




def main():
p = argparse.ArgumentParser()
p.add_argument('input_dir', help='Folder of PDFs')
p.add_argument('--company', required=True)
p.add_argument('--keywords', default='Saleable steel, EBITDA, Capex')
p.add_argument('--out', default='outputs')
args = p.parse_args()


keywords = [k.strip() for k in args.keywords.split(',')]
out_dir = Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)


tidy_all = []
for pdf in Path(args.input_dir).glob('*.pdf'):
pages = find_candidate_pages(str(pdf), keywords)
raw_tables = extract_tables(str(pdf), pages)
for t in raw_tables:
df = clean_table(t['table'])
if df.empty:
continue
tidy = to_tidy(df, company=args.company, source_file=pdf.name)
if not tidy.empty:
tidy_all.append(tidy)


if not tidy_all:
print('No tables found.')
return
final = pd.concat(tidy_all, ignore_index=True)
csv_path = out_dir / 'clean_tables.csv'
xlsx_path = out_dir / 'clean_tables.xlsx'
final.to_csv(csv_path, index=False)
final.to_excel(xlsx_path, index=False)
print(f'Wrote {csv_path} and {xlsx_path}')


if __name__ == '__main__':
main()
