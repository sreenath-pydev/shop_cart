
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
