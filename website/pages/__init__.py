import solara
from solara import autorouting
from solara.alias import rv
from solara.components.title import Title
from solara.server import server
from solara.website.components.algolia import Algolia

from ..components import Header

title = "Home"

route_order = ["/", "examples"]


@solara.component
def Page():
    solara.Markdown("should not see me")


@solara.component
def Examples():
    with solara.Link("examples"):
        solara.Button(
            "Show Examples", icon_name="mdi-code-braces", class_="ma-2", text=True
        )
