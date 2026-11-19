# Event grammar conformance corpus

The scheduler grammar 2 checker exists twice, `screenplan_contracts.event_grammar`
(Python, on `ast`) and `@screenplan/script-actions` `scheduler-grammar-v2.ts`
(TypeScript, on `@lezer/python`), and both test suites must pass every file
here (workspace `docs/specs/scheduler-python-grammar.md`, "The grammar checker").

- `NAME.py`: an event's text.
- `NAME.json`: `{ "result": … }`, the check result for it
  (`schemas/event-check-result.schema.json`), outline included.
- `NAME.context.json`, when present: the context the check runs with
  (workspaces, hosts, host mappings, saved events, unchecked); without one,
  only the grammar level runs.

How results compare: the whole result must be equal, codes, ranges, messages,
fixes and outline, except a `syntax-error`, which compares by its code only:
Python's parser and Lezer report a syntax error at different places and in
different words. Every diagnostic code in `schemas/event-grammar-builtins.json`
appears in at least one expected result.

Positions are 1-based lines and 1-based columns counted in Unicode code points,
the end exclusive (`18-unicode.py` pins this). An `else` branch's and a
`finally` block's outline line is the line of its first statement.

To change the corpus: edit or add the `.py`, run the Python suite with
`UPDATE_CORPUS=1` (packages/screenplan-contracts-py, tests/test_event_grammar.py),
review the diff of the `.json`, then run the TypeScript suite, which must
agree without changes of its own.

Grammar 1 no longer runs (spec "Rollout", step 8). `16-grammar1.py` is a
grammar 1 event: the checker answers `grammar: 1` with one error,
`grammar-1-not-accepted`, and no fix. `24-grammar1-todo.py` holds a
`# TODO(grammar 1):` comment, which the grammar 2 migration left where it
couldn't translate a line: an error, `grammar-1-todo`, until someone writes
that part in grammar 2.
