from typing import List

from pyz.decorators.task_decorator import TaskDecorator


class BaseZeebeDecorator(object):
    def __init__(self, before: List[TaskDecorator] = None, after: List[TaskDecorator] = None):
        self._before: List[TaskDecorator] = before or []
        self._after: List[TaskDecorator] = after or []

    def before(self, *decorators: TaskDecorator) -> None:
        self._before.extend(decorators)

    def after(self, *decorators: TaskDecorator) -> None:
        self._after.extend(decorators)
