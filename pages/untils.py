import streamlit as st
import pandas as pd

st.title("Обозначения и единицы измерения величин")

data = {
    'Параметр': [
        'Линейные размеры',
        'Площадь поперечного сечения', 
        'Относительное удлинение',
        'Относительное сужение',
        'Максимальное усилие разрыва',
        'Предел прочности'
    ],
    'Обозначение': [
        'l, d',
        'F',
        'δ',
        'ψ',
        'P',
        'σ'
    ],
    'Единицы измерения': [
        'мм',
        'мм²',
        '%',
        '%',
        'Н',
        'МПа'
    ]
}

df = pd.DataFrame(data)

st.markdown("Таблица условных обозначений")

st.dataframe(
    df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Параметр": st.column_config.TextColumn(width="medium"),
        "Обозначение": st.column_config.TextColumn(width="small"),
        "Единицы измерения": st.column_config.TextColumn(width="small")
    }
)