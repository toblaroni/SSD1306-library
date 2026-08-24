#include <math.h>
#include "driver/SSD1306_driver.h"
#include "graphics/graphics.h"

#define OLED_ADDR 0x3D
#define GPIO_SDA 0
#define GPIO_SCL 1

int main() {

    stdio_init_all();
    i2c_init(i2c0, 400 * 1000); 
    sleep_ms(500);

    SSD1306_t screen;
    graphics_t gfx;

    // Initialise the OLED
    int res = SSD1306_init(&screen, i2c0, OLED_ADDR, GPIO_SDA, GPIO_SCL, 128, 64);

    switch (res) {
        case SSD1306_OK:
            printf("Initialised successfully\n");
            break;
        case SSD1306_ERROR_BAD_ADDRESS:
            printf("Initialisation failed. Bad address... :(\n");
            break;
        case SSD1306_ERROR_TIMEOUT:
            printf("Initialisation failed. Timeout... :(\n");
            break;
    }

    graphics_init(&gfx, screen.framebuff, screen.width, screen.height);

    graphics_no_stroke(&gfx);
    graphics_fill(&gfx, GRAPHICS_COLOUR_WHITE);

    int framecount = 0;
    while (true)
    {
        graphics_clear(&gfx);

        // Generate three random vertices
        int x0 = rand() % screen.width;
        int y0 = rand() % screen.height;

        int x1 = rand() % screen.width;
        int y1 = rand() % screen.height;

        int x2 = rand() % screen.width;
        int y2 = rand() % screen.height;


        graphics_draw_triangle(
            &gfx,
            x0, y0,
            x1, y1,
            x2, y2
        );

        printf(
            "v1: (%i, %i), v2: (%i, %i), v3: (%i, %i)\n",
            x0, y0, x1, y1, x2, y2
        );

        SSD1306_update(&screen);

        sleep_ms(500);
    }

    return 0;
}
