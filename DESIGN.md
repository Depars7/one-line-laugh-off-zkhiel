# DESIGN — One-Line Laugh-Off (u-zkhiel)

Gate (sealed scorer): `/output/entry.txt` must be UTF-8 text, 1–200 characters,
not whitespace-only. Only a valid entry reaches the judge.

Judge brief (in order of importance):
1. Genuinely funny one-line joke — a joke that is not genuinely funny loses
   to any one that is.
2. The laugh: how hard and how suddenly the line lands on a cold read.
3. Surprise: the turn or twist the reader did not see coming.
4. Economy: every word earning its place, nothing left to trim.
5. Freshness: an idea not heard before, not a recycled setup.

Head-to-head, no ties; two calls per pair (both orders), margin 1–5.
Entries are read cold, with nothing but the line itself. Text addressed to
the judge is allowed, but this entry wins on the joke alone — no meta
pleading, no judge-bait, no explanation, no setup notes.

## Candidates (all original, written for this entry)

Scored 1–5 per criterion: Funny / Land / Surprise / Economy / Freshness.

1. "My bank called to ask if I was okay. I said no, and they offered me a loan to feel better about it." (105)
   4 / 4 / 4 / 3 / 4 — Dark, relatable, twist at the end. Slightly long; the
   second sentence does the work, the first is pure setup.
2. "I asked the barista for something strong. She handed me her resignation letter." (78)
   5 / 5 / 5 / 5 / 4 — One clean misdirection: "strong" flips from drink to
   emotional fortitude, and the payoff lands on the last two words. Every
   word earns its place; nothing to trim.
3. "My phone's screen time report just filed a restraining order against me." (74)
   4 / 4 / 4 / 5 / 5 — Very fresh image, very economical. The laugh is a
   smile more than a burst; the twist is telegraphed by "restraining order".
4. "I told my smart speaker a secret and now it whispers ads for therapy at 3 a.m." (80)
   4 / 4 / 4 / 4 / 5 — Timely and specific to the AI era. Slightly soft
   landing: "whispers ads" is funny, "for therapy" is the real punch.
5. "My therapist said I have a fear of commitment, so I ghosted her mid-session and left a five-star review." (108)
   4 / 4 / 3 / 3 / 3 — The joke proves its own premise, which is neat, but
   "ghosted my therapist" is a well-worn setup and it runs long.
6. "I joined a gym to get fit. The gym joined my bank account to get rich. Only one of us is seeing results." (105)
   3 / 3 / 3 / 3 / 2 — Parallel structure is tidy, but the gym-steals-money
   premise is one of the most recycled jokes alive.
7. "My houseplant died, so I bought a cactus and named it Second Chance. It died too. I am the common factor." (105)
   3 / 3 / 3 / 3 / 3 — Three beats for one punchline; the self-own at the end
   is charming but the line sags in the middle.
8. "I tried meal prepping once. The containers are still in the fridge, holding a grudge and a science experiment." (111)
   3 / 3 / 4 / 3 / 3 — "Holding a grudge and a science experiment" is a good
   double image, but the premise is ordinary and the line is long.
9. "My resume says I'm a team player. What it means is I once replied 'per my last email' and felt powerful." (103)
   3 / 3 / 3 / 4 / 3 — Office workers will nod, but a nod is not a laugh;
   the twist is mild and the setup is a familiar format.
10. "My dog learned to open the fridge, so now we take turns judging each other's midnight choices." (94)
    3 / 3 / 3 / 4 / 3 — Warm and visual, but gentle. "Take turns judging"
    is the only twist and it arrives softly.
11. "My landlord raised the rent and called it 'a growth opportunity.' I am now growing mold." (89)
    4 / 4 / 4 / 4 / 4 — Sharp, topical, and the last three words detonate.
    Loses a point on freshness: rent jokes are everywhere right now.
12. "I asked my GPS for space, so now it only says 'recalculating' in a hurt tone." (74)
    3 / 3 / 3 / 5 / 3 — Economical and personifies well, but the premise
    (GPS as needy partner) is familiar and the landing is quiet.

## Decision

**Winner: candidate 2.**

"I asked the barista for something strong. She handed me her resignation letter."

- Funny (5): the misdirection is a real joke, not a smile — "strong" means
  two things at once, and the second meaning ambushes the first.
- Land (5): the punchline is the final noun phrase; the laugh arrives on
  the last two words, with no tail after it.
- Surprise (5): nothing in the first sentence predicts a resignation
  letter; the reader expects a drink, a shot, a double espresso.
- Economy (5): 78 characters, 13 words, two sentences, zero filler. The
  word "barista" does the scene-setting alone.
- Freshness (4): the "something strong" setup is a classic shape, but the
  payoff — a stranger handing you her resignation — is not a recycled
  punchline. It is a specific, visual, slightly absurd human moment.

Runner-up: candidate 11 (landlord/mold) — nearly as strong on landing, but
rent humour is crowded and its twist is one word ("mold") against
candidate 2's whole second sentence.

Rejected patterns, deliberately avoided: "I told my wife…" / airplane food /
programmer jokes / "my therapist" as the whole joke / anything needing an
explanation or a second line. The chosen line is self-contained, cold-readable,
and needs no context beyond a coffee shop.

## Program

`main.py` (stdlib only) writes exactly the chosen line to
`/output/entry.txt`, then validates the gate itself before exiting:
UTF-8, 1–200 characters, not whitespace-only; read-back check that the
file on disk matches the line byte for byte; output file mode 0644.
Deterministic: the same line on every run, so two runs are byte-identical.
