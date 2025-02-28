from modules.common.component_setup import ComponentSetup
from helpermodules.auto_str import auto_str


@auto_str
class E3dcConfiguration:
    def __init__(self, address: str = None):
        self.address = address


@auto_str
class E3dc:
    def __init__(self,
                 name: str = "E3DC",
                 type: str = "E3DC",
                 id: int = 0,
                 configuration: E3dcConfiguration = None) -> None:
        self.name = name
        self.type = type
        self.id = id
        self.configuration = configuration or E3dcConfiguration()


@auto_str
class E3dcBatConfiguration:
    def __init__(self) -> None:
        pass


@auto_str
class E3dcBatSetup(ComponentSetup[E3dcBatConfiguration]):
    def __init__(self,
                 name: str = "E3DC Speicher",
                 type: str = "bat",
                 id: int = 0,
                 configuration: E3dcBatConfiguration = None) -> None:
        super().__init__(name, type, id, configuration
                         or E3dcBatConfiguration())


@auto_str
class E3dcCounterConfiguration:
    def __init__(self) -> None:
        pass


@auto_str
class E3dcCounterSetup(ComponentSetup[E3dcCounterConfiguration]):
    def __init__(self,
                 name: str = "E3DC Zähler",
                 type: str = "counter",
                 id: int = 0,
                 configuration: E3dcCounterConfiguration = None) -> None:
        super().__init__(name, type, id, configuration or
                         E3dcCounterConfiguration())


@auto_str
class E3dcInverterConfiguration:
    def __init__(self, read_ext: bool = False):
        self.read_ext = read_ext


@auto_str
class E3dcInverterSetup(ComponentSetup[E3dcInverterConfiguration]):
    def __init__(self,
                 name: str = "E3DC Wechselrichter",
                 type: str = "inverter",
                 id: int = 0,
                 configuration: E3dcInverterConfiguration = None) -> None:
        super().__init__(name, type, id, configuration or E3dcInverterConfiguration())
