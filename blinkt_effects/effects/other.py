from effects_base import Effect

# class Thunder(EffectBase):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def custom_action(self):
#         if random.randint(0, 15) == 1:
#             self.add_overwrite(thunder_flash)


X__________ = (0, 0, 0)

knight_rider = [
    [(255, 0, 0), X__________, X__________, X__________, X__________, X__________, X__________, X__________],
    [(8, 0, 0), (255, 0, 0), X__________, X__________, X__________, X__________, X__________, X__________],
    [X__________, (8, 0, 0), (255, 0, 0), X__________, X__________, X__________, X__________, X__________],
    [X__________, X__________, (8, 0, 0), (255, 0, 0), X__________, X__________, X__________, X__________],
    [X__________, X__________, X__________, (8, 0, 0), (255, 0, 0), X__________, X__________, X__________],
    [X__________, X__________, X__________, X__________, (8, 0, 0), (255, 0, 0), X__________, X__________],
    [X__________, X__________, X__________, X__________, X__________, (8, 0, 0), (255, 0, 0), X__________],
    [X__________, X__________, X__________, X__________, X__________, X__________, (8, 0, 0), (255, 0, 0)],
    [X__________, X__________, X__________, X__________, X__________, X__________, X__________, (255, 0, 0)],
    [X__________, X__________, X__________, X__________, X__________, X__________, (255, 0, 0), (8, 0, 0)],
    [X__________, X__________, X__________, X__________, X__________, (255, 0, 0), (8, 0, 0), X__________],
    [X__________, X__________, X__________, X__________, (255, 0, 0), (8, 0, 0), X__________, X__________],
    [X__________, X__________, X__________, (255, 0, 0), (8, 0, 0), X__________, X__________, X__________],
    [X__________, X__________, (255, 0, 0), (8, 0, 0), X__________, X__________, X__________, X__________],
    [X__________, (255, 0, 0), (8, 0, 0), X__________, X__________, X__________, X__________, X__________],
    [(255, 0, 0), (8, 0, 0), X__________, X__________, X__________, X__________, X__________, X__________],
]


if __name__=="__main__":
    knightrider = Effect(frames=knight_rider)
    knightrider.loop()