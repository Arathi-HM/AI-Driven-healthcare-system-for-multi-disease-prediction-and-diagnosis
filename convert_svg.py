#!/usr/bin/env python3
# Convert SVG to PNG and create enhanced UML diagram
import subprocess
import sys

try:
    # Try using cairosvg if available
    from cairosvg import svg2png
    svg2png(url='UML_UseCase_Diagram.svg', write_to='UML_UseCase_Diagram.png', dpi=300)
    print("✓ Created PNG using cairosvg")
except ImportError:
    try:
        # Try PIL/Pillow
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (1400, 1000), color='white')
        # This would require complex drawing logic - fallback instead
        raise ImportError("Need alternative approach")
    except Exception as e:
        print(f"Note: {e}")
        print("SVG file has been created successfully at: UML_UseCase_Diagram.svg")
        print("You can open it in any web browser or convert it using online tools.")
