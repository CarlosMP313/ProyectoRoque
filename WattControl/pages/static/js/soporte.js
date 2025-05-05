document.addEventListener('DOMContentLoaded', function() {
    // Agregar evento para filtrar productos al escribir en el campo de búsqueda
    document.getElementById("querySoport").addEventListener("input", filtrarProductosSoporte);
  });


function filtrarProductosSoporte() {
    var input, filter, ul, li, h2, i, txtValue;
    input = document.getElementById("querySoport");
    filter = input.value.toUpperCase();
    ul = document.querySelector(".listaProductos");
    li = ul.querySelectorAll("li");
    for (i = 0; i < li.length; i++) {
        h2 = li[i].querySelector("h2");
        txtValue = h2.textContent || h2.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
  }
  console.log("Se cargo");