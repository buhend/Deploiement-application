import streamlit as st

st.title("Prédiction de la catégorie de poids")

st.write("Ceci est un exemple d'une application qui prédit la catégorie de poids des individus en fonction de leur IMC.")

nom = st.text_input("Entrer votre nom")
if nom:
    st.write("Bonjour ", nom)

    taille = st.number_input("Entrer votre taille (en cm)", min_value=50, max_value=250, step=1)
    poids = st.number_input("Entrer votre poids (en kg)", min_value=10, max_value=200, step=1)

def calculer_imc(taille, poids):
    taille_m = taille / 100  # Conversion de la taille en mètres
    imc = poids / ((taille_m) ** 2)
    return imc

def predire_categorie(imc):
    if imc < 18.5:
        return "sous-poids"
    elif 18.5 <= imc < 24.9:
        return "poids normal"
    elif 25 <= imc < 29.9:
        return "surpoids"
    else:
        return "obésité"

if st.button("Prédire"):
    imc = calculer_imc(taille, poids)
    categorie = predire_categorie(imc)
    st.write(f"Votre IMC est de {imc:.2f}") #Vous êtes probablement en ** quote = random.choice(quotes[category])

