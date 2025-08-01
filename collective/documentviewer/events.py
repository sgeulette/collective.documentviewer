from collective.documentviewer.interfaces import IConversionFinishedEvent
from zope.component.interfaces import ObjectEvent
from zope.interface import implements


class ConversionFinishedEvent(ObjectEvent):
    implements(IConversionFinishedEvent)

    def __init__(self, obj, status):
        self.object = obj
        self.status = status
