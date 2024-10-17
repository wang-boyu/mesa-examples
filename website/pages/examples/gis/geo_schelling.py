import solara
from mesa.visualization import Slider, SolaraViz, make_plot_measure
from mesa_geo.visualization import make_geospace_leaflet
from mesa_models.gis.geo_schelling.model import GeoSchelling


def make_plot_happiness(model):
    return solara.Markdown(f"**Happy agents: {model.happy}**")


def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    portrayal = {}
    if agent.atype is None:
        portrayal["color"] = "Grey"
    elif agent.atype == 0:
        portrayal["color"] = "Red"
    else:
        portrayal["color"] = "Blue"
    return portrayal


@solara.component
def Page():
    model_params = {
        "pop_size": Slider("Population size", 30, 10, 100, 10),
        "init_infected": Slider("Fraction initial infection", 0.2, 0.00, 1.0, 0.05),
        "exposure_distance": Slider("Exposure distance", 500, 100, 1000, 100),
    }

    model_params = {
        "density": Slider("Agent density", 0.6, 0.1, 1.0, 0.1),
        "minority_pc": Slider("Fraction minority", 0.2, 0.00, 1.0, 0.05),
        "export_data": False,
    }

    model = GeoSchelling()
    SolaraViz(
        model,
        [
            make_geospace_leaflet(schelling_draw, zoom=4),
            make_plot_measure(["happy"]),
            make_plot_happiness,
        ],
        model_params=model_params,
        name="GeoSchelling",
    )
