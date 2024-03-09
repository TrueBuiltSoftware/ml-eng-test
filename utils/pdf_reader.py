import fitz
from shapely import Point, LineString, box, Polygon
from utils.types import TextDict


def process_points(item):
  points = []
  item_type = item[0]
  if item_type == "qu":
    for idx, i in enumerate(item):
      if idx == 1:
        res = list(i)
        for p in res:
          points.append(Point([p[1], p[0]]))
        return points, item_type
    # return
  if item_type == "re":
    for idx, i in enumerate(item):
      if idx == 1:
        res = [i[p : p + 2] for p in range(0, len(i), 2)]
        for p in res:
          points.append(Point([p[1], p[0]]))
    return points, item_type
  try:
    for idx, i in enumerate(item):
      if idx > 0:
        res = [i[p : p + 2] for p in range(0, len(i), 2)]
        for p in res:
          points.append(Point([p[1], p[0]]))
    return points, item_type
  except Exception as e:
    print(e)
    print(item)
    print(points)
    raise Exception

class PdfReader:
    def __init__(self, path: str):
        self.path = path
        self.doc = fitz.open(path)

    def get_page(self, page_number: int) -> "PdfPage":
        """Gets a page from the pdf.

        Args:
            page_number (int): The page number to get.

        Returns:
            PdfPage: The page object.
        """
        return PdfPage(self.doc[page_number])


class PdfPage:
    def __init__(self, page: fitz.fitz.Page):
        self.page = page

    
    def get_image(self, quality=100, dpi=100) -> bytes:
        """Generates a thumbnail of the page as a bytes object.

        Args:
            quality (int): The quality of the thumbnail. Default is 100.
            dpi (int): The dpi of the thumbnail. Default is 100. (72 is the default dpi of a pdf page)
        """
        scale = dpi / 72
        mat = fitz.Matrix(scale, scale)
        pix = self.page.get_pixmap(alpha=False, matrix=mat)
        img = pix.tobytes(output="jpg", jpg_quality=quality)
        return img
    
    def get_text(self) -> str:
        """Gets the full text from the page."""
        return self.page.get_text()
    
    def get_text_dict(self):
        """Gets the text from the page as a dictionary."""
        p = self.page.get_textpage().extractDICT()


        return TextDict(**{**p, "blocks": list(filter(lambda x: x["type"] == 0, p["blocks"]))}) 
    
    def get_drawings(self):
        """Gets the drawings from the page."""
        raw_paths = self.page.get_cdrawings()

        paths = []
        for path in raw_paths:
            base = {**path}
            del base["items"]
            for item in path["items"]:
                points, item_type = process_points(item)
                geometry = None
                if item_type == "l":
                    geometry = LineString(points)

                if item_type == "c":
                    geometry = LineString(points)

                if item_type == "qu":
                    geometry = Polygon(points)

                if item_type == "re":
                    min, max = points
                    geometry = box(min.x, min.y, max.x, max.y)
                if geometry is not None:
                    data = {
                        **base,
                        "geometry": geometry,
                        "type": item_type,
                    }
                paths.append(data)
        return paths
            