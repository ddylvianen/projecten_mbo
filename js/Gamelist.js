
const images = document.querySelectorAll(".Afbeeldingen img");
const popup = document.querySelector(".popup");
const overlay = document.querySelector(".overlay");
const popupImage = document.getElementById("popup-image");
const popupTitle = document.getElementById("popup-title");
const popupDescription = document.getElementById("popup-description");

images.forEach((image) => {
    image.addEventListener("click", () => {
        popupImage.src = image.dataset.image;
        popupTitle.textContent = image.dataset.title;
        popupDescription.textContent = image.dataset.description;

        popup.style.display = "flex"; 
        overlay.style.display = "block"; 
    });
});

overlay.addEventListener("click", () => {
    popup.style.display = "none"; 
    overlay.style.display = "none"; 
});

document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
        popup.style.display = "none";
        overlay.style.display = "none";
    }
});
