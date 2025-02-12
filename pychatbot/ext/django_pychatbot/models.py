from pychatbot.ext.django_pychatbot.abstract_models import AbstractBaseStatement, AbstractBaseTag


class Statement(AbstractBaseStatement):
    """
    A statement represents a single spoken entity, sentence or
    phrase that someone can say.
    """
    pass


class Tag(AbstractBaseTag):
    """
    A label that categorizes a statement.
    """
    pass
