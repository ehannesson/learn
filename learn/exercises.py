# exercises.py

import json
from typing import Dict


import numpy as np


class Exercise:
    """
    Base class providing general framework for representing an exercise.

    Parameters
    ----------
    TODO

    Attributes
    ----------
    TODO

    Methods
    -------
    TODO
    """

    # used to reset instance specific parameters when calling `new_instance`
    new_instance_dict = {'exercise_values': None}

    def __init__(
        self,
        outline=None,
        fields=None,
        exercise_values=None,
        solution_outline=None,
        explanation_outline=None,
        hint_outlines=None,
        level=None,
        mastery_points=None,
        exercise_domain=None,
        exercise_subject=None,
        exercise_type=None,
        concepts=None,
        data_file=None,
        **kwargs
    ):
        self.fields = fields
        self.exercise_values = exercise_values
        self.solution_outline = solution_outline
        self.explanation_outline = explanation_outline
        self.hint_outlines = hint_outlines
        self.level = level
        self.mastery_points = mastery_points
        self.exercise_domain = exercise_domain
        self.exercise_subject = exercise_subject
        self.exercise_type = exercise_type
        self.concepts = concepts
        self._set_outline(outline, data_file)

        # to be set later
        self.solution = None        # str
        self.solution_values = None
        self.explanation = None     # str
        self.hints = None           # list of str

        self.statement = self.outline
        self.generate_exercise_values()
        self.generate_statement()

    def _set_outline(self, outline: str, data_file: str) -> None:
        """Set outline if provided; otherwise, attempt to load default."""
        # prefer explicitly set outline over default
        if outline:
            self.outline = outline
            return
        # if outline was not explicitly given, attempt to load default from file
        try:
            with open(data_file, 'r') as fp:
                self.outline = json.load(fp)[self.exercise_subject][self.exercise_type]
        except KeyError:
            raise KeyError(f'No such exercise key "{self.exercise_type}" in data file {self.data_file}.')

    def generate_exercise_values(self) -> None:
        """Generate values for every ExerciseField of the Exercise."""
        # only generate exercise_values *once* (i.e., *do not* regenerate them)
        if self.exercise_values is None:
            self.exercise_values = {
                f.field: f.generate_field_values() for f in self.fields
            }

    def generate_statement(self) -> None:
        """
        Generate exercise statement.

        This function simply iterates through each 'field', substituting values
        in place of 'field placeholders'.
        """
        # don't regenerate the statement
        if self.statement == self.outline:
            for field in self.fields:
                self.statement = field.fill_exercise_with_values(self.statement)

    def generate_solution(self):
        pass

    def generate_explanation(self):
        pass

    def generate_hint(self, ind):
        pass

    def new_instance(self):
        """Create a new `Exercise` object with the same init parameters."""
        # create new ExerciseField instances so the new Exercise object can
            # get new values (without overwritting this Exercise's values)
        fields = [field.new_instance() for field in self.fields]
        # copy argument dictionary, update fields value, and reset any
            # instance specific values
        kwargs = self.__dict__.copy()
        kwargs.update({'fields': fields})
        kwargs.update(self.new_instance_dict)

        return self.__class__(**kwargs)


class MathExercise(Exercise):

    def __init__(
        self,
        data_file='/run/media/erik/OS/Users/erikh/learn-stuff/learn/math/.data/exercise_outlines.json',
        **kwargs
    ):

        if not kwargs['fields']:
            kwargs['fields'] = [kwargs['field_class'](**kwargs['field_kwargs'])]

        super().__init__(
            exercise_domain='math',
            data_file=data_file,
            **kwargs
        )


class ProblemSet:

    def __init__(
        self,
        exercise_list=[],
        n_problems=10,
        **choice_kwargs
    ):

        self.n_problems = n_problems
        self.problems_remaining = n_problems
        self.exercise_list = exercise_list
        self.choice_kwargs = choice_kwargs

    def __iter__(self):
        while self.problems_remaining > 0:
            # choose problem type from exercise list
            self.problems_remaining -= 1
            yield self._select_problem_type()

    def _select_problem_type(self):
        """TODO : extend functionality to use custom initialization functions"""
        exercise = np.random.default_rng().choice(
            self.exercise_list, **self.choice_kwargs
        )
        return exercise.new_instance()
