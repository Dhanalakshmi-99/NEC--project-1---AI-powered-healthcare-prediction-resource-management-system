import streamlit as st

st.set_page_config(
    page_title="AI Healthcare Chatbot",
    layout="wide"
)

st.title("🤖 AI Healthcare Chatbot")

st.markdown("""
Ask questions about:
- Fever
- Diabetes
- Blood Pressure
- Stress
- Headache
- Nutrition
- Exercise
- BMI
- Emergency Health Tips
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

question = st.text_input(
    "Ask Your Health Question"
)

if st.button("Send"):

    if question:

        q = question.lower()

        if "fever" in q:

            response = """
### 🌡 Fever Management

✅ Drink plenty of fluids

✅ Take adequate rest

✅ Monitor body temperature

✅ Use prescribed medicines

⚠ Consult doctor if fever exceeds 102°F
"""

        elif "diabetes" in q:

            response = """
### 🍎 Diabetes Care

✅ Avoid sugary foods

✅ Exercise daily

✅ Check blood sugar regularly

✅ Follow prescribed medication

✅ Maintain healthy weight
"""

        elif "stress" in q:

            response = """
### 🧘 Stress Management

✅ Meditation

✅ Deep Breathing

✅ Proper Sleep

✅ Physical Activity

✅ Talk with family/friends

✅ Reduce screen time
"""

        elif "blood pressure" in q or "bp" in q:

            response = """
### ❤️ Blood Pressure Control

✅ Reduce salt intake

✅ Daily exercise

✅ Healthy diet

✅ Avoid smoking

✅ Regular BP monitoring
"""

        elif "headache" in q:

            response = """
### 🤕 Headache Tips

✅ Drink water

✅ Take proper rest

✅ Avoid excessive screen time

✅ Consult doctor if severe
"""

        elif "nutrition" in q:

            response = """
### 🥗 Nutrition Advice

✅ Fruits & Vegetables

✅ Protein Rich Food

✅ Whole Grains

✅ Adequate Water

✅ Avoid Junk Food
"""

        elif "exercise" in q:

            response = """
### 🏃 Exercise Recommendations

✅ Walking 30 Minutes

✅ Cycling

✅ Yoga

✅ Stretching

✅ Light Strength Training
"""

        elif "bmi" in q:

            response = """
### ⚖ BMI Information

BMI = Weight (kg) / Height² (m)

BMI Range:

Underweight < 18.5

Normal = 18.5 - 24.9

Overweight = 25 - 29.9

Obese > 30
"""

        elif "emergency" in q:

            response = """
### 🚨 Emergency Advice

❗ Call emergency services immediately

❗ Keep patient calm

❗ Monitor breathing

❗ Seek nearest hospital
"""

        else:

            response = """
### 🏥 General Healthcare Advice

✅ Eat Healthy

✅ Drink Water

✅ Exercise Daily

✅ Sleep 7-8 Hours

✅ Regular Health Checkups

⚠ For diagnosis consult a healthcare professional.
"""

        st.session_state.messages.append(
            ("You", question)
        )

        st.session_state.messages.append(
            ("AI", response)
        )

for sender, msg in st.session_state.messages:

    if sender == "You":
        st.chat_message("user").write(msg)

    else:
        st.chat_message("assistant").markdown(msg)

st.markdown("---")

st.subheader("⚖ BMI Calculator")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        value=60.0
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=1.0,
        value=170.0
    )

if st.button("Calculate BMI"):

    bmi = weight / ((height/100) ** 2)

    st.metric(
        "BMI",
        round(bmi, 2)
    )

    if bmi < 18.5:
        st.warning("Underweight")

    elif bmi < 25:
        st.success("Normal Weight")

    elif bmi < 30:
        st.warning("Overweight")

    else:
        st.error("Obese")

st.markdown("---")

st.subheader("💡 Daily Health Tips")

tips = [
    "Drink at least 2-3 liters of water daily.",
    "Exercise for 30 minutes every day.",
    "Eat more fruits and vegetables.",
    "Get 7-8 hours of sleep.",
    "Avoid excessive sugar and junk food."
]

for tip in tips:
    st.info(tip)