import streamlit as st
def calculate_emi(p,n,r):
     emi = p* (r/100) *(1+(r/100)**n) * (1/((1+(r/100)**n)-1))

def calculate_outstanding_balance(p,n,r,m):
  balance = (p * ((1+r/100)**n - (1+r/100)**m) )/ ((1+r/100)**n - 1)
st.title('Improvised EMI Calculator')
principal = st.slider("Principal", 10000, 50000)
tenure = st.slider("Tenure", 1, 30)
roi = st.slider("Rate of interest", 1.00, 15.00)
m = st.slider("Period after which the Outstanding Loan Balance is calculated(in months)", 1, (tenure * 12))

n = tenure * 12
r = roi / 12

if st.button('Calculate EMI'):
  calculated_emi = calculate_emi(principal, n, r)
  st.write('Principal:',principal)
  st.write('Tenure',tenure)
  st.write('Roi:',roi)

if st.button('Calculate Outstanding Balance'):
  balance = calculate_outstanding_balance(principal,n,r,m)
  st.write('Outstanding balance:',balance)