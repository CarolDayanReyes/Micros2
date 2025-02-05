;------------------------------------------------------------
; Programa en ensamblador para calcular la magnitud al cuadrado 
; de un vector tridimensional.
;
; Recibe:
;   - Dirección de memoria inicial del vector (x, y, z) en R1.
;   - Dirección de memoria donde se almacenará el resultado en R2.
;
; Pasos:
; 1. Carga los valores del vector desde la memoria.
; 2. Calcula el cuadrado de cada componente.
; 3. Suma los cuadrados.
; 4. Guarda el resultado en la dirección especificada.
;
; Datos del vector:
; v = |  <d>  |
;     | <d+4> |
;     | <d+8> |
;
; | v^2 | = | x | ^2 = x^2 + y^2 + z^2
;           | y |
;           | z |
;------------------------------------------------------------

0x00   LD   R3, [R1 + 0]   ; Cargar x desde la dirección en R1
0x04    SMUL R4, R3, R3     ; R4 = x^2
0x08    LD   R3, [R1 + 4]   ; Cargar y desde la dirección en R1 + 4
0x0C    SMUL R5, R3, R3     ; R5 = y^2
0x10    LD   R3, [R1 + 8]   ; Cargar z desde la dirección en R1 + 8
0x14    SMUL R3, R3, R3     ; R3 = z^2
0x18    ADD  R3, R3, R4     ; R3 = z^2 + x^2
0x1C    ADD  R3, R3, R5     ; R3 = z^2 + x^2 + y^2
0x1C    ST   [R2 + 0], R3   ; Almacenar el resultado en la dirección de R2
