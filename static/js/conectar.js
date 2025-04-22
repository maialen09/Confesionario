const socket = io();    
socket.on('usuarios_conectados', function(listaUsuarios) {
    const lista = document.getElementById("lista-usuarios");
    lista.innerHTML = ""; 

    listaUsuarios.forEach(function(user) {
        const li = document.createElement("li");
        li.textContent = user;
        lista.appendChild(li);
    });
});