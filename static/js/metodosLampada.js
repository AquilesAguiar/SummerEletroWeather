// Liga e desliga lampada
var estado = document.getElementsById()
fetch('/lampada/estado',{
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
})
.then(response => response.json())
.catch(err => console.error(err))

//Troca o modo da lampada
var modo = document.getElementsById()
fetch('/lampada/modo',{
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
})
.then(response => response.json())
.catch(err => console.error(err))

//Altera a intensida da lampada
var intensidade = document.getElementsById()
fetch('/lampada/intesidade',{
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
})
.then(response => response.json())
.catch(err => console.error(err))


//Muda a cor da lampada
var mudaCor = document.getElementsById()
fetch('/lampada/mudaCor',{
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
})
.then(response => response.json())
.catch(err => console.error(err))