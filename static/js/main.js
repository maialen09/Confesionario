// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    // Obtener el botón
    const btnIr = document.getElementById("botonRegi");
  
    // Asignar el evento de clic al botón
    btnIr.addEventListener("click", function() {
      // Cambiar a otra página cuando el botón sea clickeado
      window.location.href = `/registro`; 
      // O si prefieres abrir en una nueva ventana:
      // window.open("otra_pagina.html", "_blank");
    });

    const btnInicio = document.getElementById("botonIni");

    btnInicio.addEventListener("click", function() {
      // Cambiar a otra página cuando el botón sea clickeado
      window.location.href = `/inicio_de_sesion`; // Redirige a otra página
      // O si prefieres abrir en una nueva ventana:
      // window.open("otra_pagina.html", "_blank");
    });


  });
  