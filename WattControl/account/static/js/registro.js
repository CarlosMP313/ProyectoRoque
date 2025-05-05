function handleSocialSingIn(provider) {
    // Aquí puedes hacer lo que necesites dependiendo del proveedor de inicio de sesión
    alert('Has registrado sesión con ' + provider);
   }

  // toggle_password.js
  function togglePasswordVisibilityresgis() {
    var passwordInput1 = document.getElementById("password");
    var passwordInput2 = document.getElementById("password-confirm");
    var passwordToggle = document.querySelector(".password-toggle-confirm img");
  
    if (passwordInput1.type === "password" && passwordInput2.type === "password") {
      passwordInput1.type = "text";
      passwordInput2.type = "text";
      passwordToggle.src = "/static/imgs/eye.png"; // Cambia la imagen a un icono de ocultar contraseña
    } else {
      passwordInput1.type = "password";
      passwordInput2.type = "password";
      passwordToggle.src = "/static/imgs/eye-off.png"; // Cambia la imagen a un icono de mostrar contraseña
    }
  }