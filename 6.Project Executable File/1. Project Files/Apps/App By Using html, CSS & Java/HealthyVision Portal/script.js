document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('upload-btn');
    const fileInput = document.getElementById('file-input');
    const resultSection = document.getElementById('result-section');
    const preview = document.getElementById('preview');

    uploadBtn.addEventListener('click', function() {
        fileInput.click();
    });

    fileInput.addEventListener('change', function() {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.src = e.target.result;
                resultSection.style.display = 'grid';

                updateDiseaseInfo(); 
            };
            reader.readAsDataURL(file);
        }
    });

    const diseases = [
        { name: "Cataract Diseases", minPercentage: 95, maxPercentage: 99.9 },
        { name: "Glaucoma", minPercentage: 70, maxPercentage: 85 },
        { name: "Diabetic Retinopathy", minPercentage: 60, maxPercentage: 75 },
        { name: "Normal", minPercentage: 80, maxPercentage: 90 }
    ];

    function getRandomDisease() {
        const randomIndex = Math.floor(Math.random() * diseases.length);
        const disease = diseases[randomIndex];
        const percentage = (Math.random() * (disease.maxPercentage - disease.minPercentage) + disease.minPercentage).toFixed(1);
        return { name: disease.name, percentage: percentage };
    }

    function updateDiseaseInfo() {
        const diseaseNameElement = document.getElementById("disease-name");
        const diseasePercentageElement = document.getElementById("disease-percentage");

        const randomDisease = getRandomDisease();

        diseaseNameElement.textContent = randomDisease.name;
        diseasePercentageElement.textContent = randomDisease.percentage + "%";
    }

    updateDiseaseInfo();
});