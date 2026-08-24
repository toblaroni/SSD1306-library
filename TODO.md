
# SSD1306 + Graphics Library Roadmap

**Goal:** Render a rotating (or static) wireframe cube on the SSD1306 OLED.

---

## Phase 1 – SSD1306 Driver

### Core Driver
- [x] Initialise the SSD1306
- [x] Support configurable display width and height
- [x] Support configurable I²C address
- [x] Implement framebuffer
- [x] Upload framebuffer to display
- [x] Clear display
- [x] Fill display
- [x] Display on/off
- [x] Contrast control

### Transport Layer
- [ ] Separate transport from driver logic
- [ ] I²C transport implementation
- [ ] SPI transport implementation
- [ ] Hardware abstraction interface (HAL)

### Documentation
- [ ] README
- [ ] Quick start example
- [ ] API documentation
- [ ] Example projects

---

# Graphics Library

## Core Drawing

### Pixels
- [x] Draw pixel
- [x] Clear pixel

### Lines
- [x] Bresenham line drawing
- [x] Horizontal line optimisation
- [ ] Vertical line optimisation

### Shapes
- [x] Rectangle
- [x] Filled rectangle
- [x] Circle
- [x] Filled circle
- [x] Triangle
- [x] Filled triangle
- [ ] Polygon
- [ ] Ellipse

### Rendering 
- [ ] Stroke Width

### Text
- [ ] Bitmap font support
- [ ] Character rendering
- [ ] String rendering
- [ ] Text alignment helpers

### Utility
- [ ] Clipping
- [ ] Viewport support
- [ ] Basic colour abstraction (future-proof for non-monochrome displays)

---

# Mathematics

## Vector Types
- [ ] Vec2
- [ ] Vec3
- [ ] Vec4 ?

## Matrix Types
- [ ] 3×3 matrix
- [ ] 4×4 matrix

## Matrix Operations
- [ ] Matrix multiplication
- [ ] Matrix × vector
- [ ] Identity matrix
- [ ] Translation
- [ ] Scaling
- [ ] Rotation X
- [ ] Rotation Y
- [ ] Rotation Z

---

# 3D Rendering

## Projection
- [ ] Orthographic projection
- [ ] Perspective projection

## Rendering Pipeline
- [ ] Transform vertices
- [ ] Project to screen
- [ ] Draw edges
- [ ] Back-face culling (optional)

---

# Demo

## Wireframe Cube
- [ ] Define cube vertices
- [ ] Define cube edges
- [ ] Render static cube
- [ ] Rotate around X
- [ ] Rotate around Y
- [ ] Rotate around Z
- [ ] Smooth animation
- [ ] Maintain stable frame rate

---

# Polish

## Testing
- [ ] Unit tests for drawing algorithms
- [ ] Verify framebuffer output
- [ ] Edge-case testing

## Build System
- [ ] CMake support
- [ ] Examples build independently

## CI
- [ ] GitHub Actions build
- [ ] Run tests automatically

## Repository
- [ ] MIT License
- [ ] CHANGELOG
- [ ] CONTRIBUTING guide
- [ ] Semantic versioning

---

# Milestone

## 🎯 Version 1.0

- [ ] SSD1306 driver is portable
- [ ] Graphics library is display-agnostic
- [ ] All primitive drawing functions implemented
- [ ] Documentation complete
- [ ] Examples included
- [ ] **Render a rotating wireframe cube on the OLED**

> **Project Complete Criteria:** The graphics library is considered v1.0 complete when it can render a smooth rotating wireframe cube on an SSD1306 display using its own math and rendering pipeline.