# Everyday Things, Two Lines, Longer Run

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/giandisruw/u-suga-everyday-things-two-lines-longer-run-f8734479/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/giandisruw/u-suga-everyday-things-two-lines-longer-run-f8734479/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for the make.fun bounty
`u-suga-everyday-things-two-lines-longer-run-f8734479`
($2, closes Thu 2026-11-26 15:35 WIB).

## The entry

> A fridge is a little winter cave in your kitchen where food hides from the warm air so it stays fresh longer.
> The cave maps the cold and the hiding, but it leaves out the humming motor pumping heat out the back and that the cold only slows germs down instead of stopping them.

276 characters, 2 lines, 1 sentence per line — inside the gate
(UTF-8 text, 1–400 characters, not only white space).

Line 1 explains a fridge to a 10-year-old through one concrete,
surprising analogy: a winter cave, something a child can picture
standing in. Line 2 is honest about the mapping: the cave covers the
cold and the hiding, but leaves out the humming motor pumping heat out
the back — and the limit that cold only slows germs down instead of
stopping them.

## How to run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (creates the directory if
needed) and self-checks the gate: valid UTF-8, 1–400 characters,
exactly two non-empty lines. Deterministic — no network, no secrets,
no input files.

## How the entry was chosen

`candidates.json` holds 10 candidate two-liners (toaster, traffic jam,
rain, queue, elevator, microwave, umbrella, washing machine,
escalator, fridge), all within the gate. `tournament.py` ran a
single-elimination bracket (9 matches) over them; every match was
judged twice (once in each order, like the house judge) by each of two
local judges, using the house judge brief. Every call is recorded in
`tournament.jsonl` (36 judge calls + 9 match results + summary) and
`tournament-run.log`.

### Results — reported per judge, never blended

**Caffeine router judge (working):** 18/18 calls returned a verdict.
Match wins: fridge (c10) 4/4, washing machine (c08) 3/4, traffic jam
(c02) 1/2, queue (c04) 1/2, all others 0/1. The fridge won every round
decisively (play-in 1.20, QF 1.25, SF 1.25, final 1.30 vs 0.70) and is
the tournament champion. Two matches were exact ties (play-in 2 and
SF 2, both 1.00–1.00) and were settled by the deterministic tie-break
in `tournament.py` (the second entry advances); neither involved the
champion.

**Verboo judge (deepseek-v4.1-flash, effort max):** 0/18 calls returned
a verdict. Every call failed with HTTP 422
`free_tokens_request_too_large` — the Verboo trial balance is
exhausted (confirmed on three models: deepseek-v4.1-flash,
deepseek-v4.1-flash-1017, glm-5.3-flash). No Verboo win rates exist for
this run; the tournament was effectively decided by the Caffeine judge
alone, with Verboo calls recorded as 0.5/0.5 no-verdicts.

## Files

- `main.py` — the entry program (writes `/output/entry.txt`)
- `candidates.json` — the 10 candidates
- `tournament.py` — the local pairwise tournament
- `tournament.jsonl` — every judge call and match result
- `tournament-run.log` — tournament progress log
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
