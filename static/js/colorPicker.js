document.querySelectorAll('input[type=color]').forEach(function (picker) {

    var targetLabel = document.querySelector('label[for="' + picker.id + '"]')
    /* PEGA O VALOR RGB */
    //,
    // codeArea = document.createElement('span');
    
    codeArea.innerHTML = picker.value;
    targetLabel.appendChild(codeArea);
    
    picker.addEventListener('change', function () {
        /* PEGA O VALOR RGB */
        // codeArea.innerHTML = picker.value;
        console.log(picker.value);
        // targetLabel.appendChild(codeArea);
    });
});