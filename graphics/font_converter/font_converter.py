#!/usr/bin/env python3

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CHAR_WIDTH = 6
CHAR_HEIGHT = 8

FIRST_CHAR = 32
LAST_CHAR = 126

def rasterize_char(font, char):
    """Return a glyph as 6 bytes, one byte per vertical column."""

    SCALE = 2

    large_width = CHAR_WIDTH * SCALE
    large_height = CHAR_HEIGHT * SCALE

    image = Image.new("L", (large_width, large_height), 0)
    draw = ImageDraw.Draw(image)

    bbox = draw.textbbox((0, 0), char, font=font)

    glyph_width = bbox[2] - bbox[0]
    glyph_height = bbox[3] - bbox[1]

    x = (large_width - glyph_width) // 2 - bbox[0]
    y = (large_height - glyph_height) // 2 - bbox[1]

    draw.text(
        (x, y),
        char,
        font=font,
        fill=255
    )

    image = image.resize(
        (CHAR_WIDTH, CHAR_HEIGHT),
        Image.Resampling.BOX
    )

    pixels = image.load()

    columns = []

    for x in range(CHAR_WIDTH):
        byte = 0

        for y in range(CHAR_HEIGHT):
            if pixels[x, y] >= 100:
                byte |= 1 << y

        columns.append(byte)

    return columns


def get_char_name(codepoint):
    """Return a readable name for a character."""

    char = chr(codepoint)

    if char == "'":
        return "\\'"
    elif char == "\\":
        return "\\\\"
    elif char == " ":
        return "SPACE"
    else:
        return char


def generate_font(ttf_path, output_base, font_size):

    output_base = Path(output_base)

    header_path = output_base.with_suffix(".h")
    source_path = output_base.with_suffix(".c")

    font = ImageFont.truetype(
        str(ttf_path),
        font_size * 8
    )

    # ---------------------------------------------------------
    # Generate .h
    # ---------------------------------------------------------

    guard = re.sub(r'\W', '_', output_base.stem.upper()) + "_H"

    with open(header_path, "w") as h:

        h.write("// Generated bitmap font\n")
        h.write("// Do not edit manually.\n\n")

        h.write(f"#ifndef {guard}\n")
        h.write(f"#define {guard}\n\n")

        h.write("#include <stdint.h>\n\n")

        h.write(f"#define FONT_FIRST_CHAR {FIRST_CHAR}\n")
        h.write(f"#define FONT_LAST_CHAR {LAST_CHAR}\n")
        h.write(f"#define FONT_CHAR_WIDTH {CHAR_WIDTH}\n")
        h.write(f"#define FONT_CHAR_HEIGHT {CHAR_HEIGHT}\n\n")

        h.write("extern const uint8_t font[];\n\n")

        h.write(f"#endif // {guard}\n")


    # ---------------------------------------------------------
    # Generate .c
    # ---------------------------------------------------------

    with open(source_path, "w") as c:

        c.write("// Generated bitmap font\n")
        c.write("// Do not edit manually.\n\n")

        c.write(f'#include "{header_path.name}"\n\n')

        c.write("const uint8_t font[] = {\n")

        for codepoint in range(FIRST_CHAR, LAST_CHAR + 1):

            char = chr(codepoint)
            name = get_char_name(codepoint)

            glyph = rasterize_char(font, char)

            c.write(
                f"    // U+{codepoint:04X} '{name}'\n"
            )

            c.write("    ")

            for i, byte in enumerate(glyph):

                c.write(f"0x{byte:02X}")

                if i < len(glyph) - 1:
                    c.write(", ")

            c.write(",\n")

        c.write("};\n")


    print(f"Generated {header_path}")
    print(f"Generated {source_path}")


def main():

    parser = argparse.ArgumentParser(
        description="Convert a TTF font into a 6x8 bitmap font."
    )

    parser.add_argument(
        "font",
        help="TTF font file"
    )

    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output filename base (default: TTF filename)"
    )

    parser.add_argument(
        "-s",
        "--size",
        type=int,
        default=8,
        help="Font size in pixels (default: 8)"
    )

    args = parser.parse_args()

    if args.output:
        output_base = Path(args.output)
    else:
        output_base = Path(args.font).with_suffix("")

    generate_font(
        Path(args.font),
        output_base,
        args.size
    )


if __name__ == "__main__":
    main()
