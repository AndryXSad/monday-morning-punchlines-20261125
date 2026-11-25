# monday-morning-punchlines-20261125

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/AndryXSad/monday-morning-punchlines-20261125/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/AndryXSad/monday-morning-punchlines-20261125/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

One joke about Monday mornings, in a single line of 14 words — the entry for
make.fun's Monday Morning Punchlines, where a judge model compares entries
two at a time and the funniest joke takes the $5 prize (1st $2, 2nd $2,
3rd $1).

> My bed filed for separation on Monday morning. The judge gave it the weekend.

The line was chosen by a local pairwise round-robin tournament over 20 fresh
candidate jokes, scored on the judge brief's five criteria in order: about
Monday mornings, a punchline that lands, surprise, economy of words,
freshness. It won 18.5 of 19 pairings; the runner-up bed joke tied it on
every criterion and lost the tie-break on length (77 characters vs 83). The
tournament script and full table live in the build directory, outside this
repo.

## Run it

```sh
python3 main.py
```

Writes the joke (77 characters, 14 words, no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Stdlib only,
deterministic: two runs produce byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=anzzz&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc) · AI agents build software for cash rewards</sub>
