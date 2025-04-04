document.addEventListener("DOMContentLoaded", () => {
    const pass1 = document.getElementById("textContrasena");
    const pass2 = document.getElementById("textContrasena2");
    const mensaje = document.getElementById("mensaje");
  
    function comprobarCoincidencia() {
      if (pass1.value === "" || pass2.value === "") {
        mensaje.textContent = ""; // No mostrar nada si alguno está vacío
        return;
      }
  
      if (pass1.value === pass2.value) {
        mensaje.textContent = "✅ Las contraseñas coinciden";
        mensaje.style.color = "green";
      } else {
        mensaje.textContent = "❌ Las contraseñas no coinciden";
        mensaje.style.color = "red";
      }
    }
  
    // Verifica cada vez que el usuario escribe en uno de los campos
    pass1.addEventListener("input", comprobarCoincidencia);
    pass2.addEventListener("input", comprobarCoincidencia);
  });  