function toggleSidebarLogin() {
    var sidebarLogin = document.getElementById("sidebarLogin");
    var overlay = document.getElementById("overlay");

    if (sidebarLogin.style.width === "300px" ) {
        sidebarLogin.style.width = "0";
        overlay.style.display = "none"; // Oculta el overlay al cerrar la barra lateral
   
    } else {
        sidebarLogin.style.width = "300px";
        overlay.style.display = "block"; // Muestra el overlay al abrir la barra lateral
  
        // content.style.marginRight = "300px";
    }
}
function closeSidebarLogin() {
    var sidebarLogin = document.getElementById("sidebarLogin");
    var sidebarLogin = document.getElementById("sidebarLogin");
    var overlay = document.getElementById("overlay");
    sidebarLogin.style.width = "0";
    overlay.style.display = "none"; // Oculta el overlay al cerrar la barra lateral

   
}
