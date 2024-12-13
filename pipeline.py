from le_arquivo import extract_data, transform_data, load_data

df = extract_data('data', 'json')
df = transform_data(df, 'idade', 'new')
load_data(df, ['csv','parquet'])