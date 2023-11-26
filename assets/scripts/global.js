const changeTheme = document.getElementById('theme-switcher');

changeTheme.addEventListener('click', () => {
    const body = document.body;
    body.classList.toggle('dark-mode');
    body.classList.toggle('light-mode');
});