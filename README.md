Berikut adalah versi **README** dalam bahasa Inggris yang sesuai dengan struktur dan gaya yang Anda minta:

---

````markdown
# GO-MAN 🗺️🤖  
// for Alibaba Hackathon 2025

**GO-MAN** (*Go Meeting Anywhere Now*) is a web application built with [Streamlit](https://streamlit.io/) that helps users find the geographic midpoint of multiple locations and recommends nearby meeting spots. It also features an AI chatbot powered by a webhook integration using [n8n](https://n8n.io/).

---

## 🚀 Main Features

### 1. 🔍 Midpoint Finder  
Users can input multiple sets of coordinates (latitude and longitude), and the app will calculate the geographical midpoint. Based on this midpoint, it will suggest the nearest cafes (within a 3 km radius) using dummy data for demonstration purposes.

### 2. 🤖 AI Chat  
This feature allows users to ask any question. The input is sent to a configured `n8n` webhook endpoint, which processes the message and returns an AI-generated response displayed in the app interface.

---

## 🧰 Technologies Used

- **Python**
- **Streamlit** — for building the interactive user interface
- **Geopy** — to calculate geographic distances between coordinates
- **Requests** — to send HTTP requests to the `n8n` webhook
- **n8n** — to manage and automate backend AI workflows

---

## 🖥️ How to Run the App

### 1. Clone this repository:
```bash
git clone https://github.com/fakhruladani/GO-MAN.git
cd GO-MAN
````

### 2. Install dependencies:

Make sure you activate a virtual environment (optional), then run:

```bash
pip install -r requirements.txt
```

### 3. Run the app:

```bash
streamlit run app.py
```

---

## 📦 Example Input Format

Enter coordinates in the following format (JSON list of dictionaries):

```json
[
  {"lat": -6.2146, "lng": 106.8451},
  {"lat": -6.1767, "lng": 106.8271},
  {"lat": -6.2000, "lng": 106.8300}
]
```

---

## 🔧 Technical Notes

* The **midpoint** is calculated by averaging the latitude and longitude values of all input locations.
* The **cafe data** is currently dummy and can be expanded or replaced with real-time data using an API (e.g., Google Places API).
* The **n8n webhook** should be configured to receive a `user_input` parameter and return a JSON response containing the key `message`.

---

## 💡 Future Improvements

* **Google Maps Integration** — Integrate Google Maps API to fetch the actual latitude and longitude from user-inputted place names or addresses, and to display map visuals directly within the app.
* **Dynamic Midpoint Calculation from Place Names** — Allow users to input locations as place names (e.g., "Jakarta Timur", "Depok") and use geocoding to convert them to coordinates before midpoint calculation.
* **Personalized Recommendations** — Enhance recommendation accuracy by integrating a larger and richer dataset of cafes, restaurants, and meeting places, categorized by user preferences, distance, ratings, and type.
* **Real-time Data from Places APIs** — Replace static dummy data with live data from APIs such as Google Places, Foursquare, or Yelp for more accurate nearby venue suggestions.
* **User Profile & History** — Implement a user system that stores previous meeting points, preferred cafe types, or frequently used locations to personalize the experience over time.
* **Improved Distance Calculation Logic** — Enhance midpoint and distance logic by using weighted or road-based routes instead of just geographic coordinates.
