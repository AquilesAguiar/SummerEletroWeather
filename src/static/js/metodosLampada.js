//Liga e desliga lampada
var estado = document.getElementById('estado');
estado.addEventListener('click', function () {
    fetch('lampada/estado', {
        method: 'POST',
        body: JSON.stringify({ estado: estado.checked }),
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
    })
        .then((response) => response.json())
        .then((json) => '')
        .catch((err) => console.error(err));
});

//Troca o modo da lampada
var modo = document.getElementById('modo');
modo.addEventListener('click', function () {
    fetch('/lampada/modo', {
        method: 'POST',
        body: JSON.stringify({ modo: modo.checked }),
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
    })
        .then((response) => response.json())
        .then((json) => '')
        .catch((err) => console.error(err));
});

// //Altera a intensida da lampada
function enviaItensidade(valor) {
    fetch('/lampada/intesidade', {
        method: 'POST',
        body: JSON.stringify({ valor: valor.value }),
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
    })
        .then((response) => response.json())
        .then((json) => '')
        .catch((err) => console.error(err));
}
