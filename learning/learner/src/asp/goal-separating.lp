% Optimization: smallest sum over feature complexities
#minimize { C,complexity(F, C) : complexity(F, C), boolean(F), select(F) }.

% Generate selected Boolean features
{ select(F) } :- boolean(F).

% Goal-separation
:- nongoal(I, S), goal(I', S'), { boolean(F) : select(F), b_value(I, S, F, V), b_value(I', S', F, V'), V != V' } = 0.

#show select/1.
#show numerical/1.
#show boolean/1.