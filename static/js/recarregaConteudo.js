var link = window.location.href
setInterval(function(){
    fetch(link+'/?type=json')
    .then(response => response.json())
    .then(json=>{
        let tempo = json['tempo']
        let tempo_img = json['tempo_img']
        let tempoProxDias = json['tempoProxDias']
        let cor = json['cor']
        
        fetch(link+'mudaLuz',{
            method: 'POST',
            body: JSON.stringify(json['tempo']['condition_slug']),
            headers: {"Content-type": "application/json; charset=UTF-8"}
        })
        .then(response => response.json())
        .catch(error => console.log(error));
    });
},10000)

