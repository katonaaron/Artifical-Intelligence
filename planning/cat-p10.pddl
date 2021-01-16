(define (problem cat-p10)
    (:domain cat)
    (:objects
        c - cat
        m1 m2 m3 m4 m5 m6 - mouse
        w1 w2 w3 w4 w5 - wall
        t1 t2 t3 t4 t5 t6 - trap
        s11 s12 s13 s14 s15 s16
        s21 s22 s23 s24 s25 s26
        s31 s32 s33 s34 s35 s36
        s41 s42 s43 s44 s45 s46
        s51 s52 s53 s54 s55 s56
        s61 s62 s63 s64 s65 s66
        - square
    )

    (:init
        ; square adjacency
        (adj s11 s12) (adj s12 s11)
        (adj s11 s21) (adj s21 s11)
        (adj s12 s13) (adj s13 s12)
        (adj s12 s22) (adj s22 s12)
        (adj s13 s14) (adj s14 s13)
        (adj s13 s23) (adj s23 s13)
        (adj s14 s15) (adj s15 s14)
        (adj s14 s24) (adj s24 s14)
        (adj s15 s16) (adj s16 s15)
        (adj s15 s25) (adj s25 s15)
        (adj s16 s26) (adj s26 s16)
        (adj s21 s22) (adj s22 s21)
        (adj s21 s31) (adj s31 s21)
        (adj s22 s23) (adj s23 s22)
        (adj s22 s32) (adj s32 s22)
        (adj s23 s24) (adj s24 s23)
        (adj s23 s33) (adj s33 s23)
        (adj s24 s25) (adj s25 s24)
        (adj s24 s34) (adj s34 s24)
        (adj s25 s26) (adj s26 s25)
        (adj s25 s35) (adj s35 s25)
        (adj s26 s36) (adj s36 s26)
        (adj s31 s32) (adj s32 s31)
        (adj s31 s41) (adj s41 s31)
        (adj s32 s33) (adj s33 s32)
        (adj s32 s42) (adj s42 s32)
        (adj s33 s34) (adj s34 s33)
        (adj s33 s43) (adj s43 s33)
        (adj s34 s44) (adj s44 s34)
        (adj s34 s35) (adj s35 s34)
        (adj s34 s44) (adj s34 s44)
        (adj s35 s36) (adj s36 s35)
        (adj s35 s45) (adj s45 s35)
        (adj s36 s46) (adj s46 s36)
        (adj s41 s42) (adj s42 s41)
        (adj s41 s51) (adj s41 s51)
        (adj s42 s43) (adj s43 s42)
        (adj s42 s52) (adj s52 s42)
        (adj s43 s44) (adj s44 s43)
        (adj s43 s53) (adj s53 s43)
        (adj s44 s45) (adj s45 s44)
        (adj s44 s54) (adj s54 s44)
        (adj s45 s46) (adj s46 s45)
        (adj s45 s55) (adj s55 s45)
        (adj s46 s56) (adj s56 s46)
        (adj s51 s52) (adj s52 s51)
        (adj s51 s61) (adj s51 s61)
        (adj s52 s53) (adj s53 s52)
        (adj s52 s62) (adj s62 s52)
        (adj s53 s54) (adj s54 s53)
        (adj s53 s63) (adj s63 s53)
        (adj s54 s55) (adj s55 s54)
        (adj s54 s64) (adj s64 s54)
        (adj s55 s56) (adj s56 s55)
        (adj s55 s65) (adj s65 s55)
        (adj s56 s66) (adj s66 s56)
        (adj s61 s62) (adj s62 s61)
        (adj s62 s63) (adj s63 s62)
        (adj s63 s64) (adj s64 s63)
        (adj s64 s65) (adj s65 s64)
        (adj s65 s66) (adj s66 s65)
        

        ; cat
        (at c s11)

        ; mice
        (at m1 s12)
        (at m2 s15)
        (at m3 s34)
        (at m4 s45)
        (at m5 s54)
        (at m6 s62)

        ; walls
        (at w1 s16)
        (at w2 s22)
        (at w3 s24)
        (at w4 s52)
        (at w5 s66)

        ; trap
        (at t1 s21)
        (at t2 s23)
        (at t3 s25)
        (at t4 s44)
        (at t5 s61)
        (at t6 s63)
        
    )

    (:goal (and (dead m1) (dead m2) (dead m3) (dead m4) (dead m5) (dead m6) ))
)