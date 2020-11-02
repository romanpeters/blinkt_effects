from base import EffectBase, Effect, VariableDelay
import random

class Thunder(EffectBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _custom_action(self):
        if random.randint(0, 15) == 1:
            self.add_overwrite(thunder_flash)

X__________ = (0, 0, 0)

raindrop_dripping = [
    [(0, 64, 255), X__________, X__________, X__________, X__________, X__________, X__________, X__________],
    [(VariableDelay(1, 10))],
    [(0, 4, 16), (0, 64, 255), X__________, X__________, X__________, X__________, X__________, X__________],
    [X__________, (0, 4, 16), (0, 64, 255), X__________, X__________, X__________, X__________, X__________],
    [X__________, X__________, (0, 4, 16), (0, 64, 255), X__________, X__________, X__________, X__________],
    [X__________, X__________, X__________, (0, 4, 16), (0, 64, 255), X__________, X__________, X__________],
    [X__________, X__________, X__________, X__________, (0, 4, 16), (0, 64, 255), X__________, X__________],
    [X__________, X__________, X__________, X__________, X__________, (0, 4, 16), (0, 64, 255), X__________],
    [X__________, X__________, X__________, X__________, X__________, X__________, (0, 4, 16), (0, 64, 255)],
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, (0, 4, 16)],
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, X__________],
    [(VariableDelay(0, 2))]
    ]

raindrop_falling = [
    [(0, 64, 255), X__________, X__________, X__________, X__________, X__________, X__________, X__________],
    [(0, 4, 16), (0, 64, 255), X__________, X__________, X__________, X__________, X__________, X__________],
    [X__________, (0, 4, 16), (0, 64, 255), X__________, X__________, X__________, X__________, X__________],
    [X__________, X__________, (0, 4, 16), (0, 64, 255), X__________, X__________, X__________, X__________],
    [X__________, X__________, X__________, (0, 4, 16), (0, 64, 255), X__________, X__________, X__________],
    [X__________, X__________, X__________, X__________, (0, 4, 16), (0, 64, 255), X__________, X__________],
    [X__________, X__________, X__________, X__________, X__________, (0, 4, 16), (0, 64, 255), X__________],
    [X__________, X__________, X__________, X__________, X__________, X__________, (0, 4, 16), (0, 64, 255)],
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, (0, 4, 16)],
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, X__________],
    [(VariableDelay(0, 2))]
    ]

snow_falling = [
    [(255, 255, 255), X__________, X__________, X__________, X__________, X__________, X__________, X__________],
    [X__________, (255, 255, 255), X__________, X__________, X__________, X__________, X__________, X__________],
    [X__________, X__________, (255, 255, 255), X__________, X__________, X__________, X__________, X__________],
    [X__________, X__________, X__________, (255, 255, 255), X__________, X__________, X__________, X__________],
    [X__________, X__________, X__________, X__________, (255, 255, 255), X__________, X__________, X__________],
    [X__________, X__________, X__________, X__________, X__________, (255, 255, 255), X__________, X__________],
    [X__________, X__________, X__________, X__________, X__________, X__________, (255, 255, 255), X__________],
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, (255, 255, 255)],
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, X__________],
    [(VariableDelay(0, 2))]
    ]

thunder_flash = [
    [(64, 64, 64), (64, 64, 64), (64, 64, 64), X__________, X__________, X__________, X__________, X__________],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)],
]

flood = [
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, (0, 0, 64)]
]

snow_layer = [
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, (64, 64, 64)]
]

if __name__=="__main__":
    # examples
    drip = Effect(frames=raindrop_dripping, fps=3)
    rain = Effect(frames=raindrop_falling, fps=10)
    heavy_rain = Effect(frames=raindrop_falling, fps=10, overlay=flood, mirrored=True)
    snow = Effect(frames=snow_falling, fps=3)
    heavy_snow = Effect(frames=snow_falling, fps=5, overlay=snow_layer, mirrored=True)

    print("starting...")
    effect = Thunder(frames=raindrop_falling, fps=10)
    heavy_rain.loop()