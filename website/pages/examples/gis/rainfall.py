from typing import Tuple

from mesa.visualization import Slider, SolaraViz, make_plot_measure
from mesa_geo.visualization import make_geospace_leaflet
from mesa_models.gis.rainfall.rainfall.model import Rainfall
from mesa_models.gis.rainfall.rainfall.space import LakeCell

import solara

model_params = {
    "rain_rate": Slider("rain rate", 500, 0, 500, 5),
    "water_height": Slider("water height", 5, 1, 5, 1),
    "num_steps": Slider("total number of steps", 20, 1, 100, 1),
    "export_data": False,
}


def cell_portrayal(cell: LakeCell) -> Tuple[float, float, float, float]:
    if cell.water_level == 0:
        return cell.elevation, cell.elevation, cell.elevation, 1
    else:
        # return a blue color gradient based on the normalized water level
        # from the lowest water level colored as RGBA: (74, 141, 255, 1)
        # to the highest water level colored as RGBA: (0, 0, 255, 1)
        return (
            (1 - cell.water_level_normalized) * 74,
            (1 - cell.water_level_normalized) * 141,
            255,
            1,
        )


@solara.component
def Page():
    model = Rainfall()
    SolaraViz(
        model,
        [
            make_geospace_leaflet(cell_portrayal, zoom=11),
            make_plot_measure(
                ["Total Amount of Water", "Total Contained", "Total Outflow"]
            ),
        ],
        name="Rainfall Model",
        model_params=model_params,
    )
