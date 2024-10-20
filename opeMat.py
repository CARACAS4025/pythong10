<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cajero Automático Simulado</title>
    <style>
        body {
            font-family: Arial, sans-serif
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .atm {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }
        .hidden {
            display: none;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            margin: 5px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        input {
            padding: 10px;
            margin: 5px 0;
            width: 90%;
            box-sizing: border-box;
        }
        #message {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="atm">
        <h2>Cajero Automático</h2>
        <div id="loginSection">
            <h3>Iniciar Sesión</h3>
            <label for="username">Usuario:</label>
            <input type="text" id="username" placeholder="Ingrese su nombre">
            <label for="pin">PIN:</label>
            <input type="password" id="pin" placeholder="Ingrese su PIN">
            <button onclick="login()">Ingresar</button>
        </div>
        
        <div id="operationSection" class="hidden">
            <h3>Bienvenido, <span id="userDisplay"></span></h3>
            <button onclick="consultarSaldo()">Consultar Saldo</button>
            <button onclick="retirar()">Retirar</button>
            <button onclick="consignar()">Consignar</button>
            <button onclick="imprimirSaldo()">Imprimir Saldo</button>
            <button onclick="salir()">Salir</button>
            <div id="message"></div>
        </div>
    </div>

    <script>
        // Simulación de datos de usuarios
        const usuarios = {
            "Andres": { pin: "1234", saldo: 6000 },
            "Suban": { pin: "1234", saldo: 8000 },
            "Juan": { pin: "1234", saldo: 5000 },
            "Maria": { pin: "1234", saldo: 10000 }
        };

        let usuarioActual = null;

        // Función de inicio de sesión
        function login() {
            const username = document.getElementById('username').value;
            const pin = document.getElementById('pin').value;
            
            if (usuarios[username] && usuarios[username].pin === pin) {
                usuarioActual = usuarios[username];
                document.getElementById('userDisplay').innerText = username;
                document.getElementById('loginSection').classList.add('hidden');
                document.getElementById('operationSection').classList.remove('hidden');
                document.getElementById('message').innerText = '';
            } else {
                alert("Usuario o PIN incorrecto");
            }
        }

        // Función para consultar saldo
        function consultarSaldo() {
            document.getElementById('message').innerText = Su saldo actual es: $${usuarioActual.saldo};
        }

        // Función para retirar dinero
        function retirar() {
            const monto = prompt("Ingrese el monto a retirar:");
            if (monto && !isNaN(monto) && monto > 0) {
                if (usuarioActual.saldo >= monto) {
                    usuarioActual.saldo -= parseFloat(monto);
                    document.getElementById('message').innerText = Retiro exitoso. Su saldo actual es: $${usuarioActual.saldo};
                } else {
                    document.getElementById('message').innerText = "Saldo insuficiente.";
                }
            } else {
                document.getElementById('message').innerText = "Monto inválido.";
            }
        }

        // Función para consignar dinero
        function consignar() {
            const monto = prompt("Ingrese el monto a consignar:");
            if (monto && !isNaN(monto) && monto > 0) {
                usuarioActual.saldo += parseFloat(monto);
                document.getElementById('message').innerText = Consignación exitosa. Su saldo actual es: $${usuarioActual.saldo};
            } else {
                document.getElementById('message').innerText = "Monto inválido.";
            }
        }

        // Función para imprimir saldo
        function imprimirSaldo() {
            document.getElementById('message').innerText = Saldo impreso: $${usuarioActual.saldo};
        }

        // Función para salir
        function salir() {
            alert("Gracias por usar el cajero automático. ¡Hasta luego!");
            document.getElementById('operationSection').classList.add('hidden');
            document.getElementById('loginSection').classList.remove('hidden');
            document.getElementById('username').value = '';
            document.getElementById('pin').value = '';
            document.getElementById('message').innerText = '';
            usuarioActual = null;
        }
    </script>
</body>
</html>
