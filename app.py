import streamlit as st
import requests
from geopy.distance import geodesic

# Webhook URL for n8n
WEBHOOK_URL = 'https://jalapeno.app.n8n.cloud/webhook-test/c7a6cfbe-bdf1-42bc-947a-b8db19c1e132'

# Dummy cafe data for demonstration purposes
cafes_data = [
    {"name": "Cafe Nova", "lat": -6.2146, "lng": 106.8451, "address": "Jakarta Timur"},
    {"name": "Restoran Minang", "lat": -6.1767, "lng": 106.8271, "address": "Jakarta Barat"},
    {"name": "Zeus Cafe", "lat": -6.2000, "lng": 106.8300, "address": "Depok"}
]

# Title of the app
st.title("GO-MAN")
st.write("Ask me anything and I'll use AI to answer, or find the midpoint of your locations!")

# Midpoint Calculation Section
st.subheader("Find Midpoint of Locations")

# Input for coordinates
coordinates_input = st.text_area(
    "Enter coordinates (lat, lng) for multiple locations:",
    '[{"lat": -6.2146, "lng": 106.8451}, {"lat": -6.1767, "lng": 106.8271}]'
)

if st.button("Find Midpoint"):
    try:
        # Parsing input and calculating midpoint
        locations = eval(coordinates_input)  # Convert string to list of dictionaries
        coords = [(loc['lat'], loc['lng']) for loc in locations]

        mid_lat = sum([c[0] for c in coords]) / len(coords)
        mid_lng = sum([c[1] for c in coords]) / len(coords)

        # Find the closest cafes to the midpoint
        closest_cafes = []
        for cafe in cafes_data:
            distance = geodesic((mid_lat, mid_lng), (cafe['lat'], cafe['lng'])).meters
            if distance <= 3000:  # You can adjust the radius as needed
                closest_cafes.append({
                    'name': cafe['name'],
                    'address': cafe['address'],
                    'distance': round(distance, 2)
                })

        # Displaying results
        st.write(f"Midpoint: Latitude {mid_lat}, Longitude {mid_lng}")
        st.write("Closest Cafes:")
        for cafe in closest_cafes:
            st.write(f"{cafe['name']} - {cafe['address']} ({cafe['distance']} meters away)")

    except Exception as e:
        st.error(f"Error calculating midpoint: {e}")

# AI Chat Section
st.subheader("Chat with AI")

user_input = st.text_input("Your Question:")

if st.button("Get AI Answer"):
    if not user_input.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking..."):
            try:
                # Prepare payload to send to n8n webhook
                payload = {"user_input": user_input}

                # Send the data to n8n webhook
                response = requests.post(WEBHOOK_URL, json=payload)

                # Handle the response
                if response.status_code == 200:
                    ai_response = response.json().get("message", "No response from AI.")
                    st.markdown("### 🧠 AI Response:")
                    st.success(ai_response)
                else:
                    st.error(f"Error: {response.status_code}. Could not get response from AI.")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
