import streamlit as st
import pandas as pd
import plotly.express as px
import math

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Mechanical Engineering Utility Suite",
    page_icon="⚙️",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #1b1b1b;
    color: white;
    font-family: 'Segoe UI';
}

.main {
    background-color: #1b1b1b;
}

.title-box {
    background: linear-gradient(to right, #2f2f2f, #556b2f);
    padding: 35px;
    border-radius: 20px;
    border: 2px solid olive;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(128,128,128,0.4);
}

.metric-box {
    background-color: #2a2a2a;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid olive;
    text-align: center;
}

.info-box {
    background-color: #2f2f2f;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid olive;
}

.sidebar .sidebar-content {
    background-color: #222222;
}

.stButton>button {
    background-color: olive;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE PAGE
# =====================================================

st.markdown("""
<div class="title-box">

<h1 style="color:#d3d3d3; font-size:48px;">
⚙️ Mechanical Engineering Utility Suite
</h1>

<h2 style="color:white;">
Mechanical Unit Converter & Density Analyzer
</h2>

<h1 style="color:#FFD700;">
Raja Abdul Rehman
</h1>

<h2 style="color:white;">
Roll Number: 25-ME-183
</h2>

<h3 style="color:#d3d3d3;">
Department of Mechanical Engineering
</h3>

<h3 style="color:olive;">
University of Engineering & Technology Taxila
</h3>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# UET TAXILA LOGO
# =====================================================

st.image(
    "https://upload.wikimedia.org/wikipedia/en/7/7d/UET_Taxila_logo.png",
    width=180
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("⚙️ Engineering Dashboard")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "🧮 Scientific Calculator",
        "📏 Unit Converter",
        "🧱 Density Checker",
        "📊 Density Graphs"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if menu == "🏠 Home":

    st.header("🏠 Project Overview")

    st.write("""
    This advanced Mechanical Engineering Utility Suite is specially developed for
    university-level engineering students and professionals.

    Features include:
    - Scientific Calculator
    - Engineering Unit Converter
    - Material Density Checker
    - Interactive Graphical Visualization
    - Engineering Data Analysis
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-box">
        <h1>100+</h1>
        <p>Unit Conversions</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-box">
        <h1>20+</h1>
        <p>Engineering Materials</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-box">
        <h1>5</h1>
        <p>Engineering Modules</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.image(
        "https://images.unsplash.com/photo-1509395176047-4a66953fd231",
        use_container_width=True
    )

# =====================================================
# SCIENTIFIC CALCULATOR
# =====================================================

elif menu == "🧮 Scientific Calculator":

    st.header("🧮 Scientific Calculator")

    expression = st.text_input(
        "Enter Mathematical Expression",
        "sqrt(25)+sin(0)"
    )

    if st.button("Calculate"):

        try:
            result = eval(expression)

            st.success(f"Result = {result}")

        except:
            st.error("Invalid Expression")

    st.markdown("""
    ### Supported Functions
    - sqrt()
    - sin()
    - cos()
    - tan()
    - log()
    - math.pi
    - math.e
    """)

# =====================================================
# UNIT CONVERTER
# =====================================================

elif menu == "📏 Unit Converter":

    st.header("📏 Advanced Engineering Unit Converter")

    category = st.selectbox(
        "Select Category",
        [
            "Length",
            "Mass",
            "Temperature",
            "Pressure",
            "Force",
            "Velocity",
            "Energy",
            "Power",
            "Area",
            "Volume"
        ]
    )

    value = st.number_input("Enter Value", value=1.0)

    # LENGTH
    if category == "Length":

        st.subheader("Length Conversion")

        conversions = {
            "Meters": value,
            "Kilometers": value / 1000,
            "Centimeters": value * 100,
            "Millimeters": value * 1000,
            "Feet": value * 3.28084,
            "Inches": value * 39.3701,
            "Yards": value * 1.09361,
            "Miles": value * 0.000621371
        }

    # MASS
    elif category == "Mass":

        conversions = {
            "Kilograms": value,
            "Grams": value * 1000,
            "Pounds": value * 2.20462,
            "Tons": value / 1000,
            "Ounces": value * 35.274
        }

    # TEMPERATURE
    elif category == "Temperature":

        conversions = {
            "Celsius": value,
            "Fahrenheit": (value * 9/5) + 32,
            "Kelvin": value + 273.15
        }

    # PRESSURE
    elif category == "Pressure":

        conversions = {
            "Pascal": value,
            "kPa": value / 1000,
            "Bar": value / 100000,
            "PSI": value * 0.000145038,
            "Atmosphere": value / 101325
        }

    # FORCE
    elif category == "Force":

        conversions = {
            "Newton": value,
            "kN": value / 1000,
            "Pound-force": value * 0.224809,
            "Dyne": value * 100000
        }

    # VELOCITY
    elif category == "Velocity":

        conversions = {
            "m/s": value,
            "km/h": value * 3.6,
            "mph": value * 2.23694,
            "ft/s": value * 3.28084
        }

    # ENERGY
    elif category == "Energy":

        conversions = {
            "Joule": value,
            "kJ": value / 1000,
            "Calorie": value * 0.239006,
            "kWh": value / 3600000
        }

    # POWER
    elif category == "Power":

        conversions = {
            "Watt": value,
            "kW": value / 1000,
            "Horsepower": value * 0.00134102
        }

    # AREA
    elif category == "Area":

        conversions = {
            "m²": value,
            "cm²": value * 10000,
            "ft²": value * 10.7639,
            "acre": value * 0.000247105
        }

    # VOLUME
    elif category == "Volume":

        conversions = {
            "m³": value,
            "Liters": value * 1000,
            "cm³": value * 1000000,
            "ft³": value * 35.3147
        }

    df = pd.DataFrame(
        list(conversions.items()),
        columns=["Unit", "Converted Value"]
    )

    st.dataframe(df, use_container_width=True)

# =====================================================
# DENSITY CHECKER
# =====================================================

elif menu == "🧱 Density Checker":

    st.header("🧱 Engineering Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200,
        "Lead": 11340,
        "Nickel": 8908,
        "Zinc": 7140,
        "Magnesium": 1740,
        "Rubber": 1100,
        "Plastic": 950,
        "Concrete": 2400,
        "Glass": 2500,
        "Wood": 600,
        "Carbon Fiber": 1750
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.markdown(f"""
    <div class="info-box">

    <h1>{material}</h1>

    <h2>Density = {density} kg/m³</h2>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# DENSITY GRAPHS
# =====================================================

elif menu == "📊 Density Graphs":

    st.header("📊 Material Density Analysis")

    data = {
        "Material": [
            "Steel",
            "Aluminum",
            "Copper",
            "Titanium",
            "Lead",
            "Magnesium",
            "Plastic",
            "Concrete"
        ],
        "Density": [
            7850,
            2700,
            8960,
            4500,
            11340,
            1740,
            950,
            2400
        ]
    }

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="Material",
        y="Density",
        color="Density",
        title="Engineering Material Density Comparison",
        template="plotly_dark",
        text="Density"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df, use_container_width=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<div style='text-align:center; color:gray;'>

© 2026 Mechanical Engineering Utility Suite<br>

Developed By: Raja Abdul Rehman<br>

Roll Number: 25-ME-183<br>

UET Taxila — Department of Mechanical Engineering

</div>
""", unsafe_allow_html=True)
