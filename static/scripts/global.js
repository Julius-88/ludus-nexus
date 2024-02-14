// --------------------------------------Toggle Mode Script ----------------------------------------

// Function to apply the theme based on local storage or default to dark mode
function applyTheme() {
    const body = document.body;
    const savedTheme = localStorage.getItem('theme');

    // Remove both classes to avoid conflicts
    body.classList.remove('dark-mode', 'light-mode');

    // Apply the saved theme or default to dark mode
    if (savedTheme === 'light-mode') {
        body.classList.add('light-mode');
    } else {
        body.classList.add('dark-mode');
    }
}

// Function to toggle the theme and update local storage
function toggleTheme() {
    const body = document.body;
    const isDarkMode = body.classList.contains('dark-mode');

    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');

    localStorage.setItem('theme', isDarkMode ? 'light-mode' : 'dark-mode');
}

// Apply the theme immediately when the script loads
applyTheme();

// Event listener for the theme switcher button
document.addEventListener('DOMContentLoaded', () => {
    const changeTheme = document.getElementById('theme-switcher');
    if (changeTheme) {
        changeTheme.addEventListener('click', toggleTheme);
    }
});
