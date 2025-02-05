    .data
vl_list: .word 10, 12, 15, 14, 10   @ Lista de velocidades de la rueda izquierda
vr_list: .word 12, 14, 16, 15, 11   @ Lista de velocidades de la rueda derecha
num_steps: .word 5                  @ Número de pasos en la simulación
d: .word 2                           @ Distancia entre ruedas
x: .word 0                           @ Posición X inicial
y: .word 0                           @ Posición Y inicial
theta: .word 0                       @ Ángulo inicial

    .text
    .globl _start
_start:
    ldr r4, =num_steps
    ldr r4, [r4]          @ Cargar número de iteraciones en r4
    ldr r5, =vl_list      @ Cargar dirección de la lista de velocidades izquierda
    ldr r6, =vr_list      @ Cargar dirección de la lista de velocidades derecha
    ldr r7, =d            @ Cargar distancia entre ruedas
    ldr r7, [r7]          @ Valor de d en r7

loop:
    cmp r4, #0            @ Comprobar si quedan elementos
    BEQ end_loop          @ Si r4 == 0, salir del loop
    
    ldr r0, [r5], #4      @ Cargar velocidad izquierda y avanzar puntero
    ldr r1, [r6], #4      @ Cargar velocidad derecha y avanzar puntero

    add r2, r0, r1        @ Vc = (Vr + Vl)
    asr r2, r2, #1        @ Dividir por 2 -> Vc = (Vr + Vl) / 2

    sub r3, r1, r0        @ Vr - Vl
    asr r3, r3, #1        @ Dividir por 2
    mul r3, r3, r7        @ Multiplicar por d -> α' = (Vr - Vl) * (2d)

    ldr r8, =theta        @ Obtener dirección de theta
    ldr r9, [r8]          @ Cargar theta
    add r9, r9, r3        @ theta += α'
    str r9, [r8]          @ Guardar nuevo theta

    ldr r8, =x            @ Obtener dirección de X
    ldr r9, [r8]          @ Cargar X
    add r9, r9, r2        @ x += Vc (simplificación sin trigonometría)
    str r9, [r8]          @ Guardar nuevo X

    ldr r8, =y            @ Obtener dirección de Y
    ldr r9, [r8]          @ Cargar Y
    add r9, r9, r2        @ y += Vc (simplificación sin trigonometría)
    str r9, [r8]          @ Guardar nuevo Y

    subs r4, r4, #1       @ Decrementar contador
    B loop                @ Repetir el ciclo

end_loop:
    @ Terminar el programa
    MOV r7, #1
    MOV r0, #0
    SWI 0
