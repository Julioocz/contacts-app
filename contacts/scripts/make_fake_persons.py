from ..factory import PersonWithInfoFactory


def run():
    PersonWithInfoFactory.create_batch(20)
