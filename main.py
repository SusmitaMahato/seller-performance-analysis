import db_setup
from analysis import load_data, analyze
from visualize import show_charts

df = load_data()
analyze(df)
show_charts(df)