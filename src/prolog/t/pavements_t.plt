:- use_module(library(plunit)).
:- use_module(library(xpath)).
:- begin_tests(paragraph_conf).
:- working_directory('..').
:- use_module(paragraph_conf).

test('read graph') :-
    application(app, 'paragraph', paragraph, [ build(maven) ]).

:- end_tests(paragraph_conf).