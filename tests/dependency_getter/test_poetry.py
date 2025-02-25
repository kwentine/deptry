from pathlib import Path

from deptry.dependency_getter.poetry import PoetryDependencyGetter
from deptry.utils import run_within_dir


def test_dependency_getter(tmp_path: Path) -> None:
    fake_pyproject_toml = """[tool.poetry.dependencies]
python = ">=3.7,<4.0"
bar =  { version = ">=2.5.1,<4.0.0", python = ">3.7" }
foo-bar =  { version = ">=2.5.1,<4.0.0", optional = true, python = ">3.7" }

[tool.poetry.dev-dependencies]
toml = "^0.10.2"
foo =  { version = ">=2.5.1,<4.0.0", optional = true }"""

    with run_within_dir(tmp_path):
        with open("pyproject.toml", "w") as f:
            f.write(fake_pyproject_toml)

        dependencies_extract = PoetryDependencyGetter().get()
        dependencies = dependencies_extract.dependencies
        dev_dependencies = dependencies_extract.dev_dependencies

        assert len(dependencies) == 2
        assert len(dev_dependencies) == 2

        assert dependencies[0].name == "bar"
        assert dependencies[0].is_conditional
        assert not dependencies[0].is_optional
        assert "bar" in dependencies[0].top_levels

        assert dependencies[1].name == "foo-bar"
        assert dependencies[1].is_conditional
        assert dependencies[1].is_optional
        assert "foo_bar" in dependencies[1].top_levels

        assert dev_dependencies[0].name == "toml"
        assert not dev_dependencies[0].is_conditional
        assert not dev_dependencies[0].is_optional
        assert "toml" in dev_dependencies[0].top_levels

        assert dev_dependencies[1].name == "foo"
        assert not dev_dependencies[1].is_conditional
        assert dev_dependencies[1].is_optional
        assert "foo" in dev_dependencies[1].top_levels
