from setuptools import setup, find_packages
setup(
    name="evolucion-del-crimen-en-latinoamerica-2015-2024-base-de-datos-por-categorias",
    version="1.0.0",
    description="Base de datos sobre la evoluci&oacute;n del crimen en Am&eacute;rica Latina y el Caribe durante el p",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/evolucion-del-crimen-en-latinoamerica-2015-2024-base-de-datos-por-categorias",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="cc0, citation, crime-data, criminology, dataset, fair-data, iberoamerica, juan-moises-de-la-serna, latam, latin-america, open-data, open-science, orcid, research, security, zenodo, zenodo, open-data",
)