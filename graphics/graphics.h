/* Graphics library for OLED displays. Treats each pixel as a bit in a framebuffer ordered by rows */

#ifndef GRAPHICS_H
#define GRAPHICS_H

#include <stdint.h>
#include <pico/stdlib.h>

typedef enum {
    GRAPHICS_COLOUR_BLACK = 0,
    GRAPHICS_COLOUR_WHITE = 1
} graphics_colour_t;

#define GRAPHICS_OK 0
#define GRAPHICS_ERROR_OUT_OF_BOUNDS -1

typedef struct {
    uint8_t *framebuff;
    uint16_t width;
    uint16_t height;
    bool fill_on;
    bool stroke_on;
    graphics_colour_t fill_colour;
    graphics_colour_t stroke_colour;
} graphics_t;

void graphics_init(graphics_t *const graphics, uint8_t *framebuff, uint16_t width, uint16_t height);
void graphics_clear(graphics_t *const graphics);
int graphics_draw_pixel(graphics_t *const graphics, int x, int y, bool on);
int graphics_draw_line(graphics_t *const graphics, int x0, int y0, int x1, int y1);
int graphics_draw_rectangle(graphics_t *const graphics, int x0, int y0, int w, int h);
int graphics_draw_circle(graphics_t *const graphics, int x0, int y0, int radius);
int graphics_draw_ellipse(graphics_t *const graphics, int x0, int y0, int radius_x, int radius_y);
int graphics_draw_triangle(graphics_t *const graphics, int x0, int y0, int x1, int y1, int x2, int y2);
void graphics_no_fill(graphics_t *const graphics);
void graphics_fill(graphics_t *const graphics, graphics_colour_t);
void graphics_no_stroke(graphics_t *const graphics);
void graphics_stroke(graphics_t *const graphics, graphics_colour_t);

// TODO Polygon
// int graphics_draw_poly();

#endif