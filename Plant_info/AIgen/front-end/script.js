async function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('result');
    const uploadedImage = document.getElementById('uploadedImage');
    const responseText = document.getElementById('responseText');

    if (fileInput.files.length === 0) {
        alert("Veuillez sélectionner une image.");
        return;
    }

    // Afficher l'image sélectionnée
    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.onload = function (e) {
        uploadedImage.src = e.target.result;
        uploadedImage.style.display = 'block';
    };
    reader.readAsDataURL(file);

    // Préparer la requête POST vers l'API
    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch('https://plant-id-bys8.onrender.com/upload/', { // URL de l'API
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error("Erreur lors de la requête.");
        }

        const data = await response.json();
        responseText.innerHTML = `<strong>Nom :</strong> ${data.nom}<br>
                                  <strong>Nom scientifique :</strong> ${data.nom_scientifique}<br>
                                  <strong>Famille :</strong> ${data.famille}<br>
                                  <strong>État de la plante :</strong> ${data.etat_plante}<br>
                                  <strong>Description :</strong> ${data.description}<br>`;
    } catch (error) {
        responseText.innerHTML = "Erreur : " + error.message;
    }
}
