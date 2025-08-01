from collective.documentviewer.config import CONVERTABLE_TYPES
from collective.documentviewer.config import EXTENSION_TO_ID_MAPPING
from collective.documentviewer.interfaces import IFileWrapper
from Products.CMFCore.utils import getToolByName

import errno
import os


def getDocumentType(obj, allowed_types):
    ct = IFileWrapper(obj).file_type
    if ct is None:
        return None

    mime_registry = getToolByName(obj, "mimetypes_registry")
    for _type in mime_registry.lookup(ct):
        for ext in _type.extensions:
            if ext in EXTENSION_TO_ID_MAPPING:
                id = EXTENSION_TO_ID_MAPPING[ext]
                if id in allowed_types:
                    return CONVERTABLE_TYPES[id]

    return None


def allowedDocumentType(object, allowed_types):
    return getDocumentType(object, allowed_types) is not None


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise


def getPortal(obj):
    return getToolByName(obj, "portal_url").getPortalObject()
