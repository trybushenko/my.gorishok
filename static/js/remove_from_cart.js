document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.remove-from-cart-button').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const productId = button.getAttribute('data-product-id');

            fetch("/cart/remove/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ product_id: productId })
            })
            .then(response => {
                if (response.status === 403) {
                    throw new Error('Forbidden');
                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'success') {
                    alert(data.message);
                    // Optionally remove the item from the DOM or refresh the cart
                    location.reload(); // Refresh the page to update the cart
                }
            })
            .catch(error => {
                console.error('Error:', error);
                if (error.message === 'Forbidden') {
                    alert('CSRF token missing or incorrect.');
                }
            });
        });
    });
});
