import click.testing
import pytest
from click.testing import CliRunner
from absorb.core.idea.commands import idea


@pytest.fixture
def runner() -> CliRunner:
    return click.testing.CliRunner()


# Tests for new() (new idea)
def test_idea_new(runner: CliRunner) -> None:
    """Adding an idea normally should return 0, if it is valid in nature."""
    result = runner.invoke(
        idea, ["new", "Make a cool machine!", "Some description.", "@ideas"]
    )
    assert result.exit_code == 0


def test_idea_new_no_tags(runner: CliRunner) -> None:
    """Adding an idea with no tags should return 0, if it is valid in nature."""
    result = runner.invoke(
        idea, ["new", "Make a cool machine!", "Some description.", "."]
    )
    assert result.exit_code == 0


# Tests for edit() (edit idea)
def test_idea_edit(runner: CliRunner) -> None:
    """Editing an idea normally should return 0, if it is valid in nature."""
    result = runner.invoke(
        idea,
        [
            "edit",
            "#1",
            "Make a super cool machine!",
            "New description.",
            "@ideas @create",
        ],
    )
    assert result.exit_code == 0


def test_idea_edit_with_no_tags(runner: CliRunner) -> None:
    """Editing an idea with no tags should return 0, if it is valid in nature."""
    result = runner.invoke(
        idea, ["edit", "#1", "Make a super cool machine!", "New description.", "."]
    )
    assert result.exit_code == 0


def test_idea_edit_only_name(runner: CliRunner) -> None:
    """Editing an idea's name with no tags or description should return 0, if it is valid in nature."""
    result = runner.invoke(idea, ["edit", "#1", "Make a super cool machine!", ".", "."])
    assert result.exit_code == 0


def test_idea_edit_only_tags(runner: CliRunner) -> None:
    """Editing an idea's tags with no description or name should return 0, if it is valid in nature."""
    result = runner.invoke(idea, ["edit", "#1", ".", ".", "@create"])
    assert result.exit_code == 0


# Tests for open() (open idea)
def test_idea_open(runner: CliRunner) -> None:
    """Opening an idea should return 0, if it is valid in nature."""
    result = runner.invoke(idea, ["open", "#1"])
    assert result.exit_code == 0


# Tests for show() (show idea)
def test_idea_show(runner: CliRunner) -> None:
    """Showing all ideas should return 0, if it is valid in nature."""
    result = runner.invoke(idea, ["show"])
    assert result.exit_code == 0
