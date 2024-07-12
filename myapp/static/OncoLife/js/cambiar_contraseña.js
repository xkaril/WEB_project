document.getElementById("changePasswordForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    var currentPassword = document.getElementById("currentPassword").value;
    var newPassword = document.getElementById("newPassword").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    if (newPassword !== confirmPassword) {
        alert("Las contraseñas nuevas no coinciden.");
        return;
    }

    
    alert("¡Contraseña cambiada exitosamente!");
});
