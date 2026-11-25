# Fortune Cookie for the Liquidated Trader

Entry for the make.fun bounty
[u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
($2 pot, 1st $0.64).

## The entry

`main.py` writes one fortune-cookie line to `/output/entry.txt`:

> Your lucky numbers are 0, 0, 0, and the amount still in your account.

14 words, 69 characters, one line, no trailing newline — inside the gate
(1–160 UTF-8 characters) and the brief's 20-word cap.

The line is a real fortune slip first: the classic "lucky numbers" device.
The punchline is the trader's own empty account — the balance IS the loss,
stated outright, and the last word lands the turn. Rueful and warm, never
cruel: the joke is on the empty wallet, not on the trader.

## Running it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py out.txt    # or any path given as argv[1]
```

Pure Python 3 standard library, deterministic, no network, no randomness,
no clock. The output file is chmodded 0o644; the output directory itself
is never chmodded.
