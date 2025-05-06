import streamlit as st
import requests

# Streamlit UI
st.title("🎮 Free Fire User Info Checker")

# Input fields
user_id = st.text_input("Enter Free Fire User ID:")
region = st.selectbox("Select Region", ["SG", "IN", "BR", "US", "ID"])

# Button to fetch data
if st.button("Fetch Details"):
    if user_id:
        url = f"https://id-game-checker.p.rapidapi.com/ff-player-info/{user_id}/{region}"
        headers = {
            'x-rapidapi-key': "2e0afea4ffmshf51a18f74d31147p1d7caejsnf5b1a0282bc5",  # Keep safe in production
            'x-rapidapi-host': "id-game-checker.p.rapidapi.com"
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                st.success("✅ User Data Fetched Successfully!")

                # Display user details
                st.write("**🎮 Nickname:**", data.get("nickname", "N/A"))
                st.write("**🏅 Level:**", data.get("level", "N/A"))
                st.write("**🆔 Account ID:**", data.get("account_id", "N/A"))
                st.write("**🌍 Region:**", region)
            else:
                st.error("❌ Failed to fetch data. Please check the User ID or region.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid User ID.")
