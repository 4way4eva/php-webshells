#!/usr/bin/env python3
"""
Yield Visualization Script
Creates an image with yield calculations and compounding factors
"""

from datetime import datetime, UTC
from PIL import Image, ImageDraw
import math

# Constants
CITY = "Zion City Atlantic"
REGION = "Rich of the Arctic"
GLYPH = "⟟⟁⟠"
STAMP = f"{CITY} | {REGION}\nGlyph: {GLYPH}\nDate: {datetime.now(UTC)}"

# Calculate π₄ (pi to the power of 4)
PI_4 = math.pi ** 4

# Initial yield
INITIAL_YIELD = 28900000

# Generate yield table data
def generate_yield_table():
    """Generate yield table with compounding factors"""
    table_data = []
    
    # Header
    table_data.append("Time (sec),Yield ($),Compounding Factor,Total Yield ($)")
    
    # Initial entry (t=0)
    table_data.append(f"0,{INITIAL_YIELD},1,{INITIAL_YIELD}")
    
    # Entry at t=1 with formula representation
    table_data.append(f"1,\"{INITIAL_YIELD} * π₄^(1/86400)\",\"π₄^(1/86400)\",...")
    
    # Final entry at t=86400 (one day)
    final_yield = int(INITIAL_YIELD * PI_4)
    table_data.append(f"86400,\"{INITIAL_YIELD} * π₄\",\"π₄\",{final_yield}")
    
    table_data.append("// ... Extend as needed")
    
    return table_data

# Create the image
def create_image():
    """Create a blank image with dark blue background"""
    # Make a blank image
    img = Image.new("RGB", (800, 400), color=(30, 30, 60))  # dark blue background
    draw = ImageDraw.Draw(img)
    
    return img, draw

def main():
    """Main function to generate yield table and image"""
    # Print the stamp
    print(STAMP)
    print()
    
    # Generate and print yield table
    yield_table = generate_yield_table()
    for row in yield_table:
        print(row)
    
    print()
    print(f"π₄ value: {PI_4}")
    print(f"Final yield after 86400 seconds: ${int(INITIAL_YIELD * PI_4):,}")
    
    # Create the image
    img, draw = create_image()
    
    # Save the image
    output_filename = "yield_visualization.png"
    img.save(output_filename)
    print(f"\nImage saved as: {output_filename}")

if __name__ == "__main__":
    main()
