const toggle = document.getElementById('theme-toggle');
const currentTheme = localStorage.getItem('afaiks-theme');
if (currentTheme === 'dark') {
    document.body.classList.add('dark');
}

if (toggle) {
    toggle.addEventListener('click', () => {
        document.body.classList.toggle('dark');
        const theme = document.body.classList.contains('dark') ? 'dark' : 'light';
        localStorage.setItem('afaiks-theme', theme);
    });
}
