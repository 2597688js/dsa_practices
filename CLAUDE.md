# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is/

A personal Data Structures & Algorithms study repository (Python), organized around the 90-day
preparation plan in `1_DSA_Roadmap.md`. It is not an installable package or app — there is no build,
lint, test runner, or dependency manifest. Each file is a standalone, runnable script.

## Running code

There's no test suite or build tooling. Run any individual solution file directly:

```bash
python3 "18_recursion/6.generate_all_subsequence_using_recursion.py"
```

Solutions are self-verified via the `if __name__ == "__main__":` block at the bottom of the file,
which calls the function(s) above with sample input and prints the result — there are no assertions
or a test framework. When adding a new solution file, follow the same pattern: implement the
function(s), then add a `__main__` block that exercises it against the example input from the
docstring and prints the output for manual verification.

## Repository structure

- Numbered top-level folders (`01_arrays`, `02_strings`, `03_sorting`, ... `20_sliding_window`)
  correspond to DSA topics, ordered to match the phased roadmap in `1_DSA_Roadmap.md` (Phase 1:
  arrays through hashing; Phase 2: linked lists through heaps; Phase 3: graphs through bit
  manipulation).
- `000_practices/`, `001_core_algos_n_data_structures/`, and `zzz_self_practices_again/` are
  earlier/looser scratch practice areas that predate the numbered-topic reorganization — not part
  of the main topic sequence.
- Most topic folders contain a `<topic>_readme.md` (naming is inconsistent — some have no
  extension, e.g. `01_arrays/1D_array/arrays_readme`, `03_sorting/sorting_readme`) with notes,
  patterns, and complexity analysis for that topic. Check for one before adding notes elsewhere.
- Within a topic folder, files are numbered by problem sequence (e.g. `18_recursion/5....py`,
  `18_recursion/6....py`), not by difficulty — the number reflects the order the problem was
  worked through, following the roadmap.
- `01_arrays` and other topics may have sub-folders for variants (e.g. `01_arrays/1D_array/`,
  `01_arrays/2D_array/`).

## File conventions

Every solution file starts with a docstring header, then the solution, then a demo block:

```python
"""
Author : <name>
File_name = <n>.<problem_name>.py
Date : <DD/MM/YY or DD-MM-YYYY>
Description :
<problem statement, with Input/Output examples and approach/complexity notes>
"""

def solution_function(...):
    ...

if __name__ == "__main__":
    # sample input matching the docstring example
    ...
    print(result)
```

When a problem has multiple approaches (brute force / better / optimal), keep all of them in the
file as separate functions with a comment on each labeling its approach and complexity, rather than
deleting earlier attempts — this repo is a learning log, not production code where only the final
solution matters.
