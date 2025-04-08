document.addEventListener("DOMContentLoaded", () => {
    const pass1 = document.getElementById("textContrasena");
    const pass2 = document.getElementById("textContrasena2");
    const mensaje = document.getElementById("mensaje");
  
    var coincide = false;
    function comprobarCoincidencia() {
      if (pass1.value === "" || pass2.value === "") {
        mensaje.textContent = ""; // No mostrar nada si alguno está vacío
        return;
      }
  
      if (pass1.value === pass2.value) {
        mensaje.textContent = "✅ Las contraseñas coinciden";
        mensaje.style.color = "green";
        coincide = true;
      } else {
        mensaje.textContent = "❌ Las contraseñas no coinciden";
        mensaje.style.color = "red";
        coincide = false;
      }
    }
  
    pass1.addEventListener("input", comprobarCoincidencia);
    pass2.addEventListener("input", comprobarCoincidencia);

    const btnReg = document.getElementById("botonRegistrarse");
  
    btnReg.addEventListener("click", function() {

      // comprobar que no son null ni el usuario ni la contraseña xxxxxxx
      // hacer que la contraseña sea segura y de la longitud adecuada 
      // comprobar que el nombre de usuario no exista ya y que sea de la longitud adecuada
      // avisar si las contraseñas no coinciden 
      // añadir en la base de datos al usuario 

      const textoUsuario = document.getElementById("textUsuario");
      const textoContrasena = document.getElementById("textContrasena"); 

      const user = textoUsuario.value.trim(); 
      const contrasena = textoContrasena.value.trim(); 

      let errores = [];
      if (!user) {  
        errores.push("usuario vacio")
        alert("El nombre de usuario está vacío o contiene solo espacios.");
      }

      if (!contrasena) { 
        errores.push("contrasena vacio") 
        alert("La contraseña está vacía o contiene solo espacios.");
      }
      else {
        const longitudValidaCon = contrasena.length >= 8 && contrasena.length < 100;
        const longitudValidaUsuario = user.length >= 3 && user.length < 100;
        const tieneMayus = /[A-Z]/.test(contrasena);
        const tieneNum = /\d/.test(contrasena);

        if(!tieneNum){
          errores.push("falta numero")
          alert("Falta número");
        }
        if(!tieneMayus){
          errores.push("falta mayuscula")
          alert("Falta mayuscula");
        }
        if(!longitudValidaCon){
          errores.push("longitud incorrecta de contrasena")
          alert("Pon una contraseña de entre 8 y 100 caracteres");
        }
        if(!longitudValidaUsuario){
          errores.push("longitud incorrecta de usuario")
          alert("Pon un usuario de entre 8 y 100 caracteres");
        }
        if(!coincide){
          errores.push("las contrasenas no coinciden")
          alert("Las contraseñas no coinciden idiota");
        }

      }

      if(errores.length == 0){
        fetch('/insertar_usuario', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ user: user, contrasena: contrasena})
        })
        .then(response => response.json())
        .then(data => {
          const existe = data.existe;
          if(existe){
            alert('El usuario ya existe, elige otro')
          }
          else{
            window.location.href = `/home`; // Redirige a otra página
          }
          console.log("El usuario " + existe)
        })
        .catch(error => console.error('Error al obtener el nombre de usuario'))
      }


   

    });
  });  