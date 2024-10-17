from mesa.visualization import (
    SolaraViz,
    make_plot_measure,
    make_space_matplotlib,
)
from mesa_models.boltzmann_wealth_model.model import BoltzmannWealthModel
import solara


def agent_portrayal(agent):
    size = 10
    color = "tab:red"
    if agent.wealth > 0:
        size = 50
        color = "tab:blue"
    return {"size": size, "color": color}


# Create the SolaraViz page. This will automatically create a server and display the
# visualization elements in a web browser.
# Display it using the following command in the example directory:
# solara run app.py
# It will automatically update and display any changes made to this file
@solara.component
def Page():
    model_params = {
        "N": {
            "type": "SliderInt",
            "value": 50,
            "label": "Number of agents:",
            "min": 10,
            "max": 100,
            "step": 1,
        },
        "width": 10,
        "height": 10,
    }
    # Create initial model instance
    model1 = BoltzmannWealthModel(50, 10, 10)

    # Create visualization elements. The visualization elements are solara components
    # that receive the model instance as a "prop" and display it in a certain way.
    # Under the hood these are just classes that receive the model instance.
    # You can also author your own visualization elements, which can also be functions
    # that receive the model instance and return a valid solara component.
    SpaceGraph = make_space_matplotlib(agent_portrayal)
    GiniPlot = make_plot_measure("Gini")
    SolaraViz(
        model1,
        components=[SpaceGraph, GiniPlot],
        model_params=model_params,
        name="Boltzmann Wealth Model",
    )


# In a notebook environment, we can also display the visualization elements directly
# SpaceGraph(model1)
# GiniPlot(model1)

# The plots will be static. If you want to pick up model steps,
# you have to make the model reactive first
# reactive_model = solara.reactive(model1)
# SpaceGraph(reactive_model)
# In a different notebook block:
# reactive_model.value.step()
