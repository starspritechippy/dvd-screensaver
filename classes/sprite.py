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

    def draw(self, window: Surface):
        window.blit(self.image, (self.pos_x, self.pos_y))
