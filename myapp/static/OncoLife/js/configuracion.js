        function openChangePasswordWindow() {
            window.open("cambiar_contraseña.html", "_blank", "width=500, height=400");
        }

        function openNotificationSettings() {
            window.open("notificaciones.html", "_blank", "width=500, height=400");
        }

        function openPrivacySettings() {
            window.open("privacidad.html", "_blank", "width=500, height=400");
        }

        function openChangeUsernameWindow() {
            window.open("cambiar_nombre_usuario.html", "_blank", "width=500, height=400");
        }

        document.getElementById('applyBtn').addEventListener('click', () => {
            const fontSize = document.getElementById('fontSize').value;
            document.body.style.fontSize = fontSize === 'small' ? '12px' : fontSize === 'medium' ? '16px' : '20px';
        });