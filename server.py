import importlib

import solara


solara_examples = {
    "examples": ["hotelling_law", "schelling"],
    "gis": ["geo_schelling", "geo_sir"],
}


@solara.component
def DiscreteExamplePage(name: str = None):
    examples = solara_examples["examples"]
    with solara.Row():
        for example in examples:
            with solara.Link(example):
                solara.Button(label=f"{example}")
    if name is not None:
        importlib.import_module(f"examples.{name}.app")


@solara.component
def GisExamplePage(name: str = None):
    examples = solara_examples["gis"]
    with solara.Row():
        for example in examples:
            with solara.Link(example):
                solara.Button(label=f"{example}")
    if name is not None:
        importlib.import_module(f"gis.{name}.app")


routes = [
    solara.Route(path="/", component=solara.Markdown("Welcome to Mesa Examples!")),
    solara.Route(path="examples", component=DiscreteExamplePage, label="examples"),
    solara.Route(path="gis", component=GisExamplePage, label="gis"),
]
