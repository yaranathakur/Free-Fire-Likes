import streamlit as st
import http.client
import json

st.title("Free Fire User Info")

user_id = st.text_input("Enter Free Fire User ID:")
region = st.selectbox("Select Region", ["SG", "IN", "BR", "US", "ID"])

if st.button("Fetch Details"):
    if user_id:
        conn = http.client.HTTPSConnection("id-game-checker.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': "2e0afea4ffmshf51a18f74d31147p1d7caejsnf5b1a0282bc5",
            'x-rapidapi-host': "id-game-checker.p.rapidapi.com"
        }

        url = f"/ff-player-info/{user_id}/{region}"
        conn.request("GET", url, headers=headers)

        res = conn.getresponse()
        data = res.read()

        result = json.loads(data.decode("utf-8"))

        st.write(result)
    else:
        st.warning("Please enter a User ID.")
