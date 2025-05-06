function toggleDescription(id) {
    const short = document.getElementById('desc-short-' + id);
    const full = document.getElementById('desc-full-' + id);
    const btn = document.getElementById('desc-toggle-' + id);

    if (short.classList.contains('d-none')) {
        short.classList.remove('d-none');
        full.classList.add('d-none');
        btn.innerText = 'Zobrazit více';
    } else {
        short.classList.add('d-none');
        full.classList.remove('d-none');
        btn.innerText = 'Skrýt';
    }
}