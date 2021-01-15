(define (domain cat)
    (:requirements :strips)
    (:types cat mouse wall trap square)
    (:predicates
        (at ?who ?where)
        (adj ?s1 ?s2 - square)
        (dead ?m)
        (has ?who ?what)
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
            (not (exists (?m1 - mouse) (has ?c ?m1)))
        )
        :effect (and 
            (not (at ?m ?s)) 
            (dead ?m)
        )
    )

    (:action grab
        :parameters (?c - cat ?s - square ?m - mouse)
        :precondition (and 
            (not (dead ?c))
            (at ?m ?s) 
            (at ?c ?s)
            (not (exists (?m1 - mouse) (has ?c ?m1)))
        )
        :effect (and 
            (not (at ?m ?s)) 
            (has ?c ?m)
        )
    )

    (:action disable-trap
        :parameters (?c - cat ?s1 - square ?s2 - square ?m - mouse ?t - trap)
        :precondition (and 
            (not (dead ?c))
            (adj ?s1 ?s2)
            (at ?c ?s1)
            (at ?t ?s2)
            (has ?c ?m) 
        )
        :effect (and 
            (not (at ?t ?s2)) 
            (dead ?m)
            (not (has ?c ?m))
        )
    )

    (:action drop
        :parameters (?c - cat ?s - square ?s2 - square ?m - mouse)
        :precondition (and 
            (not (dead ?c))
            (has ?c ?m) 
            (at ?c ?s)
            (adj ?s ?s2)
        )
        :effect (and 
            (not (has ?c ?m))            
            (at ?m ?s2)
        )
    )
)
