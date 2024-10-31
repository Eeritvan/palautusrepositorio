from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        testing = toml.loads(content)

        name = testing['tool']['poetry']['name']
        description = testing['tool']['poetry']['description']
        deps = testing['tool']['poetry']['dependencies']
        dev_deps = testing['tool']['poetry']['group']['dev']['dependencies']
        license = testing['tool']['poetry']['license']
        authors = testing['tool']['poetry']['authors']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, deps, dev_deps)
