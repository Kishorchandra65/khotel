const track = document.getElementById('carouselTrack');
const slides = Array.from(track.children);
const nextButton = document.getElementById('nextBtn');
const prevButton = document.getElementById('prevBtn');
const indicators = Array.from(document.querySelectorAll('.indicator'));

let currentIndex = 0;

// Function to update slide position
const updateSlidePosition = () => {
    const slideWidth = slides[0].getBoundingClientRect().width;
    track.style.transform = `translateX(-${slideWidth * currentIndex}px)`;
    updateIndicators();
};

// Function to update indicators
const updateIndicators = () => {
    indicators.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
    });
};

// Next button click
nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % slides.length;
    updateSlidePosition();
});

// Previous button click
prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateSlidePosition();
});

// Indicator click
indicators.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        currentIndex = index;
        updateSlidePosition();
    });
});

// Optional: auto-slide every 5 seconds
setInterval(() => {
    currentIndex = (currentIndex + 1) % slides.length;
    updateSlidePosition();
}, 5000);

// Initialize carousel
updateSlidePosition();
