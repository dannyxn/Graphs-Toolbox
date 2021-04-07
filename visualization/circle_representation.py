import math

import networkx as nx
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


class CircleRepresentation:
    def __init__(self):
        self.size_x, self.size_y = 800, 800  # image size
        self.radius = 350  # layout circle radius
        self.border = 20
        self.node_radius = 20  # radius of node circle
        self.im = Image.new('RGB', (self.size_x, self.size_y), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.im)
        self.adj_list = []
        self.angle = 0

    def init(self, adj_list: list) -> None:
        assert len(adj_list) > 0
        node_size_scale = len(self.adj_list) % 20
        if node_size_scale != 0:
            self.node_radius /= node_size_scale
        self.adj_list = adj_list
        self.angle = 2 * math.pi / len(self.adj_list)

    def display(self, adj_list: list) -> None:
        self.init(adj_list)
        self.draw_nodes()
        self.draw_edges()
        self.draw_labels()
        self.im.show()

    def draw_nodes(self) -> None:
        for node_index in range(len(self.adj_list)):
            x_pos, y_pos = self.calculate_positions(node_index, self.angle)
            self.draw.ellipse([x_pos - self.node_radius, y_pos - self.node_radius,
                               x_pos + self.node_radius, y_pos + self.node_radius], outline='black', fill='red')

    def draw_edges(self):
        angle = 2 * math.pi / len(self.adj_list)
        for node_index in range(len(self.adj_list)):
            self.draw_edge(node_index, self.adj_list[node_index], angle)

    def draw_labels(self):
        angle = 2 * math.pi / len(self.adj_list)
        for node_index in range(len(self.adj_list)):
            x_pos, y_pos = self.calculate_positions(node_index, angle)
            self.draw.text([x_pos + math.cos(angle), y_pos + math.sin(angle)],
                           str(1 + node_index), fill="white")

    def draw_edge(self, node_index: int, connections: list, angle: float) -> None:
        for other_node_index in connections:
            x_pos, y_pos = self.calculate_positions(node_index, angle)
            other_x_pos, other_y_pos = self.calculate_positions(other_node_index, angle)
            self.draw.line([x_pos, y_pos, other_x_pos, other_y_pos], fill=(0, 0, 0))

    def calculate_positions(self, node_index, angle) -> tuple:
        x_pos = self.radius * (1 - math.cos(angle * node_index)) + self.border
        y_pos = self.radius * (1 - math.sin(angle * node_index)) + self.border
        return x_pos, y_pos



