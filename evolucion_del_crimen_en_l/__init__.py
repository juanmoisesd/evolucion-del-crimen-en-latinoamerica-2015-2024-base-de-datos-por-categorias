"""Base de datos sobre la evoluci&oacute;n del crimen en Am&eacute;rica Latina y el
DOI:https://juanmoisesd.github.io/evolucion-del-crimen-en-latinoamerica-2015-2024-base-de-datos-por-categorias/"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://juanmoisesd.github.io/evolucion-del-crimen-en-latinoamerica-2015-2024-base-de-datos-por-categorias/".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Base de datos sobre la evoluci&oacute;n del crimen en Am&eac"
def info():print("DOI: https://juanmoisesd.github.io/evolucion-del-crimen-en-latinoamerica-2015-2024-base-de-datos-por-categorias/\nGitHub: https://github.com/juanmoisesd/evolucion-del-crimen-en-latinoamerica-2015-2024-base-de-datos-por-categorias")
