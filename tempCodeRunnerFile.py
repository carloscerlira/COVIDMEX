df = tabula.read_pdf('data/mexico.pdf', pages='all',  output_format='dataframe', multiple_tables=False)
# df[0].to_csv('data/covidmxraw.csv')
