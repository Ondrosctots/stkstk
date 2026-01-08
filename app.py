import streamlit as st
from reverb_client import ReverbClient

st.set_page_config(
    page_title="Reverb API Control Panel",
    layout="wide"
)

st.title("🎸 Reverb API Control Panel")

# ---------------- TOKEN GATE ----------------
st.markdown("### 🔐 Enter your Reverb API Token")

token = st.text_input(
    "API Token",
    type="password",
    help="The token is never saved and is cleared on refresh."
)

if not token:
    st.warning("Please enter your API token to continue.")
    st.stop()

client = ReverbClient(token)

# Optional: clear token manually
if st.button("🚪 Clear token"):
    st.session_state.clear()
    st.experimental_rerun()

# ---------------- TABS ----------------
tabs = st.tabs([
    "👤 Profile",
    "📦 Listings",
    "🧾 Orders",
    "💬 Messages"
])

# ---------------- PROFILE ----------------
with tabs[0]:
    st.header("👤 Your Profile")
    data = client.get("/my/profile")
    if "error" in data:
        st.error(data["error"])
    else:
        st.json(data)

# ---------------- LISTINGS ----------------
with tabs[1]:
    st.header("📦 Your Listings")
    data = client.get("/my/listings", params={"per_page": 50})

    if "error" in data:
        st.error(data["error"])
    else:
        listings = data.get("listings", [])
        if not listings:
            st.info("No listings found.")
        for l in listings:
            st.markdown(f"""
**{l['title']}**  
Price: {l['price']['amount']} {l['price']['currency']}  
Views: {l.get('view_count', '—')}  
Watchers: {l.get('watch_count', '—')}  
State: {l['state']}
""")
            st.divider()

# ---------------- ORDERS ----------------
with tabs[2]:
    st.header("🧾 Orders (Selling)")
    data = client.get("/my/orders/selling")
    if "error" in data:
        st.error(data["error"])
    else:
        st.json(data)

# ---------------- MESSAGES ----------------
with tabs[3]:
    st.header("💬 Messages")
    data = client.get("/my/messages")

    if "error" in data:
        st.error(data["error"])
    else:
        messages = data.get("messages", [])
        if not messages:
            st.info("No messages.")
        for m in messages:
            st.markdown(f"""
**From:** {m['sender']['username']}  
**Subject:** {m['subject']}
""")
            st.divider()
