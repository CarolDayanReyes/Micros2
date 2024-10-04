import time
import board
import busio
import adafruit_ssd1306
import socketpool
import wifi
import pwmio


# Conectar a la red WiFi
wifi.radio.connect("Juanes", "juanes123")
pool = socketpool.SocketPool(wifi.radio)
led = pwmio.PWMOut(board.GP14, frequency=5000, duty_cycle=0)
led1 = pwmio.PWMOut(board.GP15, frequency=5000, duty_cycle=0)

# Obtener la dirección IP como un objeto Addressa
ip_address = wifi.radio.ipv4_address
print("wifi.radio", wifi.radio.hostname, ip_address)

# Convertir la dirección IP en una lista de números, separando en unidades
ip_string = str(ip_address)  # Convertir el objeto Address a string
ip_list = []
x_string = "X=1.23"
x_list=[]
y_string = "Y=1.42"
y_list=[]

for digit in ip_string:
    if digit.isdigit():  # Verificar si el carácter es un dígito
        ip_list.append(int(digit))

print("IP:", ip_list)

for char in x_string:
    if char.isdigit():  # Verificar si es un dígito
        x_list.append(char)
    elif char == '.':  # Verificar si es el punto decimal
        x_list.append('.')
    elif char == '=':  # Verificar si es el punto decimal
        x_list.append('=')
    elif char == 'X':  # Verificar si es el punto decimal
        x_list.append('X')
print("X:", x_list)

for char in y_string:
    if char.isdigit():
        y_list.append(char)
    elif char == '.':
        y_list.append('.')
    elif char == '=':  # Verificar si es el punto decimal
        y_list.append('=')
    elif char == 'Y':  # Verificar si es el punto decimal
        y_list.append('Y')
        
print("Y:", y_list)

s = pool.socket()
s.bind(('', 80))
s.listen(5)
# Inicializar I2C
i2c = busio.I2C(board.GP5, board.GP4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Limpiar la pantalla
display.fill(0)
display.show()

# Definir patrones para números del 0 al 9
numbers = {
    '0': [
        "  *****  ",
        " **   ** ",
        " **   ** ",
        " **   ** ",
        " **   ** ",
        " **   ** ",
        "  *****  "
    ],
    '1': [
        "    **   ",
        "   **    ",
        "    **   ",
        "    **   ",
        "    **   ",
        "    **   ",
        "  ****** "
    ],
    '2': [
        "  *****  ",
        " **   ** ",
        "     **  ",
        "    **   ",
        "   **    ",
        " **      ",
        " ******** "
    ],
    '3': [
        "  *****  ",
        " **   ** ",
        "     **  ",
        "    **   ",
        "     **  ",
        " **   ** ",
        "  *****  "
    ],
    '4': [
        " **   ** ",
        " **   ** ",
        " **   ** ",
        "  ****** ",
        "     **  ",
        "     **  ",
        "     **  "
    ],
    '5': [
        " ******** ",
        " **      ",
        " **      ",
        "  ******  ",
        "     **   ",
        " **   **  ",
        "  *****   "
    ],
    '6': [
        "   *****  ",
        "  **      ",
        " **       ",
        " **  **** ",
        " **   **  ",
        "  **  **  ",
        "   ****   "
    ],
    '7': [
        " ********* ",
        "      **   ",
        "     **    ",
        "    **     ",
        "   **      ",
        "  **       ",
        " **        "
    ],
    '8': [
        "   *****  ",
        "  **   ** ",
        "  **   ** ",
        "   *****  ",
        "  **   ** ",
        "  **   ** ",
        "   *****  "
    ],
    '9': [
        "   *****  ",
        "  **   ** ",
        "  **   ** ",
        "   ****** ",
        "      **  ",
        "     **   ",
        "   *****   "
    ]
}
# Definir coordenadas
coordinates = {
    '0': [
        "  *****  ",
        " **   ** ",
        " **   ** ",
        " **   ** ",
        " **   ** ",
        " **   ** ",
        "  *****  "
    ],
    '1': [
        "    **   ",
        "   **    ",
        "    **   ",
        "    **   ",
        "    **   ",
        "    **   ",
        "  ****** "
    ],
    '2': [
        "  *****  ",
        " **   ** ",
        "     **  ",
        "    **   ",
        "   **    ",
        " **      ",
        " ******** "
    ],
    '3': [
        "  *****  ",
        " **   ** ",
        "     **  ",
        "    **   ",
        "     **  ",
        " **   ** ",
        "  *****  "
    ],
    '4': [
        " **   ** ",
        " **   ** ",
        " **   ** ",
        "  ****** ",
        "     **  ",
        "     **  ",
        "     **  "
    ],
    '5': [
        " ******** ",
        " **      ",
        " **      ",
        "  ******  ",
        "     **   ",
        " **   **  ",
        "  *****   "
    ],
    '6': [
        "   *****  ",
        "  **      ",
        " **       ",
        " **  **** ",
        " **   **  ",
        "  **  **  ",
        "   ****   "
    ],
    '7': [
        " ********* ",
        "      **   ",
        "     **    ",
        "    **     ",
        "   **      ",
        "  **       ",
        " **        "
    ],
    '8': [
        "   *****  ",
        "  **   ** ",
        "  **   ** ",
        "   *****  ",
        "  **   ** ",
        "  **   ** ",
        "   *****  "
    ],
    '9': [
        "   *****  ",
        "  **   ** ",
        "  **   ** ",
        "   ****** ",
        "      **  ",
        "     **   ",
        "   *****  "
    ],
    'X': [
        "***    ***",
        " ***  *** ",
        "  ******  ",
        "   ****   ",
        "  ******  ",
        " ***  *** ",
        "***    ***"
    ],
    'Y': [
        "***    ***",
        " ***  *** ",
        "  ******  ",
        "   ****   ",
        "   ****   ",
        "   ****   ",
        "   ****   "
    ],
    '=': [
        "          ",
        " ******** ",
        " ******** ",
        "          ",
        " ******** ",
        " ******** ",
        "          "
    ],
    '.': [
        "          ",
        "          ",
        "          ",
        "          ",
        "          ",
        "     **   ",
        "     **   "
    ]
}
def display_selected_numbers(selected_numbers):
    # Limpiar la pantalla
    display.fill(0)

    # Mostrar los números seleccionados
    x_offset = 0  # Desplazamiento horizontal inicial
    for num in selected_numbers:
        if str(num) in numbers:  # Verificar si el número está en el diccionario
            pattern = numbers[str(num)]
            
            # Dibujar el patrón de cada número en la pantalla
            for row in range(len(pattern)):
                for col in range(len(pattern[row])):
                    if pattern[row][col] == '*':
                        display.pixel(x_offset + col, row + 5, 1)  # Ajustar la posición según sea necesario
            
            x_offset += 11  # Incrementar el desplazamiento para el siguiente número
            
    display.show()

display_selected_numbers(ip_list)
display.show()

def display_selected_coordinates(selected_coordinates):

    # Mostrar los números seleccionados
    x_offset = 0  # Desplazamiento horizontal inicial
    
    for char in selected_coordinates:
        if str(char)in coordinates:  # Verificar si el número está en el diccionario
            pattern = coordinates[str(char)]
            
            # Dibujar el patrón de cada número en la pantalla
            for row in range(len(pattern)):
                for col in range(len(pattern[row])):
                    if pattern[row][col] == '*':
                        display.pixel(x_offset + col, row + 22, 2)  # Ajustar la posición según sea necesario
            
            x_offset += 11  # Incrementar el desplazamiento para el siguiente número
            
    display.show()

display_selected_coordinates(x_list)

display.show()

def display_selected_coordinates(selected_coordinates):

    # Mostrar los números seleccionados
    x_offset = 65  # Desplazamiento horizontal inicial
    
    for char in selected_coordinates:
        if str(char)in coordinates:  # Verificar si el número está en el diccionario
            pattern = coordinates[str(char)]
            
            # Dibujar el patrón de cada número en la pantalla
            for row in range(len(pattern)):
                for col in range(len(pattern[row])):
                    if pattern[row][col] == '*':
                        display.pixel(x_offset + col, row + 22, 2)  # Ajustar la posición según sea necesario
            
            x_offset += 11  # Incrementar el desplazamiento para el siguiente número
            
    display.show()

display_selected_coordinates(y_list)


display.show()



contador_valor = 40  # Variable para almacenar el valor del contador
direct_valor = 0

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    buffer = bytearray(1024)  # Crear un buffer mutable
    bytes_received, address = conn.recvfrom_into(buffer)  # Recibir datos en el buffer y obtener la dirección del remitente
    print("Received from:", address)
    request = buffer[:bytes_received].decode('utf-8')
    print("Request:", request)

    # Procesar la solicitud GET para obtener el valor del contador
    if "GET /?contador=" in request:
        contador_str = request.split("GET /?contador=")[1].split(" ")[0]
        try:
            contador_valor = int(contador_str)
        except ValueError:
            contador_valor = 0  # Valor predeterminado si no se puede convertir
    print (contador_valor)
    
    if "GET /?direct=" in request:
        direct_str = request.split("GET /?direct=")[1].split(" ")[0]
        try:
            direct_valor = int(direct_str)
        except ValueError:
            direct_valor = 0  # Valor predeterminado si no se puede convertir
    print (direct_valor)
    
    if direct_valor == 1:
    
        led.duty_cycle = int(65535 *((contador_valor*0.99)/100))# Down
        time.sleep(0.01)
        led1.duty_cycle = int(65535 *(contador_valor/100))# Down
        time.sleep(0.01)
        
    elif direct_valor == 0:
        
        led.duty_cycle = int(65535 *(0))# Down
        time.sleep(0.01)
        led1.duty_cycle = int(65535 *(0))# Down
        time.sleep(0.01)
        
    elif direct_valor == 2:
        
        led.duty_cycle = int(65535 *((contador_valor*0.8)/100))# Down
        time.sleep(0.01)
        led1.duty_cycle = int(65535 *(contador_valor/100))# Down
        time.sleep(0.01)
        
    elif direct_valor == 3:
        
        led1.duty_cycle = int(65535 *((contador_valor*0.8)/100))# Down
        time.sleep(0.01)
        led.duty_cycle = int(65535 *(contador_valor/100))# Down
        time.sleep(0.01)     
    
    # Respuesta HTML
    response = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <title>Ejemplo de JavaScript</title>
        <meta charset="UTF-8">
    </head>

    <body>

        <form>
            <input type="button" onClick="incrementar()" value="+">
            <input type="button" onClick="decrementar()" value="-">
            <p>Velocidad:<input type="text" id="text1" value="{contador_valor}"></p>
            <input type="button" onClick="avanzar()" value="⬆">
            <input type="button" onClick="izquierda()" value="⬅">
            <input type="button" onClick="parar()" value="⏹️">
            <input type="button" onClick="derecha()" value="➡">
        </form>

        <script>
            let contador = {contador_valor};

            function enviarContador(valor) {{
                fetch('/?contador=' + valor)
                .then(response => response.text())
                .then(data => console.log("Valor enviado:", valor));
            }}
            
            let direct = {direct_valor};

            function enviarDirect(valor) {{
                fetch('/?direct=' + valor)
                .then(response => response.text())
                .then(data => console.log("Valor enviado:", valor));
            }}
            
            function incrementar() {{
                contador+=10;
                if (contador >= 0 && contador < 100) {{
                    document.getElementById('text1').value = contador;
                }} else if (contador >= 100) {{
                    document.getElementById('text1').value = 'Max';
                    contador = 100;
                }}
                enviarContador(contador);
            }}

            function decrementar() {{
                contador-=10;
                if (contador >= 0 && contador < 100) {{
                    document.getElementById('text1').value = contador;
                }} else {{
                    document.getElementById('text1').value = 0;
                    contador = 0;
                }}
                enviarContador(contador);
            }}
            function avanzar() {{
                direct=1;
                enviarDirect(direct);
                enviarContador(contador);
            }}
            function parar() {{
                direct=0;
                enviarDirect(direct);
                enviarContador(contador);
            }}
            function izquierda() {{
                direct=2;
                enviarDirect(direct);
                enviarContador(contador);
            }}
            function derecha() {{
                direct=3;
                enviarDirect(direct);
                enviarContador(contador);
            }}

        </script>

    </body>

    </html>
    """
    conn.send(response)
    conn.close()