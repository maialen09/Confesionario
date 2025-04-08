// Llamar a la base de datos para obtener la lista de todas las confesiones 
// Por cada confesión, crear un elemento en la lista (li)

fetch('/comprobar_usuario', {
    method: 'GET',
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