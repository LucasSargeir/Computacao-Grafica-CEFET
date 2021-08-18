# Sistema Solar

 <br/>

### Tecnologia Utilizada

- Python 3.8.
- Processing 3.

<br/>

### Trabalho

Esse trabalho é um estudo com o objetivo de colocar corpos orbitando outros. Para realizar o estudo foi montado um modelo que imita o sistema solar e os principais planetas (incluindo Plutão).

Os dados abaixo foram utilizados para representar os corpos selestes:

```python
YELLOW = (220,220,0)
BLUE = (33,40,204)
WHITE = (255,255,255)

sun = {"diameter": 250, "color": YELLOW}

moon = {"distance": 8, "diameter":7, "translate_time": 27.3, "color": WHITE, "angle": 0}

planets = [
    {"name": "mercury", "distance": 15, "diameter": 20, "color": (106,95,67), "translate_time": 88, "angle": 0},
    {"name": "venus", "distance": 30, "diameter": 40, "color": (255,191,111), "translate_time": -108, "angle": 0},
    {"name": "earth", "distance": 70, "diameter": 50, "color": BLUE, "translate_time": 365.1, "angle": 0},
    {"name": "mars", "distance": 150, "diameter": 30, "color": (201,17,7), "translate_time": 687, "angle": 0},
    {"name": "jupiter", "distance": 250, "diameter": 200, "color": (255,233,176), "translate_time": 4307, "angle": 0},
    {"name": "saturn", "distance": 300, "diameter": 130, "color": (255,170,116), "translate_time": 10731, "angle": 0},
    {"name": "uranus", "distance": 560, "diameter": 100, "color": (153,184,237), "translate_time": -30660, "angle": 0},
    {"name": "neptune", "distance": 750, "diameter": 70, "color": (0,123,132), "translate_time": 60152, "angle": 0},
    {"name": "pluto", "distance": 890, "diameter": 10, "color": (199,169,159), "translate_time": 103660, "angle": 0}
]
```



Uma miniatura do sistema solar criado pode ser visto abaixo:

<img src="https://github.com/LucasSargeir/Computacao-Grafica-CEFET/blob/main/imagens/solar_system.gif" />

