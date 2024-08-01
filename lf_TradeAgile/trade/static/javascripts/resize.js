window.addEventListener('resize', () => {
    const container = document.querySelector('.container');
    container.style.height = `${window.innerHeight}px`;
});

// Inicializa a altura ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.container');
    container.style.height = `${window.innerHeight}px`;
});
