from typing import List, Tuple


# Returns donor types compatible with a recipient type for RBC transfusion.
def compatible_donors(recipient_bg: str, recipient_rh: str) -> List[Tuple[str, str]]:
    bg = recipient_bg.upper()
    rh = recipient_rh

    abo_map = {
        "O": ["O"],
        "A": ["A", "O"],
        "B": ["B", "O"],
        "AB": ["AB", "A", "B", "O"],
    }

    rh_map = {
        "+": ["+", "-"],
        "-": ["-"],
    }

    donors: List[Tuple[str, str]] = []
    for d_bg in abo_map.get(bg, []):
        for d_rh in rh_map.get(rh, ["-"]):
            donors.append((d_bg, d_rh))

    # Prioritize closer matches first (same group and RH first)
    donors.sort(key=lambda t: (
        t[0] != bg,  # same group first
        t[1] != rh,  # same Rh first
        # Then alphabetical as a stable order
        t[0],
        t[1],
    ))
    return donors

