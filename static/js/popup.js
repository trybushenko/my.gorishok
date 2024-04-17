// Function to show the popup
function showAuthPopup() {
  
  document.getElementById('AuthPopup').style.display = 'block';
}

// Function to hide the popup
function hideAuthPopup() {
  document.getElementById('AuthPopup').style.display = 'none';
}

// Attach event listener to all buttons with the class "add-to-cart-button"
document.querySelectorAll('.add-to-cart-button').forEach(button => {
  button.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent default button action
      showAuthPopup(); // Show the authentication popup
  });
});

// Attach event listener to the close button in the popup
document.getElementById('closePopupButton').addEventListener('click', hideAuthPopup);

document.getElementById('loginButton').addEventListener('click', function() {
  // Implement your login function here
  hideAuthPopup(); // Hide the popup after the login action
});
