function emite_alerta_python(){
    alert("Python rocks!");
}
function emite_alerta_django(){
    alert("Welcome to the Django!");
}

logo = document.getElementsByTagName("img")[0]
logo.onclick = emite_alerta_python;

logo = document.getElementsByTagName("img")[1]
logo.onclick = emite_alerta_django;