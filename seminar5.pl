sum([], 0).
sum([H|T], Sum) :-
   sum(T, Rest),
   Sum is H + Rest.

?-sum([1,2,3,4,5,6], Sum).