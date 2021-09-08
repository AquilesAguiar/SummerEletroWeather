//Liga e desliga lampada
var estado = document.getElementById("estado").value
estado.addEventListener("change",function(){
    console.log(estado)
})

console.log(estado)
// fetch('/lampada/estado',{
//     method: "POST",
//     body: JSON.stringify(_data),
//     headers: {"Content-type": "application/json; charset=UTF-8"}
// })
// .then(response => response.json())
// .catch(err => console.error(err))

// //Troca o modo da lampada
// var modo = document.getElementById()
// fetch('/lampada/modo',{
//     method: "POST",
//     body: JSON.stringify(_data),
//     headers: {"Content-type": "application/json; charset=UTF-8"}
// })
// .then(response => response.json())
// .catch(err => console.error(err))

// //Altera a intensida da lampada
// var intensidade = document.getElementById()
// fetch('/lampada/intesidade',{
//     method: "POST",
//     body: JSON.stringify(_data),
//     headers: {"Content-type": "application/json; charset=UTF-8"}
// })
// .then(response => response.json())
// .catch(err => console.error(err))


// //Muda a cor da lampada
// var mudaCor = document.getElementById()
// fetch('/lampada/mudaCor',{
//     method: "POST",
//     body: JSON.stringify(_data),
//     headers: {"Content-type": "application/json; charset=UTF-8"}
// })
// .then(response => response.json())
// .catch(err => console.error(err))