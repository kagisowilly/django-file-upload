function previewImage(event) {
    const preview = document.getElementById('image-preview');
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function() {
        preview.src = reader.result;
        preview.style.display = 'block';
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const yearElement = document.getElementById("current-year");
    const currentYear = new Date().getFullYear();
    yearElement.textContent = currentYear;
});


function count_down(obj){
    let element = document.getElementById('title');
    let charLimit = document.getElementById('character-limit');

    element.innerHTML = 55 - obj.value.length;

    if(55 - obj.value.length < 5){
        element.style.color = "firebrick";
        charLimit.style.display = "block"
    }else{
        element.style.color = "#333";
        charLimit.style.display = "none"
    }
}
