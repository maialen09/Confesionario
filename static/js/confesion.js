const botonVolver = document.getElementById("btnVolver");
const botonAnadir = document.getElementById("btnAnadir");
const botonLike = document.getElementById("btnLike");
const textArea = document.getElementById("comentario_nuevo");
const id = document.getElementById("titulo").dataset.id;
const likeButtons = document.querySelectorAll('.like-button');

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


likeButtons.forEach(button => {
  const comment_id = button.dataset.id_coment;
  
  console.log(comment_id);  // Esto debería imprimir el ID de cada comentario en la consola

  // Añadir el evento de like al botón
  button.addEventListener('click', function() {

    fetch('/incrementar_like', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ idComentario: comment_id})
    })
    .then(response => response.json())
    .then(data => {
      const resultado = data.resultado;
      if(resultado){
        window.location.reload();
      }
    })
    .catch(error => console.error('Error al intentar dar like'))
    
  });
});