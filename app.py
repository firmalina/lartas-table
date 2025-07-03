import streamlit as st
import pandas as pd

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRVqk7MUM0uwmOAq-FQZHVVhXrztOrR56vC-xn1JGQLbRK4q2XtG7YlNZgJlOlyb5rFUsNW5Ks3bvmA/pub?output=csv"

data = pd.read_csv(CSV_URL)

st.markdown("<h2 style='font-weight: bold;'>Daftar Barang Lartas</h2>", unsafe_allow_html=True)

hide_table_row_index = """
    <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
    </style>
"""
st.markdown(hide_table_row_index, unsafe_allow_html=True)

styled_table = data.style.set_table_styles([
    {'selector': 'th', 'props': [('font-weight', 'bold'), ('background-color', '#f2f2f2'), ('padding', '8px')]}
])

st.write(styled_table.to_html(escape=False), unsafe_allow_html=True)

st.markdown("<p style='font-size:12px; color:gray;'>Made with love by Malika.</p>", unsafe_allow_html=True)
