const botonAnadir = document.getElementById("btnAnadir")
const botonConectar = document.getElementById("btnConectar")
const botonMisConfesiones = document.getElementById("btnMisConfesiones")

botonAnadir.addEventListener("click", function() {

  window.location.href = `/crear_confesion`; 

})

botonConectar.addEventListener("click", function() {

  window.location.href = `/conectar`; 

})

botonMisConfesiones.addEventListener("click", function() {

  window.location.href = `/mis_confesiones`; 

})