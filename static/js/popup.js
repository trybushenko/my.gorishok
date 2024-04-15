document.getElementById('addToCartButton').addEventListener('click', function(event) {
  event.preventDefault(); // Prevent the default action of the button
  
  // Read user's authentication status from the button's data attribute
  var userAuthorized = this.dataset.userAuthorized === 'true';
  
  if (!userAuthorized) {
      // If the user is not authorized, display the popup
      document.getElementById('authPopup').style.display = 'block';
  } else {
      // If the user is authorized, proceed with the default action (e.g., add to cart)
      // Add your code here for handling authorized user actions
  }
});
