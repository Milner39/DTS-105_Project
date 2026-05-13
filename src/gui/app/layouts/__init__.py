from ..components.FragmentComponent import FragmentComponent
from .. import type_defs as GuiTypes



class Layout(FragmentComponent):
  """
  | Layout class to extend when creating real layouts.
    (Don't use this class in the GUI by itself)
  """

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)

    self.content: GuiTypes.CTkFrameT | None = None



  def set_content(
    self,
    new_content: type[GuiTypes.CTkFrameTG],
    master: GuiTypes.CTkMasterT | None,
    *args,
    **kwargs
  ) -> GuiTypes.CTkFrameTG:
    """Set the current content"""

    if self.content is not None:
      self.content.destroy()

    if master is None:
      master = self

    self.content = new_content(master, *args, **kwargs)
    return self.content






class EmptyLayout(Layout):
  """
  | The simplest example of how to extend the layout base class.
  """

  def __init__(self, master: GuiTypes.CTkMasterT):
    super().__init__(master)


    self.grid(row=0, column=0, sticky="nsew")
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)



  def set_content(self, new_content: type[GuiTypes.CTkFrameTG], *args, **kwargs) -> GuiTypes.CTkFrameTG:
    content = super().set_content(new_content, *args, **kwargs)

    content.grid(row=0, column=0, sticky="nsew")

    return content
