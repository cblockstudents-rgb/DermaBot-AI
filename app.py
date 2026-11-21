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


if st.session_state.get("is_mobile", False):
    page = st.radio(
        "🌿 Explore DermaBot",
        [
            "Home",
            "Skincare FAQ",
            "Routine Generator",
            "Skin Concerns"
        ],
        horizontal=True
    )
else:
    page = st.sidebar.radio(
        "🌿 Choose a feature",
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
    background: linear-gradient(180deg, #F3E3DC, #F8EEE8);
    border-right: 1px solid #E8D5CA;
}

/* Sidebar navigation text */
[data-testid="stSidebar"] * {
    color: #4A403A;
}

/* Headings */
h1, h2, h3, h4 {
    color: #4A403A !important;
    font-family: Georgia, serif !important;
}

/* Paragraph text */
p, label, .stMarkdown {
    color: #5B5049;
}

/* Buttons */
.stButton button {
    background-color: #A3B18A !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 9px 20px !important;
    font-weight: 600 !important;
    transition: 0.3s ease;
}

.stButton button:hover {
    background-color: #71805C !important;
    transform: translateY(-2px);
}

/* Input boxes */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: white !important;
    color: #4A403A !important;
    border: 1px solid #D8C8BD !important;
    border-radius: 10px !important;
}

/* Cards and containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFCF8;
    border: 1px solid #E8D5CA;
    border-radius: 16px;
    padding: 10px;
}

/* Section spacing */
div[data-testid="stVerticalBlock"] {
    gap: 1rem;
}

/* Horizontal separators */
hr {
    border-color: #E8D5CA;
}

/* Expander */
.streamlit-expanderHeader {
    background-color: #F3E3DC;
    border-radius: 10px;
}

/* Smooth page appearance */
.stApp {
    transition: background-color 0.3s ease;
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
    <h1 style="color:#59483F; font-family:Georgia,serif;">
        💬 Skincare Frequently Asked Questions
    </h1>
    <p style="color:#8B7568; font-size:16px;">
        Your little knowledge corner for everyday skincare.
    </p>
    """, unsafe_allow_html=True)

    faqs = {
        "What is a basic skincare routine?":
        "A basic skincare routine has three important steps: gentle cleansing, moisturising and applying broad-spectrum SPF 30+ sunscreen during the day. Consistency is more important than using lots of products.",

        "Why is sunscreen important?":
        "Sunscreen helps protect your skin from ultraviolet (UV) radiation. Broad-spectrum sunscreen protects against UVA and UVB rays. SPF 30 or higher is generally recommended for everyday use.",

        "How often should I wash my face?":
        "For most people, washing gently twice a day and after sweating is sufficient. Excessive washing and harsh scrubbing can irritate the skin.",

        "Why do we need moisturiser?":
        "Moisturiser helps maintain the skin barrier and reduce moisture loss. Different formulations are available for different skin types.",

        "What is a patch test?":
        "A patch test means trying a small amount of a new skincare product on a small area of skin first. Follow the product instructions and stop using it if irritation develops.",

        "What is the difference between UVA and UVB?":
        "UVA rays contribute to skin ageing and can penetrate deeper into the skin. UVB rays are a major cause of sunburn. Broad-spectrum sunscreen helps protect against both.",

        "What is acne?":
        "Acne is a common skin condition that develops when hair follicles become blocked. It can involve blackheads, whiteheads and inflamed spots. A dermatologist can help with persistent acne.",

        "What are blackheads and whiteheads?":
        "Both are types of clogged pores. Blackheads are open at the surface, while whiteheads are closed. They are common forms of non-inflammatory acne.",

        "What is hyaluronic acid?":
        "Hyaluronic acid is a humectant, an ingredient that helps attract and retain water. It is commonly included in moisturisers and hydrating skincare products.",

        "What is niacinamide?":
        "Niacinamide is a form of vitamin B3 used in skincare products. It is studied for its role in supporting the skin barrier and improving the appearance of uneven skin tone.",

        "What are ceramides?":
        "Ceramides are lipids naturally found in the skin barrier. Skincare products containing ceramides are designed to support the skin barrier and reduce moisture loss.",

        "Can I use multiple skincare products?":
        "You can use more than one skincare product, but introduce new products gradually. A simple routine is often a good starting point. Using too many products can sometimes cause irritation.",

        "Does drinking water cure acne?":
        "Drinking enough water supports general health, but water alone does not cure acne. Persistent or concerning acne should be discussed with a dermatologist.",

        "Can skincare products expire?":
        "Yes. Skincare products can change over time. Check the expiry date and the period-after-opening symbol on packaging. Avoid using products that have changed in smell, colour or texture.",

        "What should I do if a product irritates my skin?":
        "Stop using the product if it causes irritation. Keep your routine gentle and seek medical advice if the reaction is severe, persistent or concerning."
    }

    st.markdown("### 🌸 Explore Common Questions")

    question = st.selectbox(
        "Choose a question:",
        list(faqs.keys()),
        key="faq_question_select"
    )

    st.markdown("### 🔎 Ask DermaBot")

    user_question = st.text_input(
        "Or type your own skincare question:",
        placeholder="Example: What does niacinamide do?",
        key="faq_custom_question"
    )

    if st.button("✨ Get My Answer", key="faq_answer_button"):

        answer = faqs[question]

        if user_question.strip():

            q = user_question.lower()

            if "sunscreen" in q or "spf" in q or "uv" in q or "sun protection" in q:
                answer = faqs["Why is sunscreen important?"]

            elif "hyaluronic" in q:
                answer = faqs["What is hyaluronic acid?"]

            elif "niacinamide" in q or "vitamin b3" in q:
                answer = faqs["What is niacinamide?"]

            elif "ceramide" in q:
                answer = faqs["What are ceramides?"]

            elif "blackhead" in q or "whitehead" in q:
                answer = faqs["What are blackheads and whiteheads?"]

            elif "acne" in q or "pimple" in q or "breakout" in q:
                answer = faqs["What is acne?"]

            elif "moistur" in q or "hydration" in q:
                answer = faqs["Why do we need moisturiser?"]

            elif "cleanser" in q or "face wash" in q or "wash face" in q:
                answer = faqs["How often should I wash my face?"]

            elif "patch test" in q or "new product test" in q:
                answer = faqs["What is a patch test?"]

            elif "expire" in q or "expiry" in q:
                answer = faqs["Can skincare products expire?"]

            elif "irritat" in q or "reaction" in q:
                answer = faqs["What should I do if a product irritates my skin?"]

            elif "routine" in q or "steps" in q:
                answer = faqs["What is a basic skincare routine?"]

            elif "multiple products" in q or "many products" in q:
                answer = faqs["Can I use multiple skincare products?"]

            elif "water" in q:
                answer = faqs["Does drinking water cure acne?"]

            elif "uva" in q or "uvb" in q:
                answer = faqs["What is the difference between UVA and UVB?"]

            else:
                answer = None

        if answer:
            st.markdown("### 🌿 Your Answer")
            st.success(answer)

        else:
            st.info(
                "I don't have a verified answer for that question yet. "
                "Try asking about sunscreen, acne, moisturiser, "
                "ingredients or skincare basics. For personal skin "
                "concerns, consult a qualified dermatologist."
            )

    st.divider()

    st.markdown("### 🌷 A Little Reminder")

    st.caption(
        "Skincare information is educational and cannot replace "
        "professional medical advice or a dermatologist's diagnosis."
    )


# Routine Generator

elif page == "Routine Generator":

    st.markdown("""
    <h1 style="color:#59483F; font-family:Georgia,serif;">
        🌿 Your Personal Skincare Routine
    </h1>
    <p style="color:#8B7568; font-size:16px;">
        A simple routine based on your skin type and concerns.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("### 🌷 Tell Us About Your Skin")

    skin_type = st.selectbox(
        "Select your skin type:",
        ["Normal", "Dry", "Oily", "Combination", "Sensitive", "Not sure"],
        key="routine_skin_type"
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
        ],
        key="routine_concern"
    )

    if st.button("✨ Generate My Routine", key="generate_routine"):

        st.markdown("## 🌿 Your Personalised Results")

        # Skin-type guidance
        skin_tips = {
            "Dry": "Focus on maintaining skin hydration. Choose a gentle cleanser and a moisturiser that supports the skin barrier.",
            "Oily": "Choose lightweight, non-comedogenic products. Avoid repeatedly washing your face to remove oil.",
            "Combination": "Keep your routine balanced. Different areas of your face may feel comfortable with different product textures.",
            "Sensitive": "Choose gentle, fragrance-free products. Introduce new products one at a time.",
            "Normal": "Maintain a simple routine with gentle cleansing, moisturising and sun protection.",
            "Not sure": "Begin with a simple routine and notice how your skin responds to different products."
        }

        # Concern-specific guidance
        concern_tips = {
            "No major concern": "Maintain consistent basic skincare instead of adding unnecessary products.",
            "Dryness": "Use a gentle cleanser and moisturise regularly, especially after washing your face.",
            "Oiliness": "Avoid harsh cleansers and choose lightweight skincare products.",
            "Occasional pimples": "Avoid picking pimples. Use gentle skincare and seek professional advice if breakouts persist.",
            "Uneven skin tone": "Daily broad-spectrum sunscreen is an important part of protecting your skin from sun exposure.",
            "Sensitivity": "Avoid products that cause irritation. Keep your routine simple and fragrance-free."
        }

        # Morning routine variations
        morning_tips = {
            "Dry": "Use a gentle cleanser, apply a moisturiser and finish with broad-spectrum SPF 30+ sunscreen.",
            "Oily": "Cleanse gently, apply a lightweight moisturiser and finish with broad-spectrum SPF 30+ sunscreen.",
            "Combination": "Use a gentle cleanser, apply a comfortable moisturiser and finish with broad-spectrum SPF 30+ sunscreen.",
            "Sensitive": "Use a mild cleanser or rinse gently with water, apply a fragrance-free moisturiser and finish with a suitable SPF 30+ sunscreen.",
            "Normal": "Cleanse gently, moisturise and apply broad-spectrum SPF 30+ sunscreen.",
            "Not sure": "Start with gentle cleansing, a suitable moisturiser and broad-spectrum SPF 30+ sunscreen."
        }

        # Night routine variations
        night_tips = {
            "Dry": "Gently cleanse your face and apply a moisturiser that helps reduce moisture loss.",
            "Oily": "Remove the day's dirt and sunscreen with a gentle cleanser, then apply a lightweight moisturiser.",
            "Combination": "Cleanse gently and apply a moisturiser that feels comfortable on your skin.",
            "Sensitive": "Use a gentle cleanser and a fragrance-free moisturiser. Avoid introducing several new products together.",
            "Normal": "Cleanse gently to remove the day's dirt and sunscreen, then moisturise.",
            "Not sure": "Keep your evening routine simple with gentle cleansing and moisturising."
        }

        st.markdown("### ☀️ Your Morning Routine")
        st.success(morning_tips[skin_type])

        st.markdown("### 🌙 Your Night Routine")
        st.info(night_tips[skin_type])

        st.markdown("### 🌸 Guidance for Your Main Concern")
        st.write(concern_tips[concern])

        st.markdown("### 🌿 Why This Routine?")
        st.write(skin_tips[skin_type])
        st.write("Your selected concern is **" + concern + "**, so the routine also includes guidance related to that concern.")

        st.markdown("### 🚫 Things to Keep in Mind")

        if skin_type == "Sensitive" or concern == "Sensitivity":
            st.warning("Avoid products that cause irritation. Introduce new products one at a time.")

        elif skin_type == "Oily" or concern == "Oiliness":
            st.warning("Avoid harsh cleansing and excessive washing. These can irritate your skin.")

        elif skin_type == "Dry" or concern == "Dryness":
            st.warning("Avoid very hot water and harsh cleansers that may leave your skin feeling dry.")

        else:
            st.info("Avoid adding too many products at once. A simple, consistent routine is a good starting point.")

        st.caption(
            "🌷 This tool provides general skincare education, "
            "not medical diagnosis or treatment. Consult a dermatologist "
            "for persistent or concerning skin problems."
        )



# Skin Concerns

elif page == "Skin Concerns":

    st.markdown("""
    <h1 style="color:#59483F; font-family:Georgia,serif;">
        🔍 Understanding Your Skin
    </h1>
    <p style="color:#8B7568;">
        Explore common skin concerns and learn about gentle skincare practices.
    </p>
    """, unsafe_allow_html=True)

    concerns = {
        "Dry Skin": {
            "meaning": "Dry skin occurs when the skin does not retain enough moisture. It may feel tight, rough or flaky.",
            "factors": [
                "Cold or dry weather",
                "Frequent washing with harsh cleansers",
                "Hot showers",
                "Products that irritate or dry the skin"
            ],
            "care": [
                "Use a gentle, non-stripping cleanser.",
                "Apply a suitable moisturiser regularly.",
                "Avoid very hot water.",
                "Moisturise after bathing while the skin is slightly damp."
            ],
            "avoid": "Harsh soaps, excessive exfoliation and very hot water."
        },

        "Oily Skin": {
            "meaning": "Oily skin produces more sebum, the natural oil made by sebaceous glands. It may appear shiny, particularly around the forehead, nose and chin.",
            "factors": [
                "Genetics",
                "Hormonal changes",
                "Environmental conditions",
                "Some skincare or cosmetic products"
            ],
            "care": [
                "Cleanse gently without scrubbing.",
                "Choose lightweight, non-comedogenic moisturisers.",
                "Use suitable broad-spectrum sunscreen.",
                "Avoid repeatedly washing your face."
            ],
            "avoid": "Harsh cleansers and excessive washing to remove natural skin oils."
        },

        "Acne": {
            "meaning": "Acne is a common skin condition involving blocked hair follicles. It can appear as blackheads, whiteheads and inflamed spots.",
            "factors": [
                "Excess sebum production",
                "Blocked hair follicles",
                "Hormonal changes",
                "Genetic factors"
            ],
            "care": [
                "Cleanse gently.",
                "Choose non-comedogenic skincare products.",
                "Avoid picking or squeezing spots.",
                "Maintain a consistent, simple routine."
            ],
            "avoid": "Scrubbing, picking spots and trying several new products at once."
        },

        "Sensitive Skin": {
            "meaning": "Sensitive skin may react easily to certain skincare products or environmental conditions. It may feel uncomfortable, itchy or irritated.",
            "factors": [
                "Fragrance in certain products",
                "Environmental changes",
                "Harsh cleansing products",
                "Individual skin barrier differences"
            ],
            "care": [
                "Choose gentle, fragrance-free products.",
                "Introduce new products one at a time.",
                "Try a small-area patch test before using a new product.",
                "Keep your skincare routine simple."
            ],
            "avoid": "Products that cause irritation and unnecessary product layering."
        },

        "Uneven Skin Tone": {
            "meaning": "Uneven skin tone refers to areas of skin that appear darker or differently coloured than surrounding areas.",
            "factors": [
                "Sun exposure",
                "Post-inflammatory changes after skin irritation",
                "Hormonal influences",
                "Individual skin characteristics"
            ],
            "care": [
                "Use broad-spectrum SPF 30+ sunscreen.",
                "Avoid picking or irritating the skin.",
                "Choose gentle skincare products.",
                "Seek professional advice if changes are new or concerning."
            ],
            "avoid": "Unverified skin-lightening products and harsh home remedies."
        }
    }

    selected = st.selectbox(
        "🌸 Select a skin concern:",
        list(concerns.keys()),
        key="skin_concern_select"
    )

    details = concerns[selected]

    st.markdown("---")

    st.markdown("### 📖 Understanding the Concern")
    st.write(details["meaning"])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔎 Common Contributing Factors")
        for factor in details["factors"]:
            st.markdown("- " + factor)

    with col2:
        st.markdown("### 🌿 Everyday Care")
        for tip in details["care"]:
            st.markdown("- " + tip)

    st.markdown("### 🚫 What to Avoid")
    st.warning(details["avoid"])

    st.markdown("### 💡 Did You Know?")
    st.info(
        "Skin can change over time due to age, hormones, weather "
        "and environmental conditions. A skincare routine should "
        "be gentle and adjusted according to comfort."
    )

    st.caption(
        "DermaBot provides general skincare education, not diagnosis "
        "or treatment. Consult a qualified dermatologist for persistent, "
        "painful or worsening skin concerns."
    )


st.divider()

st.caption("DermaBot AI | Class XII Artificial Intelligence Project")
