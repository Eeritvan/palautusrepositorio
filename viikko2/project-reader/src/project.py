class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_list = "\n".join(f"- {author}" for author in self.authors)
        deps_list = "\n".join(f"- {dep}" for dep in self.dependencies)
        dev_deps = "\n".join(f"- {devdep}" for devdep in self.dev_dependencies)

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors:\n{authors_list}\n"
            f"\nDependencies:\n{deps_list}\n"
            f"\nDevelopment dependencies:\n{dev_deps}"
        )