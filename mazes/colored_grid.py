from mazes.distance_grid import DistanceGrid
import svgwrite as sw

class ColoredGrid(DistanceGrid):
    @property
    def distances(self):
        return super().distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances
        _farthest, self.max = distances.max

    def background_color_for(self, cell):
        if distance := self._distances[cell]:
            intensity = self.max - distance
            dark = round(255 * intensity / self.max)
            bright = 128 + round(127 * intensity / self.max)
            return sw.rgb(dark, dark, bright)
        
        return None
