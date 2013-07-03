from hamcrest.core.base_matcher import BaseMatcher


class MatchSubclassOf(BaseMatcher):

    def __init__(self, parent_class):
        self.parent_class = parent_class

    def _matches(self, item):
        return issubclass(item, self.parent_class)

    def describe_to(self, description):
        description.append_text('subclass of ')\
                   .append_description(self.parent_class)


def subclass_of(parent_class):
    return MatchSubclassOf(parent_class)
