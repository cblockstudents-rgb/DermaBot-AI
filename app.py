import streamlit as st

st.set_page_config(
    page_title="DermaBot AI",
    page_icon="🧴",
    layout="wide"
)

st.title("🧴 DermaBot AI")
st.subheader("Your Personal Skincare Guide")
st.write("Explore skincare information and build a simple skincare routine.")

st.info("DermaBot provides general skincare education, not medical diagnosis.")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a feature",
    [
        "Home",
        "Skincare FAQ",
        "Routine Generator",
        "Skin Concerns"
    ]
)

# Home
if page == "Home":

    st.header("Welcome to DermaBot AI!")

    st.write(
        "Healthy skincare begins with understanding "
        "your skin and following a consistent routine."
    )

    st.markdown("""
    ### Our Features

    - 💬 Skincare FAQ Chatbot
    - 🌿 Personalised Routine Generator
    - 🔍 Common Skin Concerns
    - 📚 Basic Skincare Education
    """)

    st.success("Select a feature from the sidebar to begin.")

# FAQ
elif page == "Skincare FAQ":

    st.header("💬 Skincare Frequently Asked Questions")

    faqs = {
        "What is a basic skincare routine?":
        "A basic routine includes a gentle cleanser, "
        "moisturiser and broad-spectrum sunscreen.",

        "Why is sunscreen important?":
        "Sunscreen helps protect skin from harmful UV radiation. "
        "Choose broad-spectrum SPF 30 or higher.",

        "How often should I wash my face?":
        "Generally, wash your face twice daily and after sweating.",

        "What is moisturiser?":
        "Moisturiser helps maintain the skin's moisture barrier.",

        "What is a patch test?":
        "A patch test involves trying a small amount of a "
        "new product on a small area of skin first.",

        "Can I use multiple skincare products?":
        "Introduce new products gradually. A simple routine "
        "is often a good starting point."
    }

    question = st.selectbox(
        "Choose your skincare question:",
        list(faqs.keys())
    )

    if st.button("Get Answer"):
        st.success(faqs[question])

    st.divider()

    st.subheader("Ask DermaBot")

    user_question = st.text_input(
        "Type a skincare question:"
    )

    if st.button("Ask"):
        q = user_question.lower()

        if "sunscreen" in q or "spf" in q:
            st.write(faqs["Why is sunscreen important?"])

        elif "moistur" in q:
            st.write(faqs["What is moisturiser?"])

        elif "wash" in q or "cleanser" in q:
            st.write(faqs["How often should I wash my face?"])

        elif "routine" in q:
            st.write(faqs["What is a basic skincare routine?"])

        elif "patch test" in q:
            st.write(faqs["What is a patch test?"])

        else:
            st.info(
                "I don't have a verified answer for this question yet. "
                "Please consult a qualified dermatologist for "
                "personal skin concerns."
            )

# Routine Generator
elif page == "Routine Generator":

    st.header("🌿 Skincare Routine Generator")

    skin_type = st.selectbox(
        "Select your skin type:",
        ["Normal", "Dry", "Oily", "Combination", "Sensitive", "Not sure"]
    )

    concern = st.selectbox(
        "Select your main skin concern:",
        [
            "No major concern",
            "Dryness",
            "Oiliness",
            "Occasional pimples",
            "Uneven skin tone",
            "Sensitivity"
        ]
    )

    if st.button("Generate My Routine"):

        st.subheader("Your Basic Skincare Routine")

        st.markdown("""
        **☀️ Morning Routine**

        1. Gentle cleanser.
        2. Suitable moisturiser.
        3. Broad-spectrum SPF 30+ sunscreen.

        **🌙 Night Routine**

        1. Gentle cleanser.
        2. Suitable moisturiser.
        """)

        if skin_type == "Dry":
            st.write("Tip: Choose a gentle, fragrance-free moisturiser.")

        elif skin_type == "Oily":
            st.write("Tip: Consider a lightweight, non-comedogenic moisturiser.")

        elif skin_type == "Sensitive":
            st.write("Tip: Prefer fragrance-free products and introduce new products slowly.")

        elif skin_type == "Combination":
            st.write("Tip: Choose a gentle routine suitable for different skin areas.")

        if concern == "Occasional pimples":
            st.info("Avoid picking pimples. Seek professional advice if acne persists.")

        elif concern == "Sensitivity":
            st.info("Keep your routine simple and avoid products that cause irritation.")

        elif concern == "Dryness":
            st.info("Use a gentle cleanser and moisturise regularly.")

        st.caption(
            "This is general educational guidance, not a medical prescription."
        )

# Skin Concerns
elif page == "Skin Concerns":

    st.header("🔍 Common Skin Concerns")

    concerns = {
        "Dry Skin":
        "Skin may feel tight, rough or flaky. Gentle cleansing "
        "and regular moisturising can help.",

        "Oily Skin":
        "Skin may appear shiny due to excess oil. Gentle cleansing "
        "and non-comedogenic moisturisers may help.",

        "Acne":
        "Acne is a common skin condition. Avoid picking spots "
        "and consult a dermatologist if it is persistent or painful.",

        "Sensitive Skin":
        "Sensitive skin may react to certain products. "
        "Fragrance-free products may be easier to tolerate.",

        "Uneven Skin Tone":
        "Uneven skin tone can have several causes. "
        "Sun protection is an important part of skin care."
    }

    selected = st.selectbox(
        "Choose a skin concern:",
        list(concerns.keys())
    )

    st.write(concerns[selected])

    st.warning(
        "DermaBot cannot diagnose skin conditions. "
        "For persistent, painful or worsening symptoms, "
        "consult a qualified dermatologist."
    )

st.divider()

st.caption("DermaBot AI | Class XII Artificial Intelligence Project")
