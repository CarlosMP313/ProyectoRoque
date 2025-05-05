
function toggleSidebarL() {
    var sidebarLL = document.getElementById("sidebarLL");
    var overlay = document.getElementById("overlay");

    if (sidebarLL.style.width === "300px" ) {
        sidebarLL.style.width = "0";
        overlay.style.display = "none"; // Oculta el overlay al cerrar la barra lateral
    } else {
        sidebarLL.style.width = "300px";
        overlay.style.display = "block"; // Muestra el overlay al abrir la barra lateral
   
        // content.style.marginRight = "300px";
    }
}

function closeSidebarL() {
    var sidebarLL = document.getElementById("sidebarLL");
    var overlay = document.getElementById("overlay");
    overlay.style.display = "none";
    sidebarLL.style.width = "0";
   
}

