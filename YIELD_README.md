# Yield Visualization Script

This Python script generates a yield table with compounding factors and creates a visualization image.

## Features

- Defines location and glyph constants
- Generates a CSV-formatted yield table showing:
  - Time progression (0 to 86400 seconds / 1 day)
  - Yield values with π₄ (pi to the power of 4) compounding
  - Compounding factors
  - Total yield calculations
- Creates a blank 800x400 PNG image with dark blue background

## Requirements

```bash
pip install Pillow
```

## Usage

```bash
python3 yield_visualization.py
```

## Output

The script will:
1. Print a timestamp with location and glyph information
2. Display a yield table in CSV format
3. Show π₄ value and final yield calculation
4. Create `yield_visualization.png` (800x400 pixels, dark blue background)

## Constants

- **CITY**: "Zion City Atlantic"
- **REGION**: "Rich of the Arctic"
- **GLYPH**: "⟟⟁⟠"
- **INITIAL_YIELD**: $28,900,000
- **PI_4**: π⁴ ≈ 97.409

## Example Output

```
Zion City Atlantic | Rich of the Arctic
Glyph: ⟟⟁⟠
Date: 2025-11-20 06:10:29.514935+00:00

Time (sec),Yield ($),Compounding Factor,Total Yield ($)
0,28900000,1,28900000
1,"28900000 * π₄^(1/86400)","π₄^(1/86400)",...
86400,"28900000 * π₄","π₄",2815122730
// ... Extend as needed

π₄ value: 97.40909103400242
Final yield after 86400 seconds: $2,815,122,730

Image saved as: yield_visualization.png
```
