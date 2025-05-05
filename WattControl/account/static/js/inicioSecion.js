console.log("Se cargo Inicio");
function handleSocialLogin(provider) {
    // Aquí puedes hacer lo que necesites dependiendo del proveedor de inicio de sesión
    alert('Has iniciado sesión con ' + provider);
   }

  // toggle_password.js
  function togglePasswordVisibilityInicio() {
    var passwordInput1 = document.getElementById("password");
    var passwordToggle = document.querySelector(".password-toggleLogon img");
  
    if (passwordInput1.type === "password") {
      passwordInput1.type = "text";
      passwordInput2.type = "text";
      passwordToggle.src = "/static/imgs/eye.png"; // Cambia la imagen a un icono de ocultar contraseña
    } else {
      passwordInput1.type = "password";
      passwordInput2.type = "password";
      passwordToggle.src = "/static/imgs/eye-off.png"; // Cambia la imagen a un icono de mostrar contraseña
    }
  }