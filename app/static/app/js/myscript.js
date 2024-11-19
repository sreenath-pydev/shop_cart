
// JavaScript to toggle password visibility
document.addEventListener('DOMContentLoaded', function () {
    const showPasswordCheckbox = document.getElementById('showPassword');
    if (showPasswordCheckbox) {
        showPasswordCheckbox.addEventListener('change', function () {
            const passwordField = document.getElementById('confirm_password');
            if (passwordField) {
                passwordField.type = this.checked ? 'text' : 'password';
            }
        });
    }
});

// JavaScript for owl carousel
$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        autoplay: true,              
        autoplayTimeout: 3000,        
        autoplayHoverPause: true,     
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    });
});

// Live Search 
let searchTimeout;
function handleLiveSearch(event) {
    clearTimeout(searchTimeout)
    const searchQuery = event.target.value.trim();
    console.log(searchQuery);
    if (searchQuery.length > 0) {
        searchTimeout = setTimeout(() => {
            fetch(`/search/?q=${encodeURIComponent(searchQuery)}`)
                .then(response => {
                    if (!response.ok) throw new Error('Failed to fetch search results');
                    return response.json();
                })
                .then(data => {
                    displaySearchResults(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                    displaySearchError('Failed to load search results.');
                });
        }, 300); 
    } else {
        clearSearchResults();
    }
}

// Function to display search results
function displaySearchResults(data) {
    const resultsContainer = document.getElementById('searchResults');
    console.log(resultsContainer);
    resultsContainer.innerHTML = '';

    if (data && data.products.length > 0) {
        data.products.forEach(product => {
            const resultItem = document.createElement('a');
            resultItem.className = 'dropdown-item d-flex align-items-center';
            resultItem.href = `/product/${product.id}`;
            resultItem.innerHTML = `
                <img src="/media/${product.image}" alt="${product.name}" class="me-3" style="width: 50px; height: 50px; object-fit: cover;">
                <div>
                    <h6 class="m-0">${product.name}</h6>
                    <small class="text-muted">${product.price}</small>
                </div>
            `;

            resultsContainer.appendChild(resultItem);
        });
        resultsContainer.classList.add('show'); 
    } else {
        resultsContainer.innerHTML = '<div class="dropdown-item text-center text-muted">No products found</div>';
        resultsContainer.classList.add('show');
    }
}

function displaySearchError(message) {
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = `<div class="dropdown-item text-danger">${message}</div>`;
    resultsContainer.classList.add('show');
}

function clearSearchResults() {
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = '';
    resultsContainer.classList.remove('show');
}