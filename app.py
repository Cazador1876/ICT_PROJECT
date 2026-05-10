import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    color: #00d4ff;
    text-align: center;
}

.sub-title {
    font-size: 22px;
    color: #ffffff;
    text-align: center;
}

.info-box {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #00d4ff;
}

.metric-box {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #00d4ff;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    """
    <div class='big-title'>
    ⚙️ Mechanical Unit Converter & Material Density Checker
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-title'>
    Developed By: <b>Raja Abdul Rehman</b><br>
    Roll Number: <b>25-ME-183</b>
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Navigation")

menu = st.sidebar.radio(
    "Select Feature",
    [
        "Home",
        "Unit Converter",
        "Density Checker",
        "Density Comparison"
    ]
)

# ---------------- HOME PAGE ----------------
if menu == "Home":

    st.markdown("## 📘 Project Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='metric-box'>
        <h2>7+</h2>
        <p>Engineering Unit Categories</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='metric-box'>
        <h2>8</h2>
        <p>Material Types</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='metric-box'>
        <h2>100%</h2>
        <p>Mechanical Engineering Focused</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.image(
        "https://images.unsplash.com/photo-1581092919535-7146ff1a5905",
        use_container_width=True
    )

    st.success("Welcome to the Mechanical Engineering Utility Web App!")

# ---------------- UNIT CONVERTER ----------------
elif menu == "Unit Converter":

    st.header("🔧 Mechanical Unit Converter")

    category = st.selectbox(
        "Select Conversion Type",
        [
            "Length",
            "Force",
            "Pressure",
            "Temperature",
            "Velocity",
            "Mass",
            "Energy"
        ]
    )

    value = st.number_input("Enter Value", value=1.0)

    if category == "Length":

        meters = value
        feet = meters * 3.28084
        inches = meters * 39.3701

        st.write(f"### {meters} meters")
        st.write(f"📏 Feet: {feet:.2f}")
        st.write(f"📏 Inches: {inches:.2f}")

    elif category == "Force":

        newton = value
        lbf = newton * 0.224809

        st.write(f"### {newton} Newton")
        st.write(f"💪 Pound-force: {lbf:.2f}")

    elif category == "Pressure":

        pascal = value
        psi = pascal * 0.000145038

        st.write(f"### {pascal} Pascal")
        st.write(f"🧪 PSI: {psi:.4f}")

    elif category == "Temperature":

        celsius = value
        fahrenheit = (celsius * 9/5) + 32

        st.write(f"### {celsius} °C")
        st.write(f"🌡️ Fahrenheit: {fahrenheit:.2f} °F")

    elif category == "Velocity":

        ms = value
        kmh = ms * 3.6

        st.write(f"### {ms} m/s")
        st.write(f"🚀 km/h: {kmh:.2f}")

    elif category == "Mass":

        kg = value
        pounds = kg * 2.20462

        st.write(f"### {kg} kg")
        st.write(f"⚖️ Pounds: {pounds:.2f}")

    elif category == "Energy":

        joule = value
        calorie = joule * 0.239006

        st.write(f"### {joule} Joules")
        st.write(f"🔥 Calories: {calorie:.2f}")

# ---------------- DENSITY CHECKER ----------------
elif menu == "Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200,
        "Plastic": 950,
        "Rubber": 1100
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.markdown(f"""
    <div class='info-box'>
    <h2>{material}</h2>
    <h3>Density = {density} kg/m³</h3>
    </div>
    """, unsafe_allow_html=True)

# ---------------- DENSITY COMPARISON ----------------
elif menu == "Density Comparison":

    st.header("📊 Material Density Comparison")

    data = {
        "Material": [
            "Steel",
            "Aluminum",
            "Copper",
            "Brass",
            "Titanium",
            "Cast Iron",
            "Plastic",
            "Rubber"
        ],
        "Density": [
            7850,
            2700,
            8960,
            8500,
            4500,
            7200,
            950,
            1100
        ]
    }

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="Material",
        y="Density",
        title="Material Density Comparison",
        text="Density"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df)
