# Visualizing trees, graphs, linked lists, and grids

The overall workflow is identical to the array case: instrument with
`scripts/trace_recorder.py`'s `Tracer`, run the real function on a small
example, export the trace, then render it with
`assets/animation_template.html`. The only thing that changes is the
shape of the state you pass to `tracer.step(...)` and the stage-drawing
function in the HTML template that turns that state into boxes/nodes on
screen.

`grid` (2D array) is already built into the template — pass
`grid=[[...], [...]]` and `highlights`/`pointers` keyed by `"row,col"`
strings (e.g. `"2,3"`). Use it as-is for DP tables, matrix pathfinding,
etc. Tree, graph, and linked list need a small addition to the template,
described below.

## General pattern for adding a structure

1. Pick `structure="tree"` (or `"graph"` / `"linked_list"`) when
   constructing the `Tracer`.
2. In each `tracer.step(...)` call, pass the structure's current state
   under that same field name (`tree=...`, `graph=...`,
   `linked_list=...`), plus the usual `message`, `line`, `highlights`,
   and `pointers`.
3. Open `assets/animation_template.html` after copying it for this
   animation, and:
   - Add one of the `renderXStage(step)` functions below (paste as-is,
     they only touch `stageBody` and reuse the existing `.box`,
     `.tag-*`, and `.flag` CSS classes already defined in the template).
   - Add a branch for it in the `renderStage(step)` dispatcher, e.g.
     `if (DATA.structure === "tree") return renderTreeStage(step);`

Keep using the same highlight tags (`compare`, `found`, `eliminated`,
`swap`, `sorted`, `pivot`, `visiting`) — the CSS classes already exist,
so a tree node marked `"visiting"` gets the same blue treatment an array
box would.

## Tree

**Step shape:** pass `tree` as a nested dict, one entry per node id:

```python
tracer.step(
    message="visiting node 8, its value 8 > 5 so recurse left",
    line=12,
    highlights={"n8": "visiting"},
    pointers={"root": "n8"},
    tree={
        "n8": {"value": 8, "left": "n3", "right": "n10"},
        "n3": {"value": 3, "left": None, "right": "n6"},
        "n6": {"value": 6, "left": None, "right": None},
        "n10": {"value": 10, "left": None, "right": None},
    },
    root_id="n8",
)
```

Node ids should be stable strings you invent (e.g. `f"n{id(node)}"` or
just the value if values are unique) — they're what `highlights` and
`pointers` key into. `root_id` (an extra scalar field) tells the renderer
where to start laying out the tree; include it every step since the root
can change (e.g. after a rotation).

**Renderer** — paste into the template's `<script>` block:

```javascript
function renderTreeStage(step) {
  const nodes = step.tree || {};
  const highlights = step.highlights || {};
  const pointers = step.pointers || {};
  const flagsByNode = {};
  Object.entries(pointers).forEach(([label, id]) => {
    (flagsByNode[id] = flagsByNode[id] || []).push(label);
  });

  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  const HGAP = 60, VGAP = 70, R = 20;
  const positions = {};
  let nextX = 0;

  function layout(id, depth) {
    if (!id || !nodes[id]) return;
    const node = nodes[id];
    layout(node.left, depth + 1);
    const x = nextX++ * HGAP;
    positions[id] = { x, y: depth * VGAP + 30 };
    layout(node.right, depth + 1);
  }
  layout(step.root_id, 0);

  const maxX = Math.max(0, ...Object.values(positions).map((p) => p.x)) + HGAP;
  const maxY = Math.max(0, ...Object.values(positions).map((p) => p.y)) + VGAP;
  svg.setAttribute("width", maxX + 40);
  svg.setAttribute("height", maxY);
  svg.setAttribute("viewBox", `-20 0 ${maxX + 40} ${maxY}`);

  // edges first so nodes draw on top
  Object.entries(nodes).forEach(([id, node]) => {
    const p = positions[id];
    if (!p) return;
    [node.left, node.right].forEach((childId) => {
      const cp = childId && positions[childId];
      if (!cp) return;
      const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("x1", p.x); line.setAttribute("y1", p.y);
      line.setAttribute("x2", cp.x); line.setAttribute("y2", cp.y);
      line.setAttribute("stroke", "var(--box-border)");
      line.setAttribute("stroke-width", "2");
      svg.appendChild(line);
    });
  });

  Object.entries(nodes).forEach(([id, node]) => {
    const p = positions[id];
    if (!p) return;
    const tag = highlights[id];
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", p.x); circle.setAttribute("cy", p.y); circle.setAttribute("r", R);
    circle.setAttribute("class", "box" + (tag ? ` tag-${tag}` : ""));
    svg.appendChild(circle);

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", p.x); text.setAttribute("y", p.y + 5);
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("font-size", "13"); text.setAttribute("font-weight", "700");
    text.setAttribute("fill", "var(--text)");
    text.textContent = node.value;
    svg.appendChild(text);

    const flags = flagsByNode[id];
    if (flags) {
      const flagText = document.createElementNS("http://www.w3.org/2000/svg", "text");
      flagText.setAttribute("x", p.x); flagText.setAttribute("y", p.y - R - 6);
      flagText.setAttribute("text-anchor", "middle");
      flagText.setAttribute("font-size", "10"); flagText.setAttribute("fill", "var(--accent)");
      flagText.textContent = flags.join(", ");
      svg.appendChild(flagText);
    }
  });

  stageBody.innerHTML = "";
  stageBody.appendChild(svg);
}
```

Note SVG shapes use the `class` attribute directly (`circle.setAttribute("class", ...)`)
rather than `className`, since SVG elements need `setAttribute` for classes
to apply CSS — the existing `.box`/`.tag-*` rules already work on `<circle>`
because they target `fill`/`stroke` via CSS custom properties, not
element-type-specific properties.

## Graph

**Step shape:** pass `graph` as `{"nodes": [...], "edges": [...]}`, with
fixed or precomputed positions so the layout doesn't jump between steps:

```python
tracer.step(
    message="visiting B, marking A->B as explored",
    line=15,
    highlights={"B": "visiting", "A": "sorted"},
    graph={
        "nodes": [
            {"id": "A", "value": "A", "x": 40,  "y": 40},
            {"id": "B", "value": "B", "x": 160, "y": 40},
            {"id": "C", "value": "C", "x": 100, "y": 140},
        ],
        "edges": [{"from": "A", "to": "B"}, {"from": "A", "to": "C"}],
    },
)
```

Compute `x`/`y` once up front (e.g. `networkx.spring_layout` scaled to
pixel coordinates, or a hand-picked layout for a small example graph) and
reuse the same coordinates in every step — recomputing layout per-step
makes nodes jitter around, which is disorienting rather than informative.

**Renderer:**

```javascript
function renderGraphStage(step) {
  const nodes = (step.graph && step.graph.nodes) || [];
  const edges = (step.graph && step.graph.edges) || [];
  const highlights = step.highlights || {};
  const R = 20;

  const byId = Object.fromEntries(nodes.map((n) => [n.id, n]));
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  const maxX = Math.max(0, ...nodes.map((n) => n.x)) + 40;
  const maxY = Math.max(0, ...nodes.map((n) => n.y)) + 40;
  svg.setAttribute("width", maxX);
  svg.setAttribute("height", maxY);

  edges.forEach((e) => {
    const a = byId[e.from], b = byId[e.to];
    if (!a || !b) return;
    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", a.x); line.setAttribute("y1", a.y);
    line.setAttribute("x2", b.x); line.setAttribute("y2", b.y);
    line.setAttribute("stroke", "var(--box-border)");
    line.setAttribute("stroke-width", "2");
    svg.appendChild(line);
  });

  nodes.forEach((n) => {
    const tag = highlights[n.id];
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", n.x); circle.setAttribute("cy", n.y); circle.setAttribute("r", R);
    circle.setAttribute("class", "box" + (tag ? ` tag-${tag}` : ""));
    svg.appendChild(circle);

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", n.x); text.setAttribute("y", n.y + 5);
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("font-size", "13"); text.setAttribute("font-weight", "700");
    text.setAttribute("fill", "var(--text)");
    text.textContent = n.value;
    svg.appendChild(text);
  });

  stageBody.innerHTML = "";
  stageBody.appendChild(svg);
}
```

## Linked list

**Step shape:** pass `linked_list` as an ordered array of nodes (order =
current traversal order from head, so it naturally reflects reversals
mid-algorithm):

```python
tracer.step(
    message="prev=None, cur=1, advancing: reversing cur.next to point at prev",
    line=9,
    highlights={"1": "visiting"},
    pointers={"cur": "1", "prev": "None"},
    linked_list=[{"id": "1", "value": 1}, {"id": "2", "value": 2}, {"id": "3", "value": 3}],
)
```

**Renderer** — this is just the array renderer with arrows between boxes
instead of index labels:

```javascript
function renderLinkedListStage(step) {
  const nodes = step.linked_list || [];
  const highlights = step.highlights || {};
  const pointers = step.pointers || {};
  const flagsById = {};
  Object.entries(pointers).forEach(([label, id]) => {
    (flagsById[id] = flagsById[id] || []).push(label);
  });

  const row = document.createElement("div");
  row.className = "stage-row";
  nodes.forEach((node, i) => {
    const cell = document.createElement("div");
    cell.className = "cell";

    const flags = flagsById[node.id];
    if (flags) {
      const flagsEl = document.createElement("div");
      flagsEl.className = "flags";
      flags.forEach((label) => {
        const f = document.createElement("div");
        f.className = "flag";
        f.textContent = label;
        flagsEl.appendChild(f);
      });
      cell.appendChild(flagsEl);
    }

    const box = document.createElement("div");
    const tag = highlights[node.id];
    box.className = "box" + (tag ? ` tag-${tag}` : "");
    box.textContent = node.value;
    cell.appendChild(box);
    row.appendChild(cell);

    if (i < nodes.length - 1) {
      const arrow = document.createElement("div");
      arrow.textContent = "→";
      arrow.style.alignSelf = "center";
      arrow.style.color = "var(--text-dim)";
      arrow.style.fontSize = "1.2rem";
      row.appendChild(arrow);
    }
  });
  stageBody.innerHTML = "";
  stageBody.appendChild(row);
}
```

Add `if (DATA.structure === "linked_list") return renderLinkedListStage(step);`
to the dispatcher, same as tree/graph.
