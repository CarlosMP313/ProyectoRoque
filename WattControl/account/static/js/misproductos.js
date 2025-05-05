document.addEventListener('DOMContentLoaded', function() {
  // Agregar evento para filtrar productos al escribir en el campo de búsqueda
  document.getElementById("querySoportproductosBus").addEventListener("input", filtrarProductos);

  // Obtener referencia al formulario de agregar producto
  const formularioAgregarProducto = document.getElementById("formularioAgregarProducto");

  // Obtener todos los elementos de producto y agregar el evento de clic
  const productos = document.querySelectorAll('.itemProductoBusque');
  const productosP = document.querySelectorAll('.itemProducto');

  productosP.forEach(productoA => {
      const infoAdicional = productoA.querySelector('.detallesProducto');

      productoA.addEventListener('mouseenter', function() {
          infoAdicional.style.display = 'block';
      });

      productoA.addEventListener('mouseleave', function() {
          infoAdicional.style.display = 'none';
      });
  });


  
  productos.forEach(producto => {
      producto.addEventListener('click', function() {
          // Ocultar el contenido del modal
         
          var modal = document.getElementById("modal");
          var modal2 = document.getElementById("model-dos");
          modal.style.display = "none";
          modal2.style.display = "block";
          

          // Mostrar el formulario de agregar producto
          formularioAgregarProducto.style.display = "block";
          const productoId = producto.getAttribute('data-producto-id');
            document.getElementById('productoIda').value = productoId; // Establecer el ID del producto en el campo oculto del formulario
      });
  });
});

function abrirModal() {
  var modal = document.getElementById("modal");
  modal.style.display = "block";
}

function cerrarModal() {
  var modal = document.getElementById("modal");
  modal.style.display = "none";
  document.getElementById("querySoportproductosBus").value = "";
}
function cerrarModal2() {
  var modal = document.getElementById("model-dos");
  modal.style.display = "none";
  document.getElementById("querySoportproductosBus").value = "";
}

window.onclick = function(event) {
  var modal = document.getElementById("modal");
  if (event.target == modal) {
      modal.style.display = "none";
  }
  document.getElementById("querySoportproductosBus").value = "";
}

// Función para filtrar productos al escribir en el campo de búsqueda
function filtrarProductos() {
  var input, filter, ul, li, h2, i, txtValue;
  input = document.getElementById("querySoportproductosBus");
  filter = input.value.toUpperCase();
  ul = document.querySelector(".listaProductosBusque");
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

console.log("Se cargo ");