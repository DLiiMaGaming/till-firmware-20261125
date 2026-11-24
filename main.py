#!/usr/bin/env python3
"""Till Firmware Do Us Part — u-azazex-till-firmware-do-us-part-32172929.

Writes one wedding vow a robot speaks at its own wedding to
/output/entry.txt. One sentence, under 200 characters, per RULES.txt.

The vow: a promise of love that survives every firmware update — the
joke lands out of the situation itself (a robot rebooting mid-vow and
forgetting its beloved's name for a second), with the tenderness
carried by the promise itself: love outlasts even a memory wipe.
"""

ENTRY = (
    "I promise to love you through every firmware update, even the ones "
    "that reboot me mid-vow and make me forget your name for a second."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
