function showWelcomeMessage() {
    alert("Welcome to the Dashboard!");
}

// Function to log dashboard items selected
function logSelectedDashboardItems(selectedItems) {
    console.log("Selected dashboard items:", selectedItems);
}

// Add color highlights to menu items on hover and click
function styleMenuItems() {
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.addEventListener('mouseover', function() {
            // Green/white highlight on hover
            this.style.background = 'linear-gradient(90deg, #008000 50%, #fff 50%)';
            this.style.color = '#000';
        });
        item.addEventListener('mouseout', function() {
            // Reset to original
            this.style.background = '';
            this.style.color = '';
        });
        item.addEventListener('click', function() {
            // Red/white highlight on click
            this.style.background = 'linear-gradient(90deg, #ff0000 50%, #fff 50%)';
            this.style.color = '#fff';
            setTimeout(() => {
                this.style.background = '';
                this.style.color = '';
            }, 500);
        });
    });
}

// Run the welcome message when the page loads
window.onload = function() {
    showWelcomeMessage();
    styleMenuItems();

    // Example: Get checked dashboard items if you have checkboxes with class 'dashboard-checkbox'
    let checkboxes = document.querySelectorAll('.dashboard-checkbox:checked');
    let selectedItems = Array.from(checkboxes).map(cb => cb.value);
    logSelectedDashboardItems(selectedItems);
};