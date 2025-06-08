from typing import Dict, List, Any
from PIL import Image, ImageDraw, ImageFont
from point import Point


def grid_dict_to_list(grid: Dict[tuple, Point], size: int) -> list[tuple]:
    # return [[Point() if not tuple([r,c]) in grid else grid[tuple([r,c])] for r in range(size)] for c in range(size)]
    return [tuple([r, c]) for r in range(size) for c in range(size)]


def visualise_zip(
    grid: Dict[tuple, Point],
    size: int,
    solution: List[tuple],
    path: str,
    solved: bool = True,
    show: bool = False,
) -> None:
    # --- drawing setup ----------------------------------------------

    cell_px: int = 50
    img_px: int = size * cell_px
    img: Image.Image = Image.new("RGB", (img_px, img_px), "white")
    draw: ImageDraw.ImageDraw = ImageDraw.Draw(img)
    font: Any = ImageFont.load_default()

    # --- draw cell borders ------------------------------------------

    for (y, x), pt in grid.items():
        px, py = x * cell_px, y * cell_px
        w: float = 4  # border line width
        if pt.left:
            draw.line([(px, py), (px, py + cell_px)], fill="black", width=w)
        if pt.top:
            draw.line([(px, py), (px + cell_px, py)], fill="black", width=w)
        if pt.right:
            draw.line(
                [(px + cell_px, py), (px + cell_px, py + cell_px)],
                fill="black",
                width=w,
            )
        if pt.bottom:
            draw.line(
                [(px, py + cell_px), (px + cell_px, py + cell_px)],
                fill="black",
                width=w,
            )

    # --- draw all grid lines (light) --------------------------------

    for i in range(size + 1):
        # verticals
        draw.line([(i * cell_px, 0), (i * cell_px, img_px)], fill="#ddd")
        # horizontals
        draw.line([(0, i * cell_px), (img_px, i * cell_px)], fill="#ddd")

    # --- draw the path ------------------------------------------------

    # convert grid coords to pixel centers
    pix_centers: List[Tuple[float, float]] = [
        ((x + 0.5) * cell_px, (y + 0.5) * cell_px) for y, x in solution
    ]
    if solved:
        draw.line(pix_centers, fill="red", width=6, joint="curve")

    # --- draw cell values -------------------------------------------
    r: int = 16
    # mark start/end
    x0, y0 = pix_centers[0]
    xn, yn = pix_centers[-1]
    for (y, x), pt in grid.items():
        if pt.value is not None:
            text: str = str(pt.value)
            # compute text width/height via textbbox
            bbox = draw.textbbox((0, 0), text, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
            cx: float = x * cell_px + (cell_px - w) / 2
            cy: float = y * cell_px + (cell_px - h) / 2
            xi: float = (x + 0.5) * cell_px
            yi: float = (y + 0.5) * cell_px
            fill: str = "black"
            if x0 == xi and y0 == yi:
                fill = "green"
            elif xn == xi and yn == yi:
                fill = "blue"
            draw.ellipse((xi - r, yi - r, xi + r, yi + r), fill=fill)
            draw.text((cx, cy - 8), text, fill="white", font=font)

    # --- show or save -----------------------------------------------

    if show:
        img.show()
    img.save(f"./data/{path}.png")  # or save to disk


if __name__ == "__main__":
    size: int = 3
    solution: List[tuple] = [
        (2, 0),
        (2, 1),
        (2, 2),
        (1, 2),
        (1, 1),
        (1, 0),
        (0, 0),
        (0, 1),
        (0, 2),
    ]
    grid: Dict[tuple, Point] = {
        (0, 1): Point(bottom=True),
        (0, 2): Point(value=2),
        (1, 1): Point(top=True, bottom=True),
        (2, 0): Point(value=1),
        (2, 1): Point(top=True),
    }
    visualise_zip(grid, size, solution, "solution")
