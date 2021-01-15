(define (problem cat-p02)
    (:domain cat)
    (:objects
        c - cat
        m1 m2 - mouse
        w1 w2 - wall
        s11 s12 s13 s14
        s21 s22 s23 s24
        s31 s32 s33 s34
        s41 s42 s43 s44
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
        (adj s14 s24) (adj s24 s14)
        (adj s21 s22) (adj s22 s21)
        (adj s21 s31) (adj s31 s21)
        (adj s22 s23) (adj s23 s22)
        (adj s22 s32) (adj s32 s22)
        (adj s23 s24) (adj s24 s23)
        (adj s23 s33) (adj s33 s23)
        (adj s24 s34) (adj s34 s24)
        (adj s31 s32) (adj s32 s31)
        (adj s31 s41) (adj s41 s31)
        (adj s32 s33) (adj s33 s32)
        (adj s32 s42) (adj s42 s32)
        (adj s33 s34) (adj s34 s33)
        (adj s33 s43) (adj s43 s33)
        (adj s34 s44) (adj s44 s34)
        (adj s41 s42) (adj s42 s41)
        (adj s42 s43) (adj s43 s42)
        (adj s43 s44) (adj s44 s43)

        ; cat
        (at c s11)

        ; mice
        (at m1 s31)
        (at m2 s24)

        ; walls
        (at w1 s21)
    )

    (:goal (and (dead m1) (dead m2)))
)