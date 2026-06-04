from ...components.CardComponent import CardComponent
from ...components.FragmentComponent import FragmentComponent
from ...layouts.WithViewTitleLayout import WithViewTitleLayout
from ...stores.LogEditorStore import log_editor_store
from .components.NewLogFormComponent import NewLogFormComponent
from ... import type_defs as GuiTypes
from ...theme import Sizes
from .....database import Queries



class NewLogView(FragmentComponent):
  """The `new log` view"""

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.CARD_MAX_WIDTH = Sizes.Dimension.xxl * 4


    # The day to edit is stored in the store. Find if log exists for target day.
    target_date = log_editor_store.get_state().target_date
    log = Queries.MoodLog.get_log_by_day(target_date)
    title = "Edit Log" if log is not None else "New Log"

    view_title_layout = WithViewTitleLayout(self, title)
    content = view_title_layout.set_content(FragmentComponent)


    center = FragmentComponent(content)
    center.pack(expand=True, fill="both",
      padx=Sizes.Spacing.md, pady=Sizes.Spacing.md,
    )

    # 3x3 grid centres the card horizontally and vertically.
    # grid let's us use `minsize` (can't with `pack`)
    center.grid_columnconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=0,
      minsize=center._apply_widget_scaling(self.CARD_MAX_WIDTH)
    )
    center.grid_columnconfigure(2, weight=1)
    center.grid_rowconfigure(0, weight=1)
    center.grid_rowconfigure(1, weight=0)
    center.grid_rowconfigure(2, weight=1)
  
    center.bind("<Configure>", self._on_resize)
    center.after_idle(self._on_resize)

    self._center = center


    card = CardComponent(center)
    card.grid(row=1, column=1, sticky="ew")

    form = NewLogFormComponent(card.content, log=log, target_date=target_date)
    form.pack(fill="x")



  def _on_resize(self, _event=None) -> None:
    """
    | Set the width of the card to be the smallest of:
      - The available horizontal space
      - CARD_MAX_WIDTH
    """

    available_w = self._center.winfo_width()
    max_w = self._center._apply_widget_scaling(self.CARD_MAX_WIDTH)
    self._center.grid_columnconfigure(1,
      minsize=min(max_w, max(0, available_w))
    )
