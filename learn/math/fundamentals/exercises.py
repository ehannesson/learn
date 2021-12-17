# exercises.py


import numpy as np


from exercises import MathExercise
from fields import IntegerField


class MathFundamentalsExercise(MathExercise):

    def __init__(self, **kwargs):

        super().__init__(exercise_subject='fundamentals', **kwargs)


class AdditionExercise(MathFundamentalsExercise):

    def __init__(
        self,
        outline=None,
        exercise_values=None,
        solution_outline=None,
        explanation_outline=None,
        hint_outlines=None,
        level=None,
        mastery_points=None,
        concepts=None,
        fields=None,
        field_class=IntegerField,
        **field_kwargs
    ):
        super().__init__(
            outline=outline,
            exercise_values=exercise_values,
            solution_outline=solution_outline,
            explanation_outline=explanation_outline,
            hint_outlines=hint_outlines,
            level=level,
            mastery_points=mastery_points,
            concepts=concepts,
            exercise_type='addition',
            fields=fields,
            field_class=field_class,
            field_kwargs=field_kwargs
        )

        self.generate_solution_values()

    def generate_solution_values(self) -> None:
        if self.solution_values is None:
            self.solution_values = [self.fields[0].values.sum()]


class SubtractionExercise(MathFundamentalsExercise):

    def __init__(
        self,
        outline=None,
        exercise_values=None,
        solution_outline=None,
        explanation_outline=None,
        hint_outlines=None,
        level=None,
        mastery_points=None,
        concepts=None,
        fields=None,
        field_class=IntegerField,
        **field_kwargs
    ):

        super().__init__(
            outline=outline,
            exercise_values=exercise_values,
            solution_outline=solution_outline,
            explanation_outline=explanation_outline,
            hint_outlines=hint_outlines,
            level=level,
            mastery_points=mastery_points,
            concepts=concepts,
            exercise_type='subtraction',
            fields=fields,
            field_class=field_class,
            field_kwargs=field_kwargs
        )

        self.generate_solution_values()

    def generate_solution_values(self) -> None:
        if self.solution_values is None:
            # we only have one field
            self.solution_values = [self.fields[0].values[0]]
            for i in range(1, self.fields[0].values.size):
                self.solution_values[0] -= self.fields[0].values[i]


class MultiplicationExercise(MathFundamentalsExercise):

    def __init__(
        self,
        outline=None,
        exercise_values=None,
        solution_outline=None,
        explanation_outline=None,
        hint_outlines=None,
        level=None,
        mastery_points=None,
        concepts=None,
        fields=None,
        field_class=IntegerField,
        **field_kwargs
    ):

        super().__init__(
            outline=outline,
            exercise_values=exercise_values,
            solution_outline=solution_outline,
            explanation_outline=explanation_outline,
            hint_outlines=hint_outlines,
            level=level,
            mastery_points=mastery_points,
            concepts=concepts,
            exercise_type='multiplication',
            fields=fields,
            field_class=field_class,
            field_kwargs=field_kwargs
        )

        self.generate_solution_values()

    def generate_solution_values(self) -> None:
        if self.solution_values is None:
            # we only have one field
            self.solution_values = np.prod(self.fields[0].values, keepdims=True)


class DivisionExercise(MathFundamentalsExercise):

    def __init__(
        self,
        outline=None,
        exercise_values=None,
        solution_outline=None,
        explanation_outline=None,
        hint_outlines=None,
        level=None,
        mastery_points=None,
        concepts=None,
        round_=2,
        fields=None,
        field_class=IntegerField,
        **field_kwargs
    ):

        super().__init__(
            outline=outline,
            exercise_values=exercise_values,
            solution_outline=solution_outline,
            explanation_outline=explanation_outline,
            hint_outlines=hint_outlines,
            level=level,
            mastery_points=mastery_points,
            concepts=concepts,
            exercise_type='division',
            fields=fields,
            field_class=field_class,
            field_kwargs=field_kwargs
        )

        self.round = round_

        self.generate_solution_values()

    def generate_solution_values(self) -> None:
        if self.solution_values is None:
            # we only have one field
            solution_values = [self.fields[0].values[0]]
            for i in range(1, self.fields[0].values.size):
                solution_values[0] /= self.fields[0].values[i]

            self.solution_values = np.round(solution_values, decimals=self.round)
