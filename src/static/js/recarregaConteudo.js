var link = window.location.href;


// const link = window.location.href;

// const estado = document.getElementById('estado');
// const modo = document.getElementById('modo');


setInterval(function () {
    fetch(link + '/?type=json')
        .then((response) => response.json())
        .then((json) => {
            let tempo = json['tempo'];
            let tempo_img = json['tempo_img'];
            let tempoProxDias = json['tempoProxDias'];
            let cor = json['cor'];
            let tagsInfos = ['city', 'imagem'];

            document.getElementById('city').innerHTML = tempo['city'];
            document.getElementById('imagem').innerHTML = tempo_img;
            document.getElementById('corFundo').style.backgroundColor = cor;
            document.getElementById('temperatura').innerHTML = tempo['temp'] + '°';
            document.getElementById('descricao').innerHTML = tempo['description'];
            document.getElementById('vento').innerHTML = 'Vento: ' + tempo['wind_speedy'];
            document.getElementById('umidade').innerHTML = 'Umidade: ' + tempo['humidity'];
            document.getElementsByClassName('trailerSlider').innerHTML = null;
            let auxiliar = '';

            for (let i = 0; i < 10; i++) {
                let week = tempo['forecast'][i].weekday;
                let date = tempo['forecast'][i].date;
                let max = tempo['forecast'][i].max;
                let min = tempo['forecast'][i].min;
                let description = tempo['forecast'][i].description;
                if (i === 0) {
                    auxiliar += `<div class="carousel-item active">${adicionaRole(week, date, max, min, description)}</div>`;
                } else {
                    auxiliar += `<div class="carousel-item">${adicionaRole(week, date, max, min, description)}</div>`;
                }
            }

            document.getElementsByClassName('trailerSlider').innerHTML = auxiliar;

            fetch(link + 'mudaLuz', {
                method: 'POST',
                body: JSON.stringify(json['tempo']['condition_slug']),
                headers: { 'Content-type': 'application/json; charset=UTF-8' },
            })
                .then((response) => response.json())
                .catch((error) => console.log(error));
        });
}, 500000);

function adicionaRole(weekday, date, max, min, description) {
    return `
    <div id="cover">

        <div class="row">
            <div class="col justify-content-center d-flex">
                <h2>${weekday} -
                    ${date}</h2>

            </div>
            <div class="col justify-content-end d-flex">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16"
                    height="16">
                    <path fill-rule="evenodd"
                        d="M3.22 9.78a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 0l4.25 4.25a.75.75 0 01-1.06 1.06L8 6.06 4.28 9.78a.75.75 0 01-1.06 0z">
                    </path>
                </svg>
                <span
                    style="color: rgb(255, 185, 47);">${max}°</span>

                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16"
                    height="16">
                    <path fill-rule="evenodd"
                        d="M12.78 6.22a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06 0L3.22 7.28a.75.75 0 011.06-1.06L8 9.94l3.72-3.72a.75.75 0 011.06 0z">
                    </path>
                </svg>
                <span$
                    style="color: rgb(38, 199, 248);">${min}°</span>
            </div>
        </div>
        ${description}

    </div>
    `;
}
