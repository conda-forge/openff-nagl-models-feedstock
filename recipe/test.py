from openff.nagl_models import validate_nagl_model_path, list_available_nagl_models, __version__
from packging.version import Version


assert Version(__version__) > Version("2026")

print(list_available_nagl_models())

assert len(list_available_nagl_models()) > 0

model_path = validate_nagl_model_path("openff-gnn-am1bcc-1.0.0.pt")
