! ===============================
! Reservar memoria para datos
! ===============================
    .section ".bss"
pasos:       .word   0         ! Número de pasos totales
Kv:          .word   0         ! Factor de viscosidad
m:           .word   0         ! Masa del objeto
t:           .word   0         ! Intervalo de tiempo (delta t)
Pos_i:       .word   0, 0      ! Posición inicial (x, y)
V_i:         .word   0, 0      ! Velocidad inicial (Vx, Vy)
F:           .word   0, 0      ! Fuerza en cada dirección (Fx, Fy)
a:           .word   0, 0      ! Aceleración (ax, ay)
V:           .word   0, 0      ! Velocidad actual (Vx, Vy)
delta_pos:   .word   0, 0      ! Cambio en la posición (dx, dy)
pos_lista:   .skip   400       ! Memoria para almacenar posiciones (máx. 200 pasos)

! ===============================
! Código principal
! ===============================
    .section ".text"
    .global main

main:
    ! ===========================
    ! Inicialización
    ! ===========================
    LD   [%lo(V_i)], %o0        ! Cargar Vx inicial
    ST   %o0, [%lo(V)]          ! Guardar en V[0]
    LD   [%lo(V_i)+4], %o1      ! Cargar Vy inicial
    ST   %o1, [%lo(V)+4]        ! Guardar en V[1]

    LD   [%lo(Pos_i)], %o2      ! Cargar Pos_x inicial
    ST   %o2, [%lo(pos_lista)]  ! Guardar en lista[0]
    LD   [%lo(Pos_i)+4], %o3    ! Cargar Pos_y inicial
    ST   %o3, [%lo(pos_lista)+4]! Guardar en lista[1]

    LD   [%lo(pasos)], %o4      ! Cargar número total de pasos
    LD   [%lo(t)], %o5          ! Cargar delta t
    SETHI %hi(0), %l0           ! Inicializar contador de pasos en 0
    SETHI %hi(pos_lista), %l1   ! Dirección base de la lista de posiciones

loop_pasos:
    CMP   %l0, %o4              ! Comparar contador con número de pasos
    BGE   end                   ! Si contador >= pasos, terminar
    NOP

    ! ===========================
    ! Calcular la fuerza: F = -Kv * V
    ! ===========================
    LD    [%lo(Kv)], %o6        ! Cargar Kv
    LD    [%lo(V)], %o7         ! Cargar Vx
    SMUL  %o6, %o7, %o8         ! Fx = Kv * Vx
    NEG   %o8                   ! Fx = -Fx
    ST    %o8, [%lo(F)]         ! Guardar en F[0]

    LD    [%lo(V)+4], %o7       ! Cargar Vy
    SMUL  %o6, %o7, %o8         ! Fy = Kv * Vy
    NEG   %o8                   ! Fy = -Fy
    ST    %o8, [%lo(F)+4]       ! Guardar en F[1]

    ! ===========================
    ! Calcular aceleración: a = F / m
    ! ===========================
    LD    [%lo(m)], %o9         ! Cargar m
    LD    [%lo(F)], %o10        ! Cargar Fx
    SDIV  %o10, %o9, %o11       ! ax = Fx / m
    ST    %o11, [%lo(a)]        ! Guardar en a[0]

    LD    [%lo(F)+4], %o10      ! Cargar Fy
    SDIV  %o10, %o9, %o11       ! ay = Fy / m
    ST    %o11, [%lo(a)+4]      ! Guardar en a[1]

    ! ===========================
    ! Actualizar velocidad: V = V + a * t
    ! ===========================
    LD    [%lo(a)], %o12        ! ax
    SMUL  %o12, %o5, %o12       ! ax * t
    LD    [%lo(V)], %o13        ! Vx actual
    ADD   %o13, %o12, %o13      ! Vx = Vx + ax * t
    ST    %o13, [%lo(V)]        ! Guardar nuevo Vx

    LD    [%lo(a)+4], %o12      ! ay
    SMUL  %o12, %o5, %o12       ! ay * t
    LD    [%lo(V)+4], %o13      ! Vy actual
    ADD   %o13, %o12, %o13      ! Vy = Vy + ay * t
    ST    %o13, [%lo(V)+4]      ! Guardar nuevo Vy

    ! ===========================
    ! Calcular desplazamiento: delta_pos = V * t
    ! ===========================
    SMUL  %o5, %o5, %o14       ! t*t
    LD    [%lo(delta_pos)], %o12 ! Cargar a_x en %o12
    SMUL  %o12, %o14, %o14     ! t*t*a
    LD    [%lo(V)], %o15       ! Cargar Vx
    SMUL  %o15, %o5, %o18      ! dx = Vx * t
    ADD   %o18, %014, %o14     
    SRL   %o14, %o14, 1        ! /2
    ST    %o14, [%lo(delta_pos)] ! Guardar dx

    SMUL  %o5, %o5, %o14       ! t*t
    LD    [%lo(delta_pos)+4], %o12 ! Cargar a_y en %o12
    SMUL  %o12, %o14, %o14     ! t*t*a
    LD    [%lo(V)+4], %o15       ! Cargar Vy
    SMUL  %o15, %o5, %o18      ! dx = Vy * t
    ADD   %o18, %014, %o14     
    SRL   %o14, %o14, 1        ! /2
    ST    %o14, [%lo(delta_pos)+4] ! Guardar dy

    ! ===========================
    ! Actualizar posición: Pos = Pos + delta_pos
    ! ===========================
    LD    [%l1], %o16          ! Cargar Pos_x actual
    ADD   %o16, %o14, %o16     ! Pos_x = Pos_x + dx
    ST    %o16, [%l1+8]        ! Guardar en lista siguiente posición X
    LD    [%l1+4], %o17        ! Cargar Pos_y actual
    ADD   %o17, %o15, %o17     ! Pos_y = Pos_y + dy
    ST    %o17, [%l1+12]       ! Guardar en lista siguiente posición Y

    ADD   %l1, 8, %l1           ! Avanzar en la lista
    INC   %l0                   ! Incrementar contador
    BA    loop_pasos            ! Repetir el bucle
    NOP

end:
    RET
    NOP
