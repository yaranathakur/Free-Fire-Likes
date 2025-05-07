import streamlit as st
import requests

st.title("Free Fire Player Info Checker")

# Input for user ID
user_id = st.text_input("Enter Free Fire User ID:")

if st.button("Get Player Info"):
    if user_id:
        url = f"https://id-game-checker.p.rapidapi.com/ff-player-info/{user_id}/IN"
        headers = {
            "x-rapidapi-key": "2e0afea4ffmshf51a18f74d31147p1d7caejsnf5b1a0282bc5",
            "x-rapidapi-host": "id-game-checker.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if not data["error"]:
                # Basic Info
                info = data["data"]["basicInfo"]
                # Profile Info
                profile = data["data"]["profileInfo"]
                # Clan Info
                clan = data["data"].get("clanBasicInfo", {})
                # Pet Info
                pet = data["data"].get("petInfo", {})
                # Social Info
                social = data["data"]["socialInfo"]
                # Diamond Info
                diamond = data["data"].get("diamondCostRes", {})
                # Credit Score Info
                credit_score = data["data"].get("creditScoreInfo", {})

                # Display all sections
                st.subheader("Basic Info")
                st.image(info["avatars"][0], caption=f"Avatar of {info['nickname']}", width=150)
                st.write(f"**Nickname:** {info['nickname']}")
                st.write(f"**Account ID:** {info['accountId']}")
                st.write(f"**Account Type:** {info['accountType']}")
                st.write(f"**Region:** {info['region']}")
                st.write(f"**Level:** {info['level']}")
                st.write(f"**Experience:** {info['exp']}")
                st.write(f"**Rank:** {info['rank']}")
                st.write(f"**Rank Points:** {info['rankingPoints']}")
                st.write(f"**Max Rank:** {info['maxRank']}")
                st.write(f"**CS Rank:** {info['csRank']}")
                st.write(f"**CS Ranking Points:** {info['csRankingPoints']}")
                st.write(f"**Elite Pass:** {'Yes' if info['hasElitePass'] else 'No'}")
                st.write(f"**Likes:** {info['liked']}")
                st.write(f"**Badges Count:** {info['badgeCnt']}")
                st.write(f"**Badge ID:** {info['badgeId']}")
                st.write(f"**Weapon Skins Showed:** {info['weaponSkinShows']}")
                st.write(f"**Account Created At (Epoch):** {info['createAt']}")
                st.write(f"**Last Login (Epoch):** {info['lastLoginAt']}")
                st.write(f"**External Icon Status:** {info['externalIconInfo']['status']}")
                st.write(f"**Release Version:** {info['releaseVersion']}")
                st.write(f"**Season ID:** {info['seasonId']}")
                
                # Display Clothes
                st.subheader("Clothes Info")
                for idx, img_url in enumerate(profile["clothes"]["images"]):
                    st.image(img_url, caption=f"Clothing {idx+1}", width=150)

                # Clan Info
                st.subheader("Clan Info")
                if clan:
                    st.write(f"**Clan ID:** {clan['clanId']}")
                    st.write(f"**Clan Name:** {clan['clanName']}")
                    st.write(f"**Clan Level:** {clan['clanLevel']}")
                    st.write(f"**Clan Capacity:** {clan['capacity']}")
                    st.write(f"**Clan Members:** {clan['memberNum']}/{clan['capacity']}")
                else:
                    st.write("No clan info available.")

                # Profile Info
                st.subheader("Profile Info")
                st.write(f"**Preferred Mode:** {social['modePrefer']}")
                st.write(f"**Active Time:** {social['timeActive']}")
                st.write(f"**Language:** {social['language']}")
                st.write(f"**Signature:** {social['signature']}")
                st.write(f"**Rank Show:** {social['rankShow']}")

                # Pet Info
                st.subheader("Pet Info")
                if pet:
                    st.write(f"**Pet Name:** {pet['name']}")
                    st.write(f"**Pet Level:** {pet['level']}")
                    st.write(f"**Pet Exp:** {pet['exp']}")
                    st.write(f"**Pet Skin ID:** {pet['skinId']}")
                    st.write(f"**Selected Skill ID:** {pet['selectedSkillId']}")
                    # Display pet image (if available)
                    pet_img_url = f"https://cdn.neferbyte.com/api/v1/ff/pet/{pet['skinId']}/png"
                    st.image(pet_img_url, caption=f"Pet {pet['name']}", width=150)
                else:
                    st.write("No pet info available.")

                # Diamond Cost Info
                st.subheader("Diamond Info")
                if diamond:
                    st.write(f"**Diamond Cost:** {diamond['diamondCost']}")
                else:
                    st.write("No diamond info available.")
                
                # Credit Score Info
                st.subheader("Credit Score Info")
                if credit_score:
                    st.write(f"**Credit Score:** {credit_score['creditScore']}")
                    st.write(f"**Reward State:** {credit_score['rewardState']}")
                    st.write(f"**Periodic Summary Start Time (Epoch):** {credit_score['periodicSummaryStartTime']}")
                    st.write(f"**Periodic Summary End Time (Epoch):** {credit_score['periodicSummaryEndTime']}")
                else:
                    st.write("No credit score info available.")
                    
            else:
                st.error("User not found.")
        else:
            st.error("Failed to fetch data. Please check the ID or try again later.")
    else:
        st.warning("Please enter a user ID.")
