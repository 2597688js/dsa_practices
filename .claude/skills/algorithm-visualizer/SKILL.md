---
name: algorithm-visualizer
description: Turn a piece of algorithm/data-structure code (searching, sorting, two-pointer, sliding window, recursion, tree/graph traversal, DP, etc.) into an interactive, self-contained HTML animation that plays or steps through exactly how it executes on a concrete example. Use this whenever the user pastes or references code and asks to visualize, animate, illustrate, or "show me how this works" / "walk me through this step by step" — including requests that just say "make an animation of this" or "can you visualize my algorithm" without naming a specific technique. Also use it proactively when explaining how a classic algorithm works if a step-through animation would make the explanation clearer than prose or a static diagram alone.
disable-model-invocation: true
---₹

# Algorithm Visualizer

Build a small interactive HTML page that steps through an algorithm's real
execution: an array of boxes (or tree/graph/grid — see below), pointers
that move as labeled flags, cells that light up on comparisons, swaps,
eliminations, and a narration line explaining each moment, with
play/pause/step/scrub controls and the source code panel highlighting the
current line.

## Resolving the target file from arguments

This skill can be invoked as `/algorithm-visualizer @path/to/file.py` (or
with a bare path, no `@`). When an argument is present:

- Treat it as the file to visualize — read it with the Read tool
  immediately and use its contents as "the user's code" in step 1 below.
  Don't ask the user which file they mean; the argument already answered
  that.
- If the path doesn't resolve, say so and ask for the correct path rather
  than guessing at a similarly-named file.
- If the file defines multiple functions/classes implementing different
  algorithms or variants, still ask which one to animate (or default to
  the first/clearest one and say so) — the argument picked the *file*, not
  necessarily the *function*.
- If the file has no real implementation (e.g. just a docstring/comment
  stub with no executable logic), tell the user directly and ask whether
  to (a) write a standard implementation of that algorithm into the file
  first, using the file's existing style/naming, and then animate it, or
  (b) point to a different file instead. Don't silently invent an
  implementation or silently switch files.

If no argument is given, fall back to whatever code the user pasted or
referenced earlier in the conversation, as before.

## Why trace-then-render, not hand-animate

The core idea: don't try to *imagine* what the algorithm does and script an
animation from that mental model — actually **run the algorithm** on a
small concrete input with a few instrumentation calls added, record the
real sequence of states, and render *that*. This guarantees the animation
matches the code's actual behavior (including off-by-one quirks,
edge-case handling, etc.), rather than a simplified or subtly-wrong
retelling of it. It also means the same approach works for any algorithm
the user throws at you, not just a hardcoded set of "supported" ones.

## Workflow

### 1. Understand the algorithm and pick an example input

Read the user's code and identify: the primary data structure being
operated on (array is the common case — sorting, searching, two-pointer,
sliding window, 1D DP; see `references/other-data-structures.md` for
trees/graphs/linked lists/grids), the state that actually matters to show
(pointers/indices, comparisons, swaps, recursive calls), and a **small,
illustrative concrete input** — not the trivial case, not something so
large the animation is unreadable. For a search/sort, 7–15 elements is
usually the sweet spot; pick values and a target that exercise an
interesting path (e.g. for binary search, a target that isn't in the
middle and requires at least 2–3 narrowing steps, so the viewer actually
sees the range shrink).

If the user gave multiple implementations of the same idea (as in a file
with several variants), ask which one they want animated, or default to
the first/clearest one and mention that you picked it.

### 2. Instrument the code with the tracer

Use `scripts/trace_recorder.py`'s `Tracer` class. Copy the user's function,
keep its logic completely unchanged, and add `tracer.step(...)` calls at
the meaningful state-changing moments — typically once per loop iteration
or recursive call, plus one at the start and one at the terminal
return/found/not-found point. Don't record every single line; record every
moment a human following along would want to pause on. Read the full
docstring in `scripts/trace_recorder.py` for the exact `step()` signature
and the `highlight` tag vocabulary (`compare`, `found`, `eliminated`,
`swap`, `sorted`, `pivot`, `visiting`).

Write clear, specific `message` text for each step — reference actual
values from this run ("mid=4 → arr[4]=16, target=23, 16 < 23 so search the
right half"), not generic descriptions. This narration is most of what
makes the animation actually teach something.

Pass the *real* source text of the function (the unmodified version, not
your instrumented copy) as `source_code` so the code panel matches what
the user actually wrote, and set each step's `line` to the matching line
number in that original source.

### 3. Run it and export the trace

Run the instrumented function on your chosen example input, then
`tracer.export("trace.json")`. Sanity-check the step count — fewer than
~4 steps usually means the example input was too trivial (pick one that
takes a more interesting path); more than ~30 steps is usually too many to
follow (shrink the input).

### 4. Render the final HTML

Read `assets/animation_template.html`, replace `__TITLE__` with the
algorithm's title and `__TRACE_DATA__` with the JSON you exported
(`json.dumps(trace_dict)` inlined directly as a JS value — it's valid JS
since JSON is a subset). The template is fully self-contained (no CDN
dependencies, no build step) — a single HTML file that works offline and
is easy to share.

### 5. Deliver it

Save the finished file to the outputs directory and present it to the
user. If you're in an environment where HTML renders as an artifact,
they can also try it inline before downloading.

## Extending beyond arrays

For trees, graphs, linked lists, or grids, read
`references/other-data-structures.md` — same trace-driven workflow, same
transport controls and narration console, just a different stage-drawing
function since the shape being visualized isn't a row of boxes.

## Quality bar

Before delivering, mentally step through the animation frame by frame:
does each `message` say something a viewer couldn't already see from the
boxes alone? Do the pointer labels match the variable names in the actual
code? Does the example input make the algorithm do something non-trivial
(branch, narrow, swap, recurse more than once)? If the user reacts with
"this doesn't really show what makes the algorithm interesting," the fix
is almost always a better example input or a missing intermediate step,
not a redesign of the visual style.