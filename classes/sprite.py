from pygame import Surface
import pygame.image
from typing import Optional


class Sprite:
    # def __init__(self, image: Surface, height) -> None:
    #     self.image = image
    #     self.pos = image.get_rect().move(0, height)
    #     pass

    image: Surface
    image_path: str  # FIXME implement path
    pos_x: float
    pos_y: float
    height: float
    width: float

    def __init__(
        self,
        asset_path: str,
        pos: tuple[float, float],
        *,
        size: Optional[tuple[float, float]] = None,
        scale_factor: Optional[float] = None,
    ) -> None:
        self.image_path = asset_path
        self.pos_x, self.pos_y = pos
        temp_img = pygame.image.load(self.image_path).convert_alpha()
        if size:
            self.width, self.height = size
            self.image = pygame.transform.smoothscale(
                temp_img, (self.width, self.height)
            )
        elif scale_factor:
            self.image = pygame.transform.smoothscale_by(temp_img, scale_factor)
            _, _, self.width, self.height = self.image.get_rect()
        else:
            raise ValueError(
                "Needs either a size or a scale, you have provided none of those two."
            )
        color_image = pygame.Surface(self.image.get_size()).convert_alpha()
        color_image.fill

    @property
    def pos_x_end(self) -> float:
        return self.pos_x + self.width

    @property
    def pos_y_end(self) -> float:
        return self.pos_y + self.height

    @property
    def bounding_box(self) -> pygame.Rect:
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def simulate_move(self, movement: pygame.Vector2) -> pygame.Rect:
        """Returns True if movement was possible and False if not."""
        simulated_rect = self.bounding_box
        simulated_rect.x += movement.x
        simulated_rect.y += movement.y
        return simulated_rect

    def move(self, movement: pygame.Vector2, borders: pygame.Rect) -> bool:
        """Returns True if movement was possible and False if not."""
        simulated_rect = self.simulate_move(movement)
        if borders.contains(simulated_rect):
            self.pos_x += movement.x
            self.pos_y += movement.y
            return True
        return False

    def draw(self, window: Surface):
        window.blit(self.image, (self.pos_x, self.pos_y))
