import numpy as np
import solara
from matplotlib.figure import Figure
from mesa.visualization import SolaraViz, make_plot_measure
from mesa_models.sugarscape_g1mt.model import SugarscapeG1mt
from mesa_models.sugarscape_g1mt.trader_agents import Trader


def SpaceDrawer(model):
    def portray(g):
        layers = {
            "sugar": [[np.nan for j in range(g.height)] for i in range(g.width)],
            "spice": [[np.nan for j in range(g.height)] for i in range(g.width)],
            "trader": {"x": [], "y": [], "c": "tab:red", "marker": "o", "s": 10},
        }

        for content, (i, j) in g.coord_iter():
            for agent in content:
                if isinstance(agent, Trader):
                    layers["trader"]["x"].append(i)
                    layers["trader"]["y"].append(j)
                else:
                    # Don't visualize resource with value <= 1.
                    layers["sugar"][i][j] = (
                        agent.sugar_amount if agent.sugar_amount > 1 else np.nan
                    )
                    layers["spice"][i][j] = (
                        agent.spice_amount if agent.spice_amount > 1 else np.nan
                    )
        return layers

    fig = Figure()
    ax = fig.subplots()
    out = portray(model.grid)
    # Sugar
    # Important note: imshow by default draws from upper left. You have to
    # always explicitly specify origin="lower".
    im = ax.imshow(out["sugar"], cmap="spring", origin="lower")
    fig.colorbar(im, orientation="vertical")
    # Spice
    ax.imshow(out["spice"], cmap="winter", origin="lower")
    # Trader
    ax.scatter(**out["trader"])
    ax.set_axis_off()
    return solara.FigureMatplotlib(fig)


@solara.component
def Page():
    model_params = {
        "width": 50,
        "height": 50,
    }

    model1 = SugarscapeG1mt(50, 50)

    SolaraViz(
        model1,
        components=[SpaceDrawer, make_plot_measure(["Trader", "Price"])],
        name="Sugarscape {G1, M, T}",
        play_interval=1500,
    )
