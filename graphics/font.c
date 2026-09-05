#include "font.h"
#include "determination.h"

#include <stdint.h>

int graphics_draw_char(graphics_t *const gfx, char c, int x, int y) {
    // Get the index of the character
    size_t index = c - FONT_FIRST_CHAR;


    for (int j = 0; j < FONT_CHAR_WIDTH; ++j) {
        uint8_t col_index = font[index * FONT_CHAR_WIDTH + j];
        for (int i = 0; i < FONT_CHAR_HEIGHT; ++i) {
            if (col_index & (1<<i)) {
                graphics_draw_pixel(
                    gfx, 
                    x+j,
                    y+i,
                    gfx->fill_on
                );
            }
        }
    }

    return GRAPHICS_OK;
}

