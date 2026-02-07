from .logger import vml as logger

try:
    from . import vml_engine
except ImportError:
    vml_engine = None

__version__ = "0.1.0"