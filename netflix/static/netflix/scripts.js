document.addEventListener("DOMContentLoaded", () => {
    console.log("Netflix Clone Loaded ✅");

    const trailerModal = document.getElementById("trailerModal");
    const trailerFrame = document.getElementById("trailerFrame");
    const trailerTitle = document.getElementById("trailerTitle");

    if (trailerModal) {
        trailerModal.addEventListener("show.bs.modal", event => {
            const button = event.relatedTarget;
            const trailerUrl = button.getAttribute("data-trailer");
            const movieTitle = button.getAttribute("data-title");

            if (trailerUrl) {
                const embedUrl = trailerUrl.replace("watch?v=", "embed/");
                trailerFrame.src = embedUrl;
            }
            if (movieTitle) {
                trailerTitle.textContent = `${movieTitle} - Trailer`;
            }
        });

        trailerModal.addEventListener("hidden.bs.modal", () => {
            trailerFrame.src = ""; // Stop video
        });
    }
});