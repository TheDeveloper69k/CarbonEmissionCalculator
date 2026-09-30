import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Carbon Emission Calculator",
    page_icon="🌱",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌱 Carbon Emission Calculator")
st.write(
    "Estimate your carbon emissions and understand "
    "their environmental impact."
)

st.divider()

# -----------------------------
# Input Section
# -----------------------------
st.subheader("🚗 Enter Your Activity Details")

distance = st.number_input(
    "🚗 Distance Travelled (km)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

fuel = st.number_input(
    "⛽ Fuel Used (litres)",
    min_value=0.0,
    value=0.0,
    step=0.5
)

electricity = st.number_input(
    "⚡ Electricity Used (kWh)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

# -----------------------------
# Calculate Button
# -----------------------------
if st.button("🌍 Calculate Carbon Emission"):

    # Emission factors
    transport_emission = distance * 0.21
    fuel_emission = fuel * 2.31
    electricity_emission = electricity * 0.82

    total_emission = (
        transport_emission
        + fuel_emission
        + electricity_emission
    )

    # -----------------------------
    # Main Result
    # -----------------------------
    st.success(
        f"🌍 Total Carbon Emission: "
        f"{total_emission:.2f} kg CO₂"
    )

    st.divider()

    # -----------------------------
    # Emission Breakdown
    # -----------------------------
    st.subheader("📊 Emission Breakdown")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🚗 Transport",
            f"{transport_emission:.2f} kg"
        )

    with col2:
        st.metric(
            "⛽ Fuel",
            f"{fuel_emission:.2f} kg"
        )

    with col3:
        st.metric(
            "⚡ Electricity",
            f"{electricity_emission:.2f} kg"
        )

    st.divider()

    # -----------------------------
    # Vehicle Analysis
    # -----------------------------
    st.subheader("🔧 Vehicle Pollution Analysis")

    if distance > 0 and fuel > 0:

        mileage = distance / fuel

        st.write(
            f"Your calculated fuel efficiency is "
            f"**{mileage:.2f} km/litre**."
        )

        if mileage < 8:
            st.error(
                "⚠️ Very low fuel efficiency detected. "
                "Consider getting the vehicle checked or serviced. "
                "Poor fuel efficiency can be associated with higher emissions."
            )

        elif mileage < 12:
            st.warning(
                "⚠️ Fuel efficiency is relatively low. "
                "A routine vehicle inspection/service may help improve efficiency."
            )

        else:
            st.success(
                "✅ Fuel efficiency is within a reasonable range "
                "for this simple demonstration."
            )

    else:
        st.info(
            "Enter both distance and fuel usage to analyze vehicle efficiency."
        )

    # -----------------------------
    # Environmental Impact
    # -----------------------------
    st.divider()

    st.subheader("🌍 Environmental Impact")

    # Approximate annual absorption by one mature tree.
    # Used only as an illustrative comparison.
    tree_equivalent = total_emission / 21

    if total_emission < 10:

        st.success(
            "🌱 This calculated emission is relatively low "
            "for the entered activity."
        )

    elif total_emission < 30:

        st.warning(
            "🌤️ This calculation represents a moderate amount "
            "of CO₂ emissions. Reducing unnecessary travel and "
            "energy consumption can lower the footprint."
        )

    else:

        st.error(
            "⚠️ This calculation represents a relatively high "
            "CO₂ footprint for the entered activity."
        )

    st.info(
        f"🌳 Approximate tree-equivalent comparison: "
        f"{tree_equivalent:.2f} tree-years of CO₂ absorption."
    )

    # -----------------------------
    # Ozone Layer Information
    # -----------------------------
    st.subheader("☀️ Ozone Layer Information")

    st.info(
        "CO₂ is a greenhouse gas and contributes to climate change, "
        "but it is not a direct ozone-depleting substance. "
        "Therefore, this calculator does not assign a percentage "
        "of ozone-layer damage to your emissions."
    )

    st.caption(
        "The environmental indicators shown here are simplified "
        "educational estimates and should not be treated as a "
        "scientific measurement of local air quality or vehicle condition."
    )