import streamlit as st
from reverb_client import ReverbClient

st.set_page_config(page_title="Reverb API Control Panel", layout="wide")
st.title("🎸 Reverb API Control Panel")

# -------- TOKEN GATE --------
token = st.text_input(
    "🔐 Enter your Reverb API token",
    type="password"
)

if not token:
    st.stop()

client = ReverbClient(token)

# -------- TABS (REAL ONES) --------
tabs = st.tabs([
    "👤 Account",
    "📦 Listings",
    "🧾 Orders",
    "💬 Messages",
    "📬 Addresses",
    "💰 Payouts"
])

# -------- ACCOUNT --------
with tabs[0]:
    st.header("👤 Account")
    st.json(client.get("/my/account"))

# -------- LISTINGS --------
with tabs[1]:
    st.header("📦 Listings")
    data = client.get("/my/listings", params={"per_page": 50})

    if "listings" in data:
        for l in data["listings"]:
            st.markdown(f"""
**{l['title']}**  
Price: {l['price']['amount']} {l['price']['currency']}  
State: {l['state']['description']}
""")
            st.caption("⚠️ Reverb API does not expose views, watchers, or cart count.")
            st.divider()
    else:
        st.json(data)

# -------- ORDERS --------
with tabs[2]:
    st.header("🧾 Orders (Selling)")
    st.json(client.get("/my/orders/selling"))

# -------- MESSAGES (v2 ONLY) --------
with tabs[3]:
    st.header("💬 Messages")
    st.json(client.get("/my/messages", version="2.0"))

# -------- ADDRESSES --------
with tabs[4]:
    st.header("📬 Addresses")
    st.json(client.get("/my/addresses"))

# -------- PAYOUTS --------
with tabs[5]:
    st.header("💰 Payouts")
    st.json(client.get("/my/payouts"))
