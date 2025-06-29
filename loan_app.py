import streamlit as st

def calculate_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)**-months)
    return round(payment, 2)

st.set_page_config(page_title="מחשבון הלוואות", layout="centered")
st.title("💳 מחשבון הלוואות")

amount = st.number_input("💵 סכום ההלוואה (₪)", min_value=0.0, step=100.0)
rate = st.number_input("📈 ריבית שנתית (%)", min_value=0.0, step=0.1)
years = st.number_input("📅 מספר שנים", min_value=1, step=1)

if st.button("חשב החזר חודשי"):
    if amount > 0 and rate > 0 and years > 0:
        payment = calculate_payment(amount, rate, years)
        st.success(f"ההחזר החודשי שלך הוא: ₪{payment}")
    else:
        st.error("נא למלא את כל השדות במספרים תקינים.")
