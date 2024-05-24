document.addEventListener('DOMContentLoaded', (event) => {
    const showAuthPopupButton = document.getElementById('showAuthPopup');
    const authPopup = document.getElementById('AuthPopup');
    const closePopupButton = document.getElementById('closePopupButton');
    const continueAsGuestButton = document.getElementById('continueAsGuestButton');

    // Check if the user is authenticated by reading the data attribute
    const userIsAuthenticated = document.querySelector('form').dataset.userAuthenticated === 'true';

    function getCsrfToken() {
        const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
        return csrfTokenElement ? csrfTokenElement.value : '';
    }

    // Function to show the popup
    function showPopup() {
        event.preventDefault();
        authPopup.style.display = 'block';
    }

    // Function to hide the popup
    function hidePopup() {
        authPopup.style.display = 'none';
    }

    // Function to create a guest session and redirect to cart
    function continueAsGuest() {
        const csrfToken = getCsrfToken();
        if (!csrfToken) {
            console.error('CSRF token not found.');
            return;
        }

        fetch('/user/continue_as_guest/', {  // Update URL here
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({})
        }).then(response => response.json()).then(data => {
            hidePopup();
            window.location.href = data.redirect_url;
        }).catch(error => {
            console.error('Error:', error);
        });
    }

    // Event listener for the cart button
    showAuthPopupButton.addEventListener('click', (event) => {
        event.preventDefault();

        // Check if user is authenticated (this part is server-side logic rendered into the template)
        console.log(userIsAuthenticated);

        if (!userIsAuthenticated) {
            showPopup();
        } else {
            window.location.href = '/cart/'; // Replace '/cart' with the actual URL of your cart page
            hidePopup();
        }
    });

    closePopupButton.addEventListener('click', (event) => {
        hidePopup();
    });

    continueAsGuestButton.addEventListener('click', (event) => {
        event.preventDefault();
        continueAsGuest();
        hidePopup();
    });
});