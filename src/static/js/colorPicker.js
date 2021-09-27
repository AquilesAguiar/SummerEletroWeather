document.querySelectorAll('input[type=color]').forEach(function (picker) {
    picker.addEventListener('change', function () {
        const cor =
            'rgb(' +
            picker.value
                .match(/[A-Za-z0-9]{2}/g)
                .map(function (v) {
                    return parseInt(v, 16);
                })
                .join(',') +
            ')';
            arrayColor = cor.replace('rgb(', '').replace(')', '').split(',').map((value) => parseInt(value) )
        document.getElementById('corSelecionada').value = cor;
        // Muda a cor da lampada
        fetch('/lampada/mudaCor', {
            method: 'POST',
            body: JSON.stringify({ arrayColor }),
            headers: { 'Content-type': 'application/json; charset=UTF-8' },
        })
            .then((response) => response.json())
            .catch((err) => console.error(err));
    });
});
