function alerta() {
    alert("Django NUTS !!!!");
}

function alerta_python(){
    alert("PYTHON NUTS !!!")
}

logo = document.getElementsByTagName("img")[0]
logo.onclick = alerta;

logo2 = document.getElementsByTagName("img")[1]
logo2.onclick = alerta_python
