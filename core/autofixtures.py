from core.models import User, Session, Event, KeystrokeEvent, TextSelectionEvent, MouseHoverEvent, MouseMovementEvent, MouseClickEvent, MouseScrollEvent
from autofixture import generators, register, AutoFixture

class UserAutoFixture(AutoFixture):
    field_values = {
        'username': generators.FirstNameGenerator(),
        'name': generators.FirstNameGenerator()
    }

register(User, UserAutoFixture)
