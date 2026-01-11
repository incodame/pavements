# First time:

Pavement requires swi-prolog 9 for the janus python library

```
docker run -it --network host -v $(pwd):/opt/pavements swipl
```

## install:
```
?- pack_install(list_util).
?- pack_install(regex).
```

## start a working session with:
```
?- consult('/opt/pavements/src/prolog/paragraph_conf.pl').
```

## load and execute a test suite such as doc_t with:
```
?- consult('/opt/pavements/src/prolog/t/pavements_t.plt').
?- run_tests.
```
## leave session
type CTRL+D

# Next time:
```
docker start -ai $(docker container ls -a | grep swipl | head -1 | awk '{print $1}')
```

perform the previous consults by typing the UP-arrow 
