document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-cart-button').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const productId = button.getAttribute('data-product-id');
            const quantity = document.getElementById('inputQuantity').value;

            fetch("/cart/add/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ product_id: productId, quantity: quantity })
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
                } else if (data.status === 'fail' && data.message === 'Authentication required') {
                    document.getElementById('AuthPopup').style.display = 'block';
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
