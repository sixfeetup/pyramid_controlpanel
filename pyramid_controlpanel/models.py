from sqlalchemy import Column
from sqlalchemy import UnicodeText

from sixfeetup.bowab.db.base import Base
from sixfeetup.bowab.db.types import DottedPath
from sixfeetup.bowab.db.types import JSON


class ControlPanelSection(Base):
    __tablename__ = 'control_panel_sections'
    __table_args__ = {'schema': 'settings'}
    section = Column(UnicodeText, primary_key=True)
    panel_path = Column(DottedPath)
    panel_values = Column(JSON)

    def __init__(self, section, panel_path, panel_values):
        self.section = section
        self.panel_path = panel_path
        self.panel_values = panel_values

    def __repr__(self):
        return u"<ControlPanel(%s, %s)>" % (self.section, self.panel_path)
