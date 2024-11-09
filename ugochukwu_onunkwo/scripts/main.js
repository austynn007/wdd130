// IIFE to avoid polluting the global scope
(function() {
    // General utility functions or global variables
    let sections, projects, filters;

    // Function to initialize global variables
    function initGlobals() {
        sections = document.querySelectorAll('section');
        projects = document.querySelectorAll('.project-card');
        filters = document.querySelectorAll('.filter');
    }

    // Scroll reveal for all pages
    function scrollReveal() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('reveal');
                    observer.unobserve(entry.target); // Stop observing after reveal for performance
                }
            });
        }, {
            threshold: 0.1
        });

        sections.forEach(section => {
            observer.observe(section);
        });
    }

    // Portfolio filtering (for portfolio page)
    function setupPortfolioFiltering() {
        filters.forEach(filter => {
            filter.addEventListener('click', function(e) {
                e.preventDefault();
                const category = this.getAttribute('data-filter');

                filters.forEach(button => button.classList.remove('active'));
                this.classList.add('active');

                projects.forEach(project => {
                    if (category === 'all' || project.getAttribute('data-category') === category) {
                        project.style.display = 'block';
                    } else {
                        project.style.display = 'none';
                    }
                });
            });
        });
    }

    // Contact form handling (for contact page)
    function setupContactForm() {
        const form = document.getElementById('contact-form');
        if (form) {
            form.addEventListener('submit', function(event) {
                event.preventDefault();
                alert('Form Submitted! Thank you for your message.');
                form.reset();
            });
        }
    }

    // Modal functionality (if used on multiple pages)
    function setupModal() {
        const modal = document.getElementById('project-modal');
        const closeBtn = document.querySelector('.close-modal');

        if (modal && closeBtn) {
            document.querySelectorAll('.project-card .btn:not(.view-site)').forEach(btn => {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    modal.style.display = 'block';
                    // Here you'd typically populate modal with project details
                });
            });

            closeBtn.addEventListener('click', function() {
                modal.style.display = 'none';
            });

            window.addEventListener('click', function(event) {
                if (event.target === modal) {
                    modal.style.display = 'none';
                }
            });
        }
    }

    // Initialize scripts
    document.addEventListener('DOMContentLoaded', () => {
        initGlobals();
        scrollReveal();
        setupPortfolioFiltering();
        setupContactForm();
        setupModal();

        // Any additional page-specific scripts
        if (window.location.pathname.includes('index.html')) {
            // Home page specific scripts
        } else if (window.location.pathname.includes('portfolio.html')) {
            // Portfolio specific scripts
        } else if (window.location.pathname.includes('skills.html')) {
            // Skills page specific scripts
        } else if (window.location.pathname.includes('contact.html')) {
            // Contact page specific scripts
        }
        // Add more conditions for other pages if needed
    });
})();