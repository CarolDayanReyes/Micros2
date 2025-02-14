section ".data"
pi:         .double 3.141592653589793
k:          .word 256
x:          .word 64    ! x = k/4
x_squared:  .word 0
k_squared:  .word 0
numerator:  .word 0
numerator_init: .word 256
acc_i1:     .word 0
acc_i2:     .word 0
terms:      .word 10
neg_two_pi_squared: .double -39.47841760435743

.section ".text"
.global _start
_start:
    set k, %l0             ! Load k
    st %l0, numerator      ! Initial numerator
    st %l0, acc_i1         ! Initial acc_i1
    st %l0, acc_i2         ! Initial acc_i2

    ld [x], %l1            ! Load x
    smul %l1, %l1, %l2      ! x^2
    st %l2, x_squared

    mul %l0, %l0, %l3      ! k^2
    st %l3, k_squared

    mov 1, %l4             ! Denominator
    mov 1, %l5             ! n = 1

loop:
    ld [numerator], %l6
    ld [x_squared], %l7
    flags neg_two_pi_squared, %f0
    smul %f0, %l7, %f1    ! (-x^2 * (2π)^2)
    st %f1, %l7
    smul %l6, %l7, %l6      ! Numerator *= (-x^2 * (2π)^2)
    st %l6, numerator

    smul %l5, 2, %l8
    sub %l8, 1, %l9
    ld [k_squared], %l10
    smul %l4, %l8, %l4      ! Denominator *= (2n)
    smul %l4, %l9, %l4      ! Denominator *= (2n-1)
    smul %l4, %l10, %l4     ! Denominator *= k^2

    ! term_i1 = numerator // denominator
    ! acc_i1 += term_i1
    ! term_i2 = term_i2 * (-x^2 * (2π)^2) // ((2n)(2n-1) * k^2)
    ! acc_i2 += term_i2

    add %l5, 1, %l5        ! n++
    ld [terms], %l11
    cmp %l5, %l11
    ble loop

    mov 1, %g1             ! Exit
    NOP 0