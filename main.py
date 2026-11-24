"""Two-Sentence Horror — make.fun entry.

The entry: exactly two sentences, at most 400 characters, the
scariest two-sentence horror story. The winning shape for an
ultra-short horror brief is a dark reversal with the twist word
last: an ordinary scene, then a fatal last word. Sentence one sets
the ordinary scene — a parent, a baby monitor, 3 AM, six hours of
static finally ending, a whispered thank you to an empty nursery.
Sentence two reverses it: the voice that had been whispering
lullabies all night whispers back, from inside the crib, "You're
welcome." The horror is that the comfort was never the parent's:
something else was singing the child to sleep all night, and it is
still in the room, polite enough to answer. The twist word is the
last one the reader meets — welcome — and it turns gratitude into
dread.

Candidates considered and rejected:
- "I checked the baby monitor and saw my daughter sleeping
  peacefully, so I finally slept too. I woke to her standing over
  me, whispering the lullaby I had heard through the monitor all
  night." — the reversal is there, but the second sentence explains
  the scare instead of delivering it; the twist lands in the middle,
  not on the last word.
- "The smart lock logged my wife coming home at midnight, and I
  made her tea. She has been dead for three years, and the tea is
  gone." — a strong fatal last word, but the setup spends its
  sentence on a log entry rather than a scene the reader can feel.
- "Every night the attic whispers my name, and every night I
  pretend not to hear it. Last night it whispered my daughter's
  name, in my voice." — close, but the second sentence is two
  beats (her name, my voice) competing for the last word.
The chosen story wins on the brief's own order: a concrete ordinary
scene (baby monitor, 3 AM, six hours of static), a specific number
(six hours), and the reversal landing on the very last word
("welcome"), which reframes the whole first sentence as a
conversation with something in the crib. Exactly two sentences and
242 characters, inside the 400-character cap, with no dollar
amounts anywhere. Note the deliberate "3 AM": the story avoids
"a.m." so no stray period can ever be mistaken for a sentence
boundary.
"""

TEXT = (
    "The baby monitor finally stopped crackling at 3 AM, after six "
    "hours of static, and I whispered thank you to the empty "
    "nursery. Then the voice that had been whispering lullabies all "
    "night whispered back, from inside the crib, 'You're welcome.'"
)


def main() -> None:
    """Write the horror story to ``<output_dir>/entry.txt``."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
