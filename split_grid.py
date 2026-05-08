#!/usr/bin/env python3
"""Split a storyboard grid image into individual panels.

Usage:
  Manual mode:  python3 split_grid.py <image> <rows> <cols> [output_dir] [prefix]
  Auto mode:    python3 split_grid.py <image> --auto [output_dir] [prefix]
                python3 split_grid.py <image> -a [output_dir] [prefix]
"""
import sys
import os
from PIL import Image

# ──────────────────────────────────────────
# Auto-detection
# ──────────────────────────────────────────

def auto_detect_grid(image_path, edge_margin=8, std_threshold=15, max_border_width=20):
    """
    Scan the image for internal border lines (uniform-colour strips
    between panels) and return (rows, cols).

    Only internal dividers are counted — edges of the image are ignored.
    """
    img = Image.open(image_path).convert('L')
    pixels = img.load()
    w, h = img.size

    def row_stats(y):
        vals = [pixels[x, y] for x in range(w)]
        mean = sum(vals) / len(vals)
        var = sum((v - mean) ** 2 for v in vals) / len(vals)
        return mean, var ** 0.5

    def col_stats(x):
        vals = [pixels[x, y] for y in range(h)]
        mean = sum(vals) / len(vals)
        var = sum((v - mean) ** 2 for v in vals) / len(vals)
        return mean, var ** 0.5

    def count_borders(total, get_stats, label):
        border_flags = []
        for i in range(total):
            _, s = get_stats(i)
            border_flags.append(s < std_threshold)

        groups = []
        in_group = False
        start = 0
        for i in range(total):
            if border_flags[i] and not in_group:
                start = i
                in_group = True
            elif not border_flags[i] and in_group:
                groups.append((start, i - 1))
                in_group = False
        if in_group:
            groups.append((start, total - 1))

        # Keep only internal borders (not touching the image edges)
        internal = [
            (s, e)
            for s, e in groups
            if s > edge_margin and e < total - edge_margin and 2 <= (e - s + 1) <= max_border_width
        ]

        print(f"   {label}: found {len(internal)} internal divider(s)")
        for s, e in internal:
            print(f"      {label.lower()} {s}–{e}  ({e - s + 1} px)")

        return len(internal)

    print(f"🔍 Auto-detecting grid from: {image_path}  ({w}×{h})")
    h_divs = count_borders(h, row_stats, "Horizontal")
    v_divs = count_borders(w, col_stats, "Vertical")

    rows = h_divs + 1
    cols = v_divs + 1
    print(f"   →  {rows} row(s) × {cols} col(s)  =  {rows * cols} panels")
    return rows, cols


# ──────────────────────────────────────────
# Core splitter
# ──────────────────────────────────────────

def split_grid(image_path, rows, cols, output_dir=None, prefix="panel"):
    """
    Split a grid image into rows x cols panels.

    Args:
        image_path: Path to the grid image
        rows: Number of rows in the grid
        cols: Number of columns in the grid
        output_dir: Directory for output panels (default: same dir as input)
        prefix: Output filename prefix (default: "panel")

    Returns:
        List of output file paths
    """
    img = Image.open(image_path)
    width, height = img.size

    panel_w = width // cols
    panel_h = height // rows

    if output_dir is None:
        output_dir = os.path.dirname(image_path) or "."
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(image_path))[0]
    out_dir = os.path.join(output_dir, f"{base_name}_panels")
    os.makedirs(out_dir, exist_ok=True)

    outputs = []
    panel_num = 1
    for row in range(rows):
        for col in range(cols):
            left = col * panel_w
            upper = row * panel_h
            right = left + panel_w
            lower = upper + panel_h

            panel = img.crop((left, upper, right, lower))
            out_path = os.path.join(out_dir, f"{prefix}_{panel_num:02d}.png")
            panel.save(out_path, "PNG")
            outputs.append(out_path)
            panel_num += 1

    # Summary file
    summary_path = os.path.join(out_dir, "mapping.txt")
    with open(summary_path, "w") as f:
        f.write(f"Source: {image_path}\n")
        f.write(f"Grid: {rows}x{cols} ({rows * cols} panels)\n")
        f.write(f"Panel size: {panel_w}x{panel_h}\n")
        f.write(f"\nPanels:\n")
        for i, p in enumerate(outputs, 1):
            f.write(f"  Panel {i}: {os.path.basename(p)}\n")

    print(f"✅ Split {image_path} into {rows * cols} panels ({rows}x{cols})")
    print(f"   Output: {out_dir}/")
    for i, p in enumerate(outputs, 1):
        print(f"   [{i}] {os.path.basename(p)}")

    return outputs


# ──────────────────────────────────────────
# CLI
# ──────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("Examples:")
        print("  python3 split_grid.py storyboard.png 3 2")
        print("  python3 split_grid.py storyboard.png --auto")
        print("  python3 split_grid.py storyboard.png -a ./output scene")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        sys.exit(1)

    # ── Auto mode ──────────────────────
    if "--auto" in sys.argv or "-a" in sys.argv:
        # Extract optional [output_dir] [prefix] from remaining args
        flag_idx = sys.argv.index("--auto") if "--auto" in sys.argv else sys.argv.index("-a")
        extra = sys.argv[flag_idx + 1:]  # args after --auto
        output_dir = extra[0] if len(extra) > 0 else None
        prefix = extra[1] if len(extra) > 1 else "panel"

        rows, cols = auto_detect_grid(image_path)
        split_grid(image_path, rows, cols, output_dir, prefix)

    # ── Manual mode ────────────────────
    else:
        if len(sys.argv) < 4:
            print("❌ Manual mode needs <rows> <cols>")
            print("   python3 split_grid.py <image> <rows> <cols> [output_dir] [prefix]")
            print("   Or use --auto for automatic detection.")
            sys.exit(1)

        rows = int(sys.argv[2])
        cols = int(sys.argv[3])
        output_dir = sys.argv[4] if len(sys.argv) > 4 else None
        prefix = sys.argv[5] if len(sys.argv) > 5 else "panel"

        split_grid(image_path, rows, cols, output_dir, prefix)
