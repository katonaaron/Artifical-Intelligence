(define (domain cat)
    (:requirements :strips)
    (:types cat mouse wall trap square)
    (:predicates
        (at ?who ?where)
        (adj ?s1 ?s2 - square)
        (dead ?m)
    )

    (:action move
        :parameters (?c - cat ?s1 - square ?s2 - square)
        :precondition (and 
            (not (dead ?c))
            (adj ?s1 ?s2)
            (at ?c ?s1)
            (not (exists (?w - wall) (at ?w ?s2)))
        )
        :effect (and 
            (not (at ?c ?s1))
            (when (exists (?t - trap) (at ?t ?s2)) (dead ?c))
            (when (not(exists (?t - trap) (at ?t ?s2))) (at ?c ?s2))
        )
    )
  
    (:action eat
        :parameters (?c - cat ?s - square ?m - mouse)
        :precondition (and 
            (not (dead ?c))
            (at ?m ?s) 
            (at ?c ?s)
        )
        :effect (and 
            (not (at ?m ?s)) 
            (dead ?m)
        )
    )
)
