from ...components.CardComponent import CardComponent
from ...components.FragmentComponent import FragmentComponent
from ...layouts.WithViewTitleLayout import WithViewTitleLayout
from .components.NewLogFormComponent import NewLogFormComponent
from ... import type_defs as GuiTypes



class NewLogView(FragmentComponent):
  """The `new log` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.CARD_MAX_WIDTH: int = 520


    view_title_layout = WithViewTitleLayout(self, "New Log")
    content = view_title_layout.set_content(FragmentComponent)


    # 3x3 grid centres the card horizontally and vertically.
    content.grid_columnconfigure(0, weight=1)
    content.grid_columnconfigure(1, weight=0, minsize=self.CARD_MAX_WIDTH)
    content.grid_columnconfigure(2, weight=1)
    content.grid_rowconfigure(0, weight=1)
    content.grid_rowconfigure(1, weight=0)
    content.grid_rowconfigure(2, weight=1)

    self._content = content
    content.bind("<Configure>", self._on_resize)
    content.after_idle(self._on_resize)


    card = CardComponent(content)
    card.grid(row=1, column=1, sticky="ew")

    form = NewLogFormComponent(card.content)
    form.pack(fill="x")



  def _on_resize(self, _event=None) -> None:
    """
    | Set the width of the card to be the smallest of:
      - The available horizontal space
      - CARD_MAX_WIDTH
    """

    available_w = self._content.winfo_width()
    self._content.grid_columnconfigure(1,
      minsize=min(self.CARD_MAX_WIDTH, max(0, available_w))
    )
