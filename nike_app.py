# ============================================================
# 📊 STREAMLIT APP – ANÁLISIS INTEGRAL DE INVERSIÓN NIKE (NKE)
# ============================================================

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Análisis Integral de Inversión: NIKE (NKE)",
    page_icon="👟",
    layout="wide"
)

st.sidebar.title("📘 Menú de Navegación")
page = st.sidebar.radio(
    "Ir a:",
    ["Introducción", "Análisis Fundamental", "Análisis Técnico", "Conclusión Ejecutiva"]
)

st.title("👟 Análisis Integral de Inversión: NIKE, Inc. (NKE)")
st.caption("Informe híbrido basado en análisis fundamental y técnico. Datos: Form 10-K FY2023 + Yahoo Finance TTM 2024.")

if page == "Introducción":
    st.header("1. Introducción")
    st.write(
        "Este análisis combina un enfoque fundamental (salud financiera y valoración) con un enfoque técnico "
        "(tendencia y momentum) para evaluar la conveniencia de invertir en las acciones de NIKE (NKE). "
        "Se utilizan datos del Form 10-K FY 2023 y métricas actualizadas de Yahoo Finance (TTM 2024)."
    )

elif page == "Análisis Fundamental":
    st.header("2. Análisis Fundamental")
    st.write("Comparativa de ratios entre el Form 10-K FY2023 y los datos TTM de Yahoo Finance.")
    st.table({
        "Indicador": [
            "Precio actual",
            "Book Value por acción",
            "EPS",
            "PER",
            "ROE",
            "Deuda/Patrimonio"
        ],
        "Form 10-K FY2023": [
            "64.59 USD",
            "14.2 USD",
            "3.31 USD",
            "19.5",
            "23.3 %",
            "41 %"
        ],
        "Yahoo Finance TTM 2024": [
            "64.59 USD",
            "9.118 USD",
            "1.95 USD",
            "33.1",
            "21 %",
            "82 %"
        ],
    })
    st.info(
        "**Fórmulas**\n"
        "- Book Value = Patrimonio / Nº de acciones\n"
        "- EPS = Beneficio neto / Nº de acciones\n"
        "- PER = Precio / EPS\n"
        "- ROE = Beneficio / Patrimonio\n"
        "- D/E = Deuda total / Patrimonio"
    )

elif page == "Análisis Técnico":
    st.header("3. Análisis Técnico")
    st.write("Indicadores usados: RSI(14), EMA(40) y SMA(200).")

    # Mostrar imágenes si existen
    try:
        st.subheader("📈 Precio histórico (1980–2025)")
        st.image("data/nike_hist.png", use_column_width=True)
        st.caption("Tendencia estructuralmente alcista en escala logarítmica.")
    except Exception:
        st.warning("No se encontró 'data/nike_hist.png'. Súbelo a la carpeta data/.")

    try:
        st.subheader("📊 Precio con EMA(40) y SMA(200)")
        st.image("data/nike_ma.png", use_column_width=True)
        st.caption("EMA(40) → corto/medio plazo | SMA(200) → tendencia principal.")
    except Exception:
        st.warning("No se encontró 'data/nike_ma.png'. Súbelo a la carpeta data/.")

    try:
        st.subheader("📉 RSI(14)")
        st.image("data/nike_rsi.png", use_column_width=True)
        st.caption("RSI > 70 → sobrecompra; RSI < 30 → sobreventa.")
    except Exception:
        st.warning("No se encontró 'data/nike_rsi.png'. Súbelo a la carpeta data/.")

elif page == "Conclusión Ejecutiva":
    st.header("4. Conclusión Ejecutiva")
    st.write(
        "La combinación del análisis fundamental y técnico muestra que NIKE mantiene una posición financiera sólida, "
        "con márgenes rentables y un balance equilibrado. El precio se encuentra en fase correctiva de corto plazo, "
        "pero dentro de una estructura de largo plazo que sigue siendo alcista."
    )
    st.warning("Recomendación: **MANTENER / ESPERAR**. Vigilar rebotes técnicos o cruce alcista de medias.")
    st.success("A mediano/largo plazo, NIKE sigue siendo un activo atractivo dentro del sector consumo-discrecional.")
