import streamlit as st
from reverb_client import ReverbClient

st.set_page_config(page_title="Reverb API Control Panel", layout="wide")

st.title("🎸 Reverb API Control Panel")

# ---------------- TOKEN GATE ----------------
st.markdown("### 🔐 Enter your Reverb API Token")

token = st.text_input(
    "API Token",
    type="password",
    help="Token is never stored and is cleared on refresh."
)

if not token:
    st.warning("Please enter your API token to continue.")
    st.stop()

client = ReverbClient(token)

if st.button("🚪 Clear token"):
    st.session_state.clear()
    st.experimental_rerun()

# ---------------- ALL FEATURES ----------------
tabs = st.tabs([
    "👤 Profile",
    "📦 Listings",
    "🧾 Orders",
    "💬 Messages",
    "🏷️ Offers",
    "⭐ Reviews",
    "📬 Addresses",
    "📃 Watchlist",
    "💰 Payouts",
    "🗣️ Feedback"
])

# -------- PROFILE --------
with tabs[0]:
    st.header("👤 Profile")
    data = client.get("/my/profile")
    st.json(data)

# -------- LISTINGS --------
with tabs[1]:
    st.header("📦 Listings")
    data = client.get("/my/listings", params={"per_page": 50})
    if "listings" in data:
        for l in data["listings"]:
            st.markdown(f"""
**{l['title']}**  
Price: {l['price']['amount']} {l['price']['currency']}  
Views: {l.get('view_count', '—')}  
Watchers: {l.get('watch_count', '—')}  
State: {l['state']}
""")
            st.divider()
    else:
        st.json(data)

# -------- ORDERS --------
with tabs[2]:
    st.header("🧾 Orders (Selling)")
    st.json(client.get("/my/orders/selling"))

# -------- MESSAGES --------
with tabs[3]:
    st.header("💬 Messages")
    st.json(client.get("/my/messages"))

# -------- OFFERS --------
with tabs[4]:
    st.header("🏷️ Offers")
    st.json(client.get("/my/offers"))

# -------- REVIEWS --------
with tabs[5]:
    st.header("⭐ Reviews")
    st.json(client.get("/my/reviews"))

# -------- ADDRESSES --------
with tabs[6]:
    st.header("📬 Addresses")
    st.json(client.get("/my/addresses"))

# -------- WATCHLIST --------
with tabs[7]:
    st.header("📃 Watchlist")
    st.json(client.get("/my/lists"))

# -------- PAYOUTS --------
with tabs[8]:
    st.header("💰 Payouts")
    st.json(client.get("/my/payouts"))

# -------- FEEDBACK --------
with tabs[9]:
    st.header("🗣️ Feedback")
    st.json(client.get("/my/feedback"))
