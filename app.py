import streamlit as st
from cost_logic import estimate_cost, get_distance

st.set_page_config(page_title="Logistics Cost Estimator")

st.title("AI Logistics Cost Estimator")

source = st.text_input("Source City")
destination = st.text_input("Destination City")
vehicle = st.selectbox(
    "Vehicle Type",
    ["Mahindra Jeeto","Ashok Leyland Ecomet","BharatBenz"]
)
fuel_price = st.number_input("Fuel Price (per litre)", min_value = 1)

if st.button("Estimate Cost"):
    distance = get_distance(source,destination)
      
    if distance is None:
        st.error("Could not calculate distance. Check city names.")
    else: 
       result = estimate_cost(distance,vehicle, fuel_price)

    if result:
        st.success("Cost Estimated Successfully")
        st.write("### Cost Breakdown")
        st.write(f"**Distance:** {result['distance_km']} km")
        st.write(f"**Fuel Cost:** ₹{result['fuel_cost']}")
        st.write(f"**Total Trip Cost :** ₹{result['total_cost']}")
    else:
        st.error("Could not calculate distance. Check City names.")