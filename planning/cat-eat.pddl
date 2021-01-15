(define (domain cat)
    (:requirements :strips)
    (:types cat mouse square)
    (:predicates
        (at ?who ?where)
        (adj ?s1 ?s2 - square)
        (dead ?m)
    )

    (:action move
        :parameters (?c - cat ?s1 - square ?s2 - square)
        :precondition (and 
            (adj ?s1 ?s2)
            (at ?c ?s1)
        )
        :effect (and 
            (not (at ?c ?s1))
            (at ?c ?s2)
        )
    )
  
    (:action eat
        :parameters (?c - cat ?s - square ?m - mouse)
        :precondition (and 
            (at ?m ?s) 
            (at ?c ?s)
        )
        :effect (and 
            (not (at ?m ?s)) 
            (dead ?m)
        )
    )
)
