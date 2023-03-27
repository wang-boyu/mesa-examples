import streamlit as st
import matplotlib.pyplot as plt

from model import Schelling


class MatplotlibGridVisualization:
    def __init__(self, portrayal_method, grid):
        self.portrayal_method = portrayal_method
        self.grid = grid

    def render(self):
        portrayal_list = []

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell_objects = self.grid.get_cell_list_contents([(x, y)])
                for obj in cell_objects:
                    portrayal = self.portrayal_method(obj)
                    if portrayal:
                        portrayal_list.append(
                            {"x": x, "y": y, "Color": portrayal["Color"]}
                        )

        # extract x, y, and color values
        x = [item["x"] for item in portrayal_list]
        y = [item["y"] for item in portrayal_list]
        colors = [item["Color"] for item in portrayal_list]

        plt.style.use("ggplot")
        # create figure and axis objects
        fig, ax = plt.subplots()

        # set axis limits
        ax.set_xlim((-1, self.grid.width))
        ax.set_ylim((-1, self.grid.height))

        # create scatter plot
        ax.scatter(x, y, c=colors)
        plt.axis("off")

        # show plot
        st.pyplot(fig)


# define the portrayal method
def schelling_draw(agent):
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}

    if agent.type == 0:
        portrayal["Color"] = "tab:blue"
    else:
        portrayal["Color"] = "tab:orange"
    return portrayal


st.title("Schelling's Model of Segregation")
density = st.sidebar.slider("Agent density", 0.1, 1.0, 0.8, 0.1)
minority_pc = st.sidebar.slider("Fraction minority", 0.00, 1.0, 0.2, 0.05)
homophily = st.sidebar.slider("Homophily", 0, 8, 3, 1)
step_button = st.sidebar.button("Step")

# define your model and grid here
schelling_model = Schelling(
    density=density, minority_pc=minority_pc, homophily=homophily
)

# create the MatplotlibGridVisualization object
visualization = MatplotlibGridVisualization(schelling_draw, schelling_model.grid)


if step_button:
    schelling_model.step()


# render the grid
visualization.render()

st.subheader(f"Happy agents: {schelling_model.happy}")
