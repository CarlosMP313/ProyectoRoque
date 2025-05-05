
function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var overlayIn = document.getElementById("overlayin");


    if (sidebar.style.width === "300px") {
        sidebar.style.width = "0";
        overlayIn.style.display = "none"; // Oculta el overlay al cerrar la barra lateral
    } else {
        sidebar.style.width = "300px";
        overlayIn.style.display = "block"; // Muestra el overlay al abrir la barra lateral
    }
}

function closeSidebar() {
    var sidebar = document.getElementById("sidebar");
    var overlayIn = document.getElementById("overlayin");
    sidebar.style.width = "0";
    overlayIn.style.display = "none";
}
