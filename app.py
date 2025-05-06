import streamlit as st
import http.client
import json
import pandas as pd

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
        
        if result["error"] == False:
            # Extract relevant info
            basic_info = result["data"]["basicInfo"]
            profile_info = result["data"]["profileInfo"]
            pet_info = result["data"]["petInfo"]
            social_info = result["data"]["socialInfo"]
            clan_info = result["data"]["clanBasicInfo"]
            credit_score_info = result["data"]["creditScoreInfo"]

            # Prepare data for vertical table
            user_data = {
                "Account ID": basic_info["accountId"],
                "Nickname": basic_info["nickname"],
                "Region": basic_info["region"],
                "Level": basic_info["level"],
                "Rank": basic_info["rank"],
                "Ranking Points": basic_info["rankingPoints"],
                "Max Rank": basic_info["maxRank"],
                "Last Login (Timestamp)": basic_info["lastLoginAt"],
                "Avatar": basic_info["avatars"][0],  # First avatar image
                "Pet Name": pet_info["name"],
                "Pet Level": pet_info["level"],
                "Pet Exp": pet_info["exp"],
                "Pet Skin ID": pet_info["skinId"],
                "Pet Selected Skill ID": pet_info["selectedSkillId"],
                "Social Language": social_info["language"],
                "Social Signature": social_info["signature"],
                "Clan Name": clan_info["clanName"] if clan_info else "N/A",
                "Clan Level": clan_info["clanLevel"] if clan_info else "N/A",
                "Clan Capacity": clan_info["capacity"] if clan_info else "N/A",
                "Clan Members": clan_info["memberNum"] if clan_info else "N/A",
                "Credit Score": credit_score_info["creditScore"],
                "Diamond Cost": result["data"]["diamondCostRes"]["diamondCost"],
            }

            # Convert the dictionary into a DataFrame for a vertical table
            df = pd.DataFrame(list(user_data.items()), columns=["Key", "Value"])

            # Display the vertical table
            st.write(df)
        else:
            st.error("❌ Failed to fetch data. Please check the User ID or region.")
    else:
        st.warning("Please enter a User ID.")
