import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Mechanical Engineering Utility Suite",
    page_icon="⚙️",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.main {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    color: #00d4ff;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #ffffff;
    margin-bottom: 30px;
}

.info-card {
    background-color: #1f2937;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #00d4ff;
    box-shadow: 0px 0px 10px rgba(0,212,255,0.3);
}

.metric-card {
    background-color: #111827;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #00d4ff;
}

.stButton>button {
    background-color: #00d4ff;
    color: black;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("""
<div class="title">
⚙️ Mechanical Unit Converter & Material Density Checker
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Developed By: <b>Raja Abdul Rehman</b><br>
Roll Number: <b>25-ME-183</b>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("⚙️ Navigation Panel")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "📏 Unit Converter",
        "🧱 Density Checker",
        "📊 Density Comparison"
    ]
)

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------
if menu == "🏠 Home":

    st.header("🎓 Mechanical Engineering Utility Suite")

    st.write("""
    This web application is designed for Mechanical Engineering students and professionals.
    It provides unit conversion tools, material density checking, and engineering data visualization.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
        <h2>7+</h2>
        <p>Engineering Conversions</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
        <h2>8</h2>
        <p>Engineering Materials</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
        <h2>100%</h2>
        <p>Mechanical Engineering Based</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.image(
        "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc",
        use_container_width=True
    )

    st.success("Welcome to the Mechanical Engineering Utility Web App!")

# ---------------------------------------------------
# UNIT CONVERTER
# ---------------------------------------------------
elif menu == "📏 Unit Converter":

    st.header("📏 Mechanical Unit Converter")

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

    st.markdown("---")

    if category == "Length":

        meters = value
        feet = meters * 3.28084
        inches = meters * 39.3701

        st.metric("Meters", meters)
        st.metric("Feet", round(feet, 2))
        st.metric("Inches", round(inches, 2))

    elif category == "Force":

        newton = value
        lbf = newton * 0.224809

        st.metric("Newton", newton)
        st.metric("Pound-force", round(lbf, 2))

    elif category == "Pressure":

        pascal = value
        psi = pascal * 0.000145038

        st.metric("Pascal", pascal)
        st.metric("PSI", round(psi, 4))

    elif category == "Temperature":

        celsius = value
        fahrenheit = (celsius * 9/5) + 32

        st.metric("Celsius", celsius)
        st.metric("Fahrenheit", round(fahrenheit, 2))

    elif category == "Velocity":

        ms = value
        kmh = ms * 3.6

        st.metric("m/s", ms)
        st.metric("km/h", round(kmh, 2))

    elif category == "Mass":

        kg = value
        pounds = kg * 2.20462

        st.metric("Kilograms", kg)
        st.metric("Pounds", round(pounds, 2))

    elif category == "Energy":

        joule = value
        calorie = joule * 0.239006

        st.metric("Joules", joule)
        st.metric("Calories", round(calorie, 2))

# ---------------------------------------------------
# DENSITY CHECKER
# ---------------------------------------------------
elif menu == "🧱 Density Checker":

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
    <div class="info-card">
        <h2>{material}</h2>
        <h3>Density = {density} kg/m³</h3>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# DENSITY COMPARISON
# ---------------------------------------------------
elif menu == "📊 Density Comparison":

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
        text="Density",
        title="Engineering Material Density Comparison",
        template="plotly_dark"
    )

    fig.update_traces(textposition='outside')

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df, use_container_width=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown("""
<div style='text-align:center; color:gray;'>
© 2026 Mechanical Engineering Utility Suite <br>
Developed by Raja Abdul Rehman | Roll No: 25-ME-183
</div>
""", unsafe_allow_html=True)
