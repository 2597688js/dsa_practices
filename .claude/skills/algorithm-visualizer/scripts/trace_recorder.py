"""
Tracer — records a step-by-step trace of an algorithm's real execution so
it can be rendered as an interactive HTML animation (see
assets/animation_template.html).

Basic usage
-----------
    from trace_recorder import Tracer

    tracer = Tracer(
        title="Binary Search",
        source_code=open("original_binary_search.py").read(),
        structure="array",   # or "tree" / "graph" / "linked_list" / "grid"
    )

    tracer.step(
        message="low=0, high=6, mid=3 -> arr[3]=16, target=23, 16 < 23 so search the right half",
        line=7,
        array=arr,
        pointers={"low": 0, "high": 6, "mid": 3},
        highlights={3: "compare", 0: "eliminated", 1: "eliminated", 2: "eliminated"},
    )
    ...
    tracer.export("trace.json")

step() signature
-----------------
    tracer.step(message, line=None, highlights=None, pointers=None, **structure_state)

    message (str, required)
        Specific narration for this moment. Reference the *actual* values
        from this run ("mid=4 -> arr[4]=16, target=23, 16 < 23 so search
        the right half"), not a generic description of what the code does.

    line (int, optional)
        1-indexed line number in the ORIGINAL (unmodified) source you pass
        as `source_code` — the code panel highlights this line.

    highlights (dict, optional)
        Maps an index / node id / (row, col) key to one of the tags below.
        The renderer colors each matching cell/box/node accordingly.

    pointers (dict, optional)
        Maps a label (matching the variable name in the code, e.g. "i",
        "low", "mid") to an index / node id — rendered as a small flag
        under (or next to) that cell so viewers can track named variables.

    **structure_state (required, at least one)
        The current full state of the thing being visualized, passed
        under the field name matching `structure`:
          - structure="array"        -> array=[...]
          - structure="grid"         -> grid=[[...], [...], ...]
          - structure="tree"         -> tree={...}            (see references/other-data-structures.md)
          - structure="graph"        -> graph={"nodes": [...], "edges": [...]}
          - structure="linked_list"  -> linked_list=[...]
        You may pass more than one field (e.g. `array` plus a scalar like
        `pivot_value=17`) — anything extra rides along in the step record
        and is available to a custom stage-drawing function.

    IMPORTANT — pass live state, not a manual copy: step() deep-copies
    every structure_state value at call time, so it's safe (and expected)
    to call tracer.step(..., array=arr) repeatedly on the SAME mutating
    list across a loop. Without this, every recorded step would show the
    array's *final* state instead of its state at that moment, since
    Python stores references, not snapshots.

Highlight tag vocabulary
------------------------
    compare     - two or more elements being compared right now
    found       - the target/answer has just been located
    eliminated  - ruled out of consideration (binary search half, pruned
                  branch, exhausted candidate, ...)
    swap        - elements currently being exchanged
    sorted      - finalized / locked into its correct final position
    pivot       - the pivot element in partition-based algorithms
    visiting    - the node/cell currently being visited or computed
                  (traversal, DP cell fill, grid cell, ...)

Pick the closest match. Don't invent new tags unless you also extend the
CSS in animation_template.html to style them — an unrecognized tag falls
back to a neutral "active" style, which still works but loses color
meaning.

Exporting
---------
    tracer.export("trace.json")   # writes JSON to disk
    tracer.to_dict()              # same data as a Python dict, no file I/O

Either is fine for step 4 of the workflow (embedding into the HTML
template) — `json.dumps(tracer.to_dict())` is valid to inline directly as
a JS value, since JSON is a subset of JS object-literal syntax.
"""

import copy
import json


class Tracer:
    VALID_STRUCTURES = {"array", "grid", "tree", "graph", "linked_list"}

    def __init__(self, title, source_code, structure="array"):
        if structure not in self.VALID_STRUCTURES:
            raise ValueError(
                f"structure={structure!r} not in {sorted(self.VALID_STRUCTURES)}"
            )
        self.title = title
        self.source_code = source_code
        self.structure = structure
        self.steps = []

    def step(self, message, line=None, highlights=None, pointers=None, **structure_state):
        if not message:
            raise ValueError("step() requires a specific, non-empty message")
        if not structure_state:
            raise ValueError(
                "step() needs at least one structure keyword matching "
                f"structure={self.structure!r}, e.g. array=[...]"
            )

        entry = {
            "message": message,
            "line": line,
            "highlights": {str(k): v for k, v in (highlights or {}).items()},
            "pointers": dict(pointers or {}),
        }
        # Deep-copy so later in-place mutation of the caller's structure
        # doesn't retroactively change already-recorded steps.
        entry.update(copy.deepcopy(structure_state))
        self.steps.append(entry)

    def to_dict(self):
        return {
            "title": self.title,
            "source_code": self.source_code,
            "structure": self.structure,
            "steps": self.steps,
        }

    def export(self, path):
        data = self.to_dict()
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return data
