class VCD_SIG_TYPE():
    WIRE = "wire"
    REAL = "real"


class VcdVarInfo():
    """
    Common part of VcdParsingVarInfo and VcdVarWritingInfo
    Container of informations about variable in VCD

    :ivar vcdId: id in VCD file
    :ivar name: name in VCD file
    :ivar widht: width in VCD file (int)
    :ivar sigType: VCD var type name (from VCD_SIG_TYPE)
    :ivar parent: parent VcdSignalScope object
    """

    def __init__(self, vcdId, name, width, sigType, parent):
        self.vcdId = vcdId
        self.name = name
        self.width = width
        self.sigType = sigType
        self.parent = parent

    def __repr__(self):
        return "<%s %s vcdId:%s>" % (
            self.__class__.__name__,
            VcdVarScope._getDebugName(self),
            self.vcdId)


class VcdVarScope():
    """
    VCD module - container for variables

    :ivar name: name of this scope
    :ivar parent: parent scope of this scope or None
    :ivar children: dict {name: <VcdVarScope or VcdVarInfo instance>}
    """

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}

    def _getDebugName(self):
        buff = []
        o = self
        while True:
            buff.append(o.name)
            o = o.parent
            if o is None:
                break
        return ".".join(reversed(buff))

    def toJson(self):
        return {
            "name": self.name,
            "children": {n: ch.toJson() for n, ch in self.children.items()}
        }

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self._getDebugName())
