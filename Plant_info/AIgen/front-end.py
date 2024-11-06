import streamlit as st
import requests

# URL de l'API
api_url = "https://plant-id-bys8.onrender.com/upload/"
MAX_FILE_SIZE_MB = 20
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

# Titre de l'application
st.title("🌿 Identification des Plantes")
st.write("Télécharge une image d'une plante pour obtenir des informations.")

# Téléchargement de l'image
uploaded_file = st.file_uploader("Choisir une image (max 20 Mo)...", type=["jpg", "jpeg", "png"])
c1, c2 = st.columns(2)

# Vérification de la taille du fichier
if uploaded_file is not None:
    if uploaded_file.size > MAX_FILE_SIZE_BYTES:
        st.error(f"Le fichier est trop volumineux. La taille maximale autorisée est de {MAX_FILE_SIZE_MB} Mo.")
    else:
        c1.image(uploaded_file, caption='Image chargée', use_column_width=True)
        
        # Appel de l'API avec indicateur de chargement
        with st.spinner("Identification en cours... Veuillez patienter."):
            files = {"file": (uploaded_file.name, uploaded_file, "image/jpeg")}
            try:
                response = requests.post(api_url, files=files)
                response.raise_for_status()
                plant_info = response.json().get("réponse", "")
                
                # Affichage des informations avec sections et expandeur pour les détails
                c2.subheader("📝 Informations principales")
                c2.markdown(plant_info)

            except requests.exceptions.RequestException as e:
                c2.error(f"Erreur lors de la requête : {e}")
            except ValueError:
                c2.error("Erreur lors de la lecture de la réponse. Assurez-vous que l'API retourne un JSON.")
