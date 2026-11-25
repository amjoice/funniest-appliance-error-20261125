#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line (at most 200 characters): the funniest honest error
message an appliance could show, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim.

The line was picked by sparring candidates pairwise against the published
judge brief (deadpan appliance engineer; in order: an honest error an
appliance could plausibly show, a real laugh/surprise/twist, honesty naming
a plausible fault, the machine's own flat put-upon voice, economy), not as
a first draft. Candidates weighed:

- "ERROR E17: DRAIN BLOCKED. THE WATER IS NOT LEAVING. NEITHER ARE YOUR
  CLOTHES." Real fault, good twist, but the shouty caps read like a
  warning sign, not a flat machine voice.
- "Fault: drum unbalanced. One trainer, one duvet. I have been shaking for
  twenty minutes. Please come and look at me." Vivid and funny, but 116
  chars and the plea ("please come and look at me") risks reading cute
  rather than flat; the machine sounds like it means to be funny.
- "Error: bread jammed. It is now charcoal. I did warn you. You smelled
  it." Strong and accusatory, but the laugh leans on blaming the owner
  rather than on the fault itself.
- "Error: ice maker jammed. There is no ice. There will be no ice. Please
  stop pressing the button." Very put-upon, but the joke is only repetition;
  no surprise after the second sentence.
- "Error: lever stuck down. The bread has given up. So have I." The
  shortest (59 chars) and very flat, but "so have I" is a smaller twist
  than the winner's and the fault is less concrete than "boiled air".

Winner: a kettle that ran dry. "No water detected" is a fault a kettle
really reports; "I boiled air for three minutes" is the plain truth of
what it did; "I am sorry" is the flat apology; "I am also empty" is the
surprise -- empty means no water and, at the same time, spent. The machine
states facts without meaning to be funny, which is exactly what the brief
calls the best line. 86 characters, which also wins a size tie-break.
"""

import os

LINE = (
    "Error: no water detected. I boiled air for three minutes. "
    "I am sorry. I am also empty."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be one clean line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
