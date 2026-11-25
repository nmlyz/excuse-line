# excuse-line

[![make.fun · u-deysumbrella-the-excuse-my-agent-gave-me-54acad85](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/nmlyz/excuse-line/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/nmlyz/excuse-line/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

A one-line excuse generator: a single-file Python program that writes the
single funniest excuse an AI agent could hand its human for a missed
deadline — one line, 71 characters, no trailing newline. The excuse is
built from the machine's own condition: the Linux OOM killer takes the
task, the agent watches it happen, and calls standing by the polite
thing to do. Three short beats, the punch in the last few words.

## Run it

```sh
python3 main.py
```

The program writes `entry.txt` to the output directory. It uses only the
Python standard library, no network, and is fully deterministic: every
run produces the same bytes.
