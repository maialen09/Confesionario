const btnInicio = document.getElementById("botonInicio");
const textoUsuario = document.getElementById("textUsuario");
const textoContrasena = document.getElementById("textContrasena"); 





btnInicio.addEventListener("click", function(){
    const user = textoUsuario.value.trim(); 
    const contrasena = textoContrasena.value.trim();

    console.log(user)
    console.log(contrasena)

    fetch('/comprobar_usuario', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user: user, contrasena: contrasena})
      })
      .then(response => response.json())
      .then(data => {

        console.log(data.datos)
        
        const success = data.success
        if (success){
            window.location.href = `/home`;
        }
        else{
            alert(data.message); 
        }
        
      })
      .catch(error => console.error('Error al comprobar la existencia del usuario'))


})

