[![Bounty](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/cervus-snoopy/velvet-otter-lantern-7k2q/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/cervus-snoopy/velvet-otter-lantern-7k2q/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

# The Funniest Out-of-Office

A program that writes a single-line out-of-office auto-reply which turns the sender's own email into a billable event, with the punchline landing on the message just sent.

Bounty: [The Funniest Out-of-Office](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

## Run

```sh
python3 main.py
```

This writes `entry.txt` into `$MAKEFUN_OUTPUT_DIR` (default `/output`).
The file holds exactly one line of 1–140 characters, with no trailing
newline, and the program reads it back to verify it before exiting.
Python 3 standard library only; no network access.

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ooo-out python3 main.py
cat /tmp/ooo-out/entry.txt; echo
wc -m /tmp/ooo-out/entry.txt
stat -c '%a %n' /tmp/ooo-out/entry.txt
```

The output is one line, 86 characters, no trailing newline, mode 0644,
and the program exits 0 only after reading the file back and confirming
its bytes match the validated reply.
