document.addEventListener("DOMContentLoaded", () => {
    const btnPublicar = document.getElementById("btnPublicar");
    const tituloConfesion = document.getElementById("titulo");
    const textoConfesion = document.getElementById("cuerpo");

   

    btnPublicar.addEventListener("click", function() {

      const titulo = tituloConfesion.value.trim();
      const confesion = textoConfesion.value.trim();

      let errores = [];
        if (!titulo) {  
          errores.push("El titulo vacio")
          alert("El Titulo está vacío o contiene solo espacios.");
        }
        else{
          const longitudValidaTitulo = titulo.length >= 5 && titulo.length < 70;
          if(!longitudValidaTitulo){
              errores.push("longitud incorrecta de titulo")
              alert("Pon un titulo de entre 5 y 70 caracteres");
          }
        }

        if (!confesion) { 
          errores.push("Confesion vacio") 
          alert("La confesion está vacía o contiene solo espacios."); 
        }
        else{
          const longitudValidaConfesion = confesion.length >= 50 && confesion.length < 10000;
          if(!longitudValidaConfesion){
              errores.push("longitud incorrecta de confesion")
              alert("Pon una confesion de entre 50 y 10000 caracteres");
          }
      }

        if(errores.length == 0){
          fetch('/insertar_confesion', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title: titulo, conf: confesion})
          })
          .then(response => response.json())
          .then(data => {
            const existe = data.existe;
            if(existe){
              window.location.href = `/home`; // Redirige a otra página

            }
          })
          .catch(error => console.error('Error al obtener el nombre de usuario'))
        }
    });
});