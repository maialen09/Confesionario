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

      if (!user) {  
        alert("El nombre de usuario está vacío o contiene solo espacios.");
      }

      if (!contrasena) {  
        alert("La contraseña está vacía o contiene solo espacios.");
      }
      else {
        const longitudValidaCon = contrasena.length >= 8 && contrasena.length < 100;
        const longitudValidaUsuario = user.length >= 8 && user.length < 100;
        const tieneMayus = /[A-Z]/.test(contrasena);
        const tieneNum = /\d/.test(contrasena);

        if(!tieneNum){
          alert("Falta número");
        }
        if(!tieneMayus){
          alert("Falta mayuscula");
        }
        if(!longitudValidaCon){
          alert("Pon una contraseña de entre 8 y 100 caracteres");
        }
        if(!longitudValidaUsuario){
          alert("Pon un usuario de entre 8 y 100 caracteres");
        }
        if(!coincide){
          alert("Las contraseñas no coinciden idiota");
        }
      }

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
        console.log("El usuario " + existe)
      })
      .catch(error => console.error('Error al obtener el nombre de usuario'))


      




    });
  });  