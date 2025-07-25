# fichier: app.py
import streamlit as st
import joblib

model = joblib.load("meilleur_modele.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Prédiction de log SIEM")
log_input = st.text_area("Entrez un log ici :")

if st.button("Prédire"):
    X_input = vectorizer.transform([log_input])
    prediction = model.predict(X_input)[0]
    st.success(f"Classe prédite : {prediction}")
