/*
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control Tipo Xbox</title>
    <style>
        body { 
            margin: 0; 
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: #ffffff;
            height: 100vh;
        }
        .car-container {
            position: relative;
            width: 200px;
            height: 120px;
            margin-bottom: 20px;
        }
        .car {
            width: 250%;
            height: auto;
            position: relative;
            left: -4.5cm; 
        }
        .wheel {
            position: absolute;
            width: 88px;
            height: 88px;
            background-color: #333;
            border-radius: 50%;
            border: 4px solid #000;
            top: 185px;
            transform-origin: center;
            background-image: linear-gradient(to right, transparent 50%, #fff 50%);
            background-size: 100% 20px;
            transition: transform 0.3s linear;
        }
        .wheel.left {
            right: 85%;
        }
        .wheel.right {
            left: 75%;
        }
        .control-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            width: 700px;
            height: 400px;
            background: url('control.png') no-repeat center center;
            background-size: contain;
            position: relative;
            margin-top: 3cm;
        }
        .action-buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            padding: 10px;
            position: absolute;
            left: 80px; 
            top: 80px; 
        }
        .action-buttons .row {
            display: flex;
            gap: 5px;
        }
        .control-title {
            background-color: #9b59b6;
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-size: 20px;
            text-align: center;
            position: absolute;
            left: 280px; 
            top: 150px; 
        }
        .speed-control {
            display: flex;
            align-items: center;
            gap: 5px;
            position: absolute;
            left: 435px; 
            top: 142px; 
        }
        button {
            width: 50px;
            height: 50px;
            font-size: 14px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px #0056b3, 0 -2px #0056b3 inset;
            transition: all 0.2s ease;
        }
        button:active {
            background-color: #0056b3;
            box-shadow: 0 2px #003d7a, 0 -1px #003d7a inset;
        }
        .speed-control button {
            width: 53px;
            height: 53px;
            font-size: 16px;
            background-color: #28a745;
            color: white;
            border-radius: 50%;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px #1e7e34, 0 -2px #1e7e34 inset;
            transition: all 0.2s ease;
        }
        .speed-control button:active {
            background-color: #1e7e34;
            box-shadow: 0 2px #1e7e34, 0 -1px #1e7e34 inset;
        }
        .speed-label {
            font-size: 16px;
            color: #fff;
        }
        .speed-display {
            font-size: 20px;
            color: #fff;
            width: 50px;
            text-align: center;
        }
        .stop-button {
            background-color: #007bff;
            box-shadow: 0 4px #0056b3, 0 -2px #0056b3 inset;
            position: absolute;
            top: 110px; 
            left: 65px; 
        }
        .stop-button:active {
            background-color: #0056b3;
            box-shadow: 0 2px #003d7a, 0 -1px #003d7a inset;
        }
        .right-button {
            position: absolute;
            left: 120px; 
            top: 64px;
        }
        .up-button {
            position: absolute;
            left: 65px; 
            top: 20px;
        }
        .left-button {
            position: absolute;
            left: 10px; 
            top: 64px;
        }

        @keyframes rotate-left {
            from { transform: rotate(0deg); }
            to { transform: rotate(-360deg); }
        }
    </style>
</head>
<body>
    <div class="car-container">
        <img src="https://img.freepik.com/vector-gratis/etiqueta-engomada-historieta-coche-compacto-sobre-fondo-blanco_1308-76736.jpg" alt="Carro" class="car">
        <div class="wheel left" id="leftWheel"></div>
        <div class="wheel right" id="rightWheel"></div>
    </div>
    <div class="control-label">Control del Carro</div>
    <div id="arm"></div>
    <div class="control-container">
        <div class="action-buttons">
            <div class="row">
                <div></div>
                <button class="up-button" onclick="sendCommand('forward')">↑</button>
                <div></div>
            </div>
            <div class="row">
                <button class="left-button" onclick="sendCommand('left')">←</button>
                <button class="stop-button" onclick="sendCommand('stop')">⏹</button>
                <button class="right-button" onclick="sendCommand('right')">→</button>
            </div>
        </div>
        <div class="control-title">CONTROL</div>
        <div class="speed-control">
            <button onclick="adjustSpeed('down')">−</button>
            <span class="speed-display" id="speedValue">0</span>
            <button onclick="adjustSpeed('up')">+</button>
        </div>
    </div>
    <script>
*/
        let speed = 0;
        const speedIncrement = 1;
        const maxSpeed = 10;

        function sendCommand(command) {
            if (command === 'stop') {
                speed = 0;
                document.getElementById('speedValue').innerText = speed;
                updateWheelRotation();
            } else {
                fetch(`/command?cmd=${command}`)
                .then(response => response.text())
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
            }
        }

        function adjustSpeed(direction) {
            if (direction === 'up') {
                speed = Math.min(speed + speedIncrement, maxSpeed);
            } else if (direction === 'down') {
                speed = Math.max(speed - speedIncrement, 0);
            }
            document.getElementById('speedValue').innerText = speed;
            updateWheelRotation();
            fetch(`/speed?adjust=${direction}&value=${speed}`)
            .then(response => response.text())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
        }

        function updateWheelRotation() {
            const maxDuration = 0.3;
            const minDuration = 2.6;
            const duration = minDuration - (speed / maxSpeed * (minDuration - maxDuration));

            const leftWheel = document.getElementById('leftWheel');
            const rightWheel = document.getElementById('rightWheel');

            if (speed > 0) {
                leftWheel.style.animation = `rotate-left ${duration}s linear infinite`;
                rightWheel.style.animation = `rotate-left ${duration}s linear infinite`;
            } else {
                leftWheel.style.animation = 'none';
                rightWheel.style.animation = 'none';
            }
        }
        
/*
    </script>
</body>
</html>

*/
