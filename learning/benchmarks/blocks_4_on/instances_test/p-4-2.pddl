

(define (problem BW-rand-4)
(:domain blocksworld)
(:objects b3 b4 )
(:init
(arm-empty)
(on b3 b4)
(on b4 b1)
(on-table b1)
(on-table b2)
(clear b2)
(clear b3)
)
(:goal
(and
(on b1 b2))
)
)


