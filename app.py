import streamlit as st
from reverb_client import ReverbClient

st.set_page_config(page_title="Reverb API Control Panel", layout="wide")
st.title("🎸 Reverb API Control Panel")

# -------- TOKEN GATE --------
token = st.text_input(
    "🔐 Enter your Reverb API token",
    type="password",
    help="Token is never saved and cleared on refresh."
)

if not token:
    st.stop()

client = ReverbClient(token)

# -------- TABS --------
tabs = st.tabs([
    "👤 Account",
    "📦 Listings",
    "🧾 Orders",
    "💬 Messages",
    "📬 Addresses",
    "💰 Payouts"
])

# -------- ACCOUNT (v3) --------
with tabs[0]:
    st.header("👤 Account")
    st.json(client.get("/my/account", version="3.0"))

# -------- LISTINGS (v3) --------
with tabs[1]:
    st.header("📦 Listings")
    data = client.get("/my/listings", version="3.0", params={"per_page": 50})

    if "listings" in data:
        for l in data["listings"]:
            st.markdown(f"""
**{l['title']}**  
Price: {l['price']['amount']} {l['price']['currency']}  
State: {l['state']['description']}
""")
            st.caption("⚠️ Reverb API does NOT expose views, watchers, or cart counts.")
            st.divider()
    else:
        st.json(data)

# -------- ORDERS (v3) --------
with tabs[2]:
    st.header("🧾 Orders (Selling)")
    st.json(client.get("/my/orders/selling", version="3.0"))

# -------- MESSAGES (v1 ONLY) ✅ --------
with tabs[3]:
    st.header("💬 Messages")
    st.json(client.get("/my/messages", version="1.0"))

# -------- ADDRESSES (v3) --------
with tabs[4]:
    st.header("📬 Addresses")
    st.json(client.get("/my/addresses", version="3.0"))

# -------- PAYOUTS (v3) --------
with tabs[5]:
    st.header("💰 Payouts")
    st.json(client.get("/my/payouts", version="3.0"))
