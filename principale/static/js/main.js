// Kasa - Main JavaScript

// Document Ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavbar();
    initScrollAnimations();
    initDateInputs();

    const menuToggle = document.querySelector('.navbar-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', toggleMobileMenu);
    }
});

// Navbar scroll effect
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 2px 16px rgba(0, 0, 0, 0.08)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        });
    }
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    document.querySelectorAll('.card, .section > .container').forEach(el => {
        observer.observe(el);
    });
}

// Initialize date inputs with min date
function initDateInputs() {
    const today = new Date().toISOString().split('T')[0];
    document.querySelectorAll('input[type="date"]').forEach(input => {
        input.setAttribute('min', today);
    });
}

// FAQ Accordion (already implemented inline, but can be enhanced)
function initFAQ() {
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', () => {
            const faqItem = question.parentElement;
            const isActive = faqItem.classList.contains('active');
            
            // Close all other items
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
            });
            
            // Toggle current item
            if (!isActive) {
                faqItem.classList.add('active');
            }
        });
    });
}

// Filter buttons
function initFilters() {
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });
}

// Gallery thumbnail click
function initGallery() {
    document.querySelectorAll('.gallery-thumb img').forEach(thumb => {
        thumb.addEventListener('click', () => {
            const mainImg = document.querySelector('.gallery-main img');
            const tempSrc = mainImg.src;
            mainImg.src = thumb.src;
            thumb.src = tempSrc;
        });
    });
}

// Form validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], select[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = '#C46A4A';
        } else {
            input.style.borderColor = '#E5E5E5';
        }
    });
    
    return isValid;
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Mobile menu toggle (for future implementation)
function toggleMobileMenu() {
    const navbarLinks = document.querySelector('.navbar-links');
    if (navbarLinks) {
        navbarLinks.classList.toggle('active');
    }
}

// Price calculator for booking form
function calculateTotal(checkIn, checkOut, pricePerNight) {
    if (!checkIn || !checkOut) return 0;
    
    const startDate = new Date(checkIn);
    const endDate = new Date(checkOut);
    const nights = Math.ceil((endDate - startDate) / (1000 * 60 * 60 * 24));
    
    if (nights <= 0) return 0;
    
    const basePrice = nights * pricePerNight;
    const cleaningFee = 25000;
    const serviceFee = 15000;
    
    return basePrice + cleaningFee + serviceFee;
}

// Export functions for use in templates
window.Kasa = {
    initFAQ,
    initFilters,
    initGallery,
    validateForm,
    calculateTotal,
    toggleMobileMenu
};
