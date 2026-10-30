# Fractal Art Generator

An interactive Sierpinski Carpet generator built with [CMU Graphics](https://pypi.org/project/cmu-graphics/). Click anywhere on the canvas to recurse deeper into the fractal, or click a color swatch to change its fill color.

## How it works

The Sierpinski Carpet is drawn recursively: each square is divided into a 3×3 grid, the center cell is left empty (shown here as a small white square), and the same pattern is then redrawn into each of the 8 surrounding cells at one-third the size. The recursion stops once it reaches the requested depth.

Each square also gets a border whose thickness scales with the square's size, so the artwork stays visually consistent no matter how deep the recursion goes.

## Features

- Recursive Sierpinski Carpet rendering at adjustable depth
- Click-to-recurse: clicking anywhere outside the color swatches increases the fractal depth by one level
- 6 selectable colors: crimson, dark orange, gold, medium sea green, dodger blue, and dark orchid
- Proportional borders that scale with square size, so detail stays clean at every depth
- Shape count raised to 10,000 to support several levels of recursion without hitting CMU Graphics' default limit

## Requirements

- Python 3.10+
- [cmu_graphics](https://pypi.org/project/cmu-graphics/)

## Installation

```bash
pip install cmu_graphics
```

> **macOS users:** `cmu_graphics` depends on `pycairo`, which needs Xcode Command Line Tools and Homebrew's `cairo`/`pkg-config` installed first:
> ```bash
> xcode-select --install
> brew install pkg-config cairo
> pip install cmu_graphics
> ```

## Usage

Clone the repo and run the script directly (not through a debugger):

```bash
git clone https://github.com/<your-username>/fractal-art-generator.git
cd fractal-art-generator
python3 fractal-art.py
```

A 400×400 window will open showing the fractal at depth 1, with six color swatches along the bottom.

## Controls

| Action | Effect |
|---|---|
| Click a color swatch | Changes the fractal's fill color |
| Click anywhere else on the canvas | Increases recursion depth by 1 |

> Higher depths produce exponentially more shapes — if you click many times in a row, you may hit the `setMaxShapeCount` limit. Increase it in `onAppStart` if needed.

## Project structure

```
Fractal Art Generator/
└── fractal-art.py   # Main script: fractal logic, rendering, and event handlers
```

## Acknowledgments

Built with the [CMU Graphics](https://academy.cs.cmu.edu/desktop) library from CMU CS Academy.

## License

MIT — feel free to use, modify, and share.
