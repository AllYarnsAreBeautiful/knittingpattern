from test import *
from knittingpattern.InstructionLibrary import DefaultInstructions, default_instructions


@fixture
def default():
    return DefaultInstructions()


def test_default_instructions_is_a_singleton():
    assert default_instructions() is default_instructions()


def test_knitting_instruction(default):
    assert default["knit"].type == "knit"


def test_purl_instruction(default):
    assert default["skp"]["number of consumed meshes"] == 2
    

def test_yarn_over(default):
    assert default["yo"]["number of consumed meshes"] == 0


def test_default_instructions_are_an_instance_of_the_class():
    assert isinstance(default_instructions(), DefaultInstructions)