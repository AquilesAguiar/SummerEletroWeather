document.querySelectorAll('input[type=color]').forEach(function (picker) {    
    picker.addEventListener('change', function () {
        const cor = "rgb(" + picker.value.match(/[A-Za-z0-9]{2}/g).map(function(v) { return parseInt(v, 16) }).join(",") + ")";
        document.getElementById('corSelecionada').value = cor
    });
});

