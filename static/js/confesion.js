const botonVolver = document.getElementById("btnVolver");
const botonAnadir = document.getElementById("btnAnadir");
const textArea = document.getElementById("comentario_nuevo");
const id = document.getElementById("titulo").dataset.id;
console.log("Id:", id);



botonVolver.addEventListener("click", function() {

    window.location.href = `/home`;
  
}); 

botonAnadir.addEventListener("click", function(){

    var textoComentario = textArea.value; 
    if (textoComentario.trim() === ""){
        alert("Introduce texto para poder crear un comentario"); 
    }
    else{

        textArea.value = ""; 

    fetch('/insertar_comentario', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ textoComentario: textoComentario, idConfesion: id})
      })
      .then(response => response.json())
      .then(data => {
        const resultado = data.resultado;
        if(resultado){
          window.location.reload();

        }
      })
      .catch(error => console.error('Error al intentar añadir el comentario'))

    }

    

}); 