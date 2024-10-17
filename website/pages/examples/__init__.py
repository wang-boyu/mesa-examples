import solara
from solara.website.components import Gallery, MarkdownWithMetadata

title = "Examples"


@solara.component
def Page(route_external=None):
    Gallery(route_external)
