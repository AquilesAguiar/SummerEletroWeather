//Liga e desliga lampada
var estado = document.getElementById('estado');
estado.addEventListener('click', function () {
    if(estado.checked){
        fetch(link + '/?reset=json').then((response) => response.json()).catch((err) => console.error(err));
    }
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
    if(modo.checked == true) {
        document.getElementById('colorPickerMain').hidden = false;
    }
    if(modo.checked == false) {
        fetch(link + '/?reset=json').then((response) => response.json()).catch((err) => console.error(err));
        document.getElementById('colorPickerMain').hidden = true;
    }

    fetch('/lampada/modo', {
        method: 'POST',
        body: JSON.stringify({ modo: modo.checked }),
        headers: { 'Content-type': 'application/json; charset=UTF-8' },
    })
        .then((response) => response.json())
        .then((json) => '')
        .catch((err) => console.error(err));

});

