import streamlit as st

st.title("🏬 Casa TIA")
st.write("¡Bienvenido a nuestro sistema de compras!")

# Precios
precios = {
    "Heladera": 700000,
    "Lavarropas": 500000,
    "Licuadora": 45000,
    "Notebook": 1500000,
    "Smartphone": 250000,
}

total = 0

# Selección de categoría
categoria = st.radio(
    "¿Qué desea comprar?",
    ("Solo Electrodomésticos", "Solo Computación", "Ambos", "Ninguno")
)

# Sección Electrodomésticos
if categoria in ["Solo Electrodomésticos", "Ambos"]:
    st.subheader("--- Sección de Electrodomésticos ---")
    electro = st.selectbox(
        "Seleccione un electrodoméstico:",
        ("Ninguno", "Heladera ($700.000)", "Lavarropas ($500.000)", "Licuadora ($45.000)")
    )
    if "Heladera" in electro:
        total += precios["Heladera"]
    elif "Lavarropas" in electro:
        total += precios["Lavarropas"]
    elif "Licuadora" in electro:
        total += precios["Licuadora"]

# Sección Computación
if categoria in ["Solo Computación", "Ambos"]:
    st.subheader("--- Sección de Computación ---")
    compu = st.selectbox(
        "Seleccione un producto de computación:",
        ("Ninguno", "Notebook ($1.500.000)", "Smartphone ($250.000)")
    )
    if "Notebook" in compu:
        total += precios["Notebook"]
    elif "Smartphone" in compu:
        total += precios["Smartphone"]

# Resultado Final
st.divider()
total_formateado = f"${total:,.2f}".replace(",", "@").replace(".", ",").replace("@", ".")
st.metric(label="Total a pagar", value=total_formateado)

if st.button("Finalizar Compra"):
    st.success("¡Muchas gracias por su compra en Casa TIA! Que tenga un excelente día.")
