import streamlit as st

st.set_page_config(
    page_title="DermaBot AI",
    page_icon="🧴",
    layout="wide"
)
st.markdown("""
<style>

.stApp {
    background-color: #F0F4EA;
}

[data-testid="stSidebar"] {
    background-color: #E5EBDD;
}
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 12px;
}
[data-testid="stSidebar"] label {
    color: #294D3A !important;
    font-size: 15px;
    font-weight: 600;
}

h1, h2, h3 {
    color: #294D3A !important;
    font-family: Georgia, serif;
    font-weight: 700;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #294D3A !important;
}

p {
    color: #455B4B;
}

</style>
""", unsafe_allow_html=True)

st.title("🧴 DermaBot AI")
st.subheader("Your Personal Skincare Guide")
st.write("Explore skincare information and build a simple skincare routine.")

st.markdown("""
<div style="
    background-color: #E5EBDD;
    border-left: 5px solid #66866C;
    padding: 16px 22px;
    border-radius: 10px;
    margin: 15px 0 25px 0;
">
    <p style="
        color: #26382D;
        font-size: 15px;
        font-weight: 600;
        margin: 0;
    ">
        🌿 DermaBot provides general skincare education,
        not medical diagnosis.
    </p>
</div>
""", unsafe_allow_html=True)
# Sidebar
st.sidebar.markdown("""
<h2 style="
    color: #294D3A;
    font-family: Georgia, serif;
    font-size: 25px;
    margin-bottom: 5px;
">
    🌿 DermaBot AI
</h2>
<p style="
    color: #66866C;
    font-size: 13px;
    margin-top: 0;
">
    Your Skincare Companion
</p>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Choose a feature",
    [
        "Home",
        "Skincare FAQ",
        "Routine Generator",
        "Skin Concerns"
    ]
)


st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #FFF8F0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #F3E3DC;
}

/* Headings */
h1, h2, h3, h4 {
    color: #4A403A !important;
    font-family: Georgia, serif !important;
}

/* Buttons */
.stButton button {
    background-color: #A3B18A !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
}

/* Input boxes */
.stTextInput input {
    background-color: white !important;
    color: #4A403A !important;
    border: 1px solid #D8C8BD !important;
    border-radius: 8px !important;
}

</style>
""", unsafe_allow_html=True)
# Home


if page == "Home":

    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #F3E3DC, #FFF1E8);
        padding: 35px;
        border-radius: 20px;
        border: 1px solid #E8D5CA;
        margin-bottom: 25px;
    ">
        <h1 style="color: #59483F; font-family: Georgia, serif;">
            Welcome to DermaBot AI 🌷
        </h1>
        <h3 style="color: #8B7568;">
            Your Personal Skincare Companion
        </h3>
        <p style="color: #59483F; font-size: 17px;">
            Discover skincare knowledge, understand common skin
            concerns and explore simple routines for everyday care.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 style="color: #59483F; font-family: Georgia, serif;">
        Explore DermaBot Features
    </h2>
    """, unsafe_allow_html=True)

    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color:#FFF9F4; padding:26px;
        border-radius:18px; border:1px solid #E8D5CA;
        min-height:145px;">
            <h3 style="color:#8B7568;">💬 Skincare FAQ Chatbot</h3>
            <p style="color:#59483F;">Explore answers to common skincare questions.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#F5F7EF; padding:26px;
        border-radius:18px; border:1px solid #DCE5D5;
        min-height:145px;">
            <h3 style="color:#71805C;">🌿 Personalised Routine Generator</h3>
            <p style="color:#59483F;">Discover simple morning and evening routines.</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div style="background-color:#F5F7EF; padding:26px;
        border-radius:18px; border:1px solid #DCE5D5;
        min-height:145px;">
            <h3 style="color:#71805C;">🔍 Common Skin Concerns</h3>
            <p style="color:#59483F;">Learn about common skincare concerns.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background-color:#FFF9F4; padding:26px;
        border-radius:18px; border:1px solid #E8D5CA;
        min-height:145px;">
            <h3 style="color:#8B7568;">📚 Basic Skincare Education</h3>
            <p style="color:#59483F;">Understand skincare ingredients and basics.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color:#F3E3DC;
    border:1px solid #E8D5CA; padding:16px 22px;
    border-radius:12px; margin-top:25px;">
        <p style="color:#59483F; font-size:15px;
        font-weight:600; margin:0;">
            ✨ Select a feature from the sidebar to begin.
        </p>
    </div>
    """, unsafe_allow_html=True)



elif page == "Skincare FAQ":

    st.markdown("""
    <h1 style="
        color: #294D3A;
        font-family: Georgia, serif;
        font-size: 32px;
    ">
        💬 Skincare Frequently Asked Questions
    </h1>
    <p style="color: #66866C; font-size: 16px;">
        Simple answers to help you understand everyday skincare.
    </p>
    """, unsafe_allow_html=True)

    faqs = {
        "What is a basic skincare routine?":
        "A basic routine includes a gentle cleanser, moisturiser and broad-spectrum sunscreen.",

        "Why is sunscreen important?":
        "Sunscreen helps protect skin from harmful UV radiation. Choose broad-spectrum SPF 30 or higher.",

        "How often should I wash my face?":
        "Generally, wash your face twice daily and after sweating.",

        "What is moisturiser?":
        "Moisturiser helps maintain the skin's moisture barrier.",

        "What is a patch test?":
        "A patch test involves trying a small amount of a new product on a small area of skin first.",

        "Can I use multiple skincare products?":
        "Introduce new products gradually. A simple routine is often a good starting point."
    }

    st.markdown(
        "<h4 style='color: #294D3A;'>Choose Your Question</h4>",
        unsafe_allow_html=True
    )

    question = st.selectbox(
        "Select a skincare topic:",
        list(faqs.keys())
    )

    st.markdown(
        "<h4 style='color: #294D3A;'>Or Ask Your Own Question</h4>",
        unsafe_allow_html=True
    )

    user_question = st.text_input(
        "Type your skincare question here:",
        placeholder="e.g. Why is moisturiser important?"
    )

    if st.button("Get Answer"):

        answer = faqs[question]

        if user_question.strip():
            q = user_question.lower()

            if "sunscreen" in q or "spf" in q:
                answer = faqs["Why is sunscreen important?"]

            elif "moisturiser" in q or "moisturizer" in q:
                answer = faqs["What is moisturiser?"]

            elif "cleanser" in q or "face wash" in q:
                answer = "A gentle cleanser helps remove dirt, oil and impurities from the skin."

            elif "routine" in q:
                answer = faqs["What is a basic skincare routine?"]

            elif "patch test" in q:
                answer = faqs["What is a patch test?"]

            elif "wash" in q:
                answer = faqs["How often should I wash my face?"]

            else:
                answer = "I don't have a prepared answer for this question yet. Please try asking about sunscreen, moisturiser, cleanser or skincare routines."

        st.markdown("""
        <div style="
            background-color: #E5EBDD;
            border: 1px solid #C8D8C5;
            border-left: 5px solid #66866C;
            padding: 20px;
            border-radius: 12px;
            margin-top: 15px;
        ">
            <h4 style="color: #294D3A; margin-top: 0;">
                🌿 Your Answer
            </h4>
        """ + "<p style='color: #26382D; font-size: 16px;'>" +
        answer + "</p></div>", unsafe_allow_html=True)



elif page == "Skincare FAQ":

    st.markdown("""
    <h1 style="
        color: #294D3A;
        font-family: Georgia, serif;
        font-size: 32px;
    ">
        💬 Skincare Frequently Asked Questions
    </h1>
    <p style="color: #66866C; font-size: 16px;">
        Simple answers to help you understand everyday skincare.
    </p>
    """, unsafe_allow_html=True)

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

    st.markdown(
        "<h4 style='color: #294D3A;'>Choose Your Question</h4>",
        unsafe_allow_html=True
    )

    question = st.selectbox(
        "Select a skincare topic:",
        list(faqs.keys())
    )

    st.markdown(
        "<h4 style='color: #294D3A;'>Or Ask Your Own Question</h4>",
        unsafe_allow_html=True
    )

    user_question = st.text_input(
        "Type your skincare question here:",
        placeholder="e.g. Why is moisturiser important?"
    )

    if st.button("Get Answer"):

        answer = faqs[question]

        if user_question.strip():
            q = user_question.lower()

            if "sunscreen" in q:
                answer = "Sunscreen helps protect your skin from harmful UV radiation. Broad-spectrum SPF 30 or higher is generally recommended."

            elif "moisturiser" in q or "moisturizer" in q:
                answer = "Moisturiser helps maintain your skin's moisture barrier and prevent dryness."

            elif "cleanser" in q or "face wash" in q:
                answer = "A gentle cleanser helps remove dirt, oil and impurities from the skin."

            elif "routine" in q:
                answer = "A basic skincare routine includes cleansing, moisturising and applying sunscreen during the day."

            else:
                answer = "I don't have a prepared answer for this question yet. Please try asking about sunscreen, moisturiser, cleanser or skincare routines."

        st.markdown("""
        <div style="
            background-color: #E5EBDD;
            border: 1px solid #C8D8C5;
            border-left: 5px solid #66866C;
            padding: 20px;
            border-radius: 12px;
            margin-top: 15px;
        ">
            <h4 style="color: #294D3A; margin-top: 0;">
                🌿 Your Answer
            </h4>
        """ + "<p style='color: #26382D; font-size: 16px;'>" +
        answer + "</p></div>", unsafe_allow_html=True)
    

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
