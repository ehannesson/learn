# exercises.py

import re
from typing import Dict


import numpy as np
from numpy.random import default_rng


class ExerciseField:
    """
    Class representing a parameter field of an Exercise.

    Parameters
    ----------
    field : str
    gen_func : callable **kwargs --> ndarray
    **kwargs

    Attributes
    ----------

    Methods
    -------
    """

    def __init__(self, field, gen_func=default_rng().choice, **kwargs):

        self.field = field
        self.gen_func = gen_func
        self.kwargs = kwargs

        # to be set later
        self.values = None

    def generate_field_values(self):
        """
        Generate and return field values. If field values have already been
        generated, return those.
        """

        if self.values is None:
            self.values = self.gen_func(**self.kwargs)

        return self.values

    def fill_exercise_with_values(self, outline: str) -> str:
        """
        Fill in Exercise statement with field values.

        Parameters
        ----------
        outline : str
            Exercise statement outline. Fields to be filled must be of the form
            '__field#__'.

        Returns
        -------
        outline : str
            Exercise outline with associated field placeholders replaced by
            field values.
        """

        for i in range(self.values.size):
            outline = outline.replace(f'__{self.field}{i}__', str(self.values[i]))

        return outline


class Exercise:
    """
    Base class providing general framework for representing an exercise.

    Parameters
    ----------
    outline : str

    fields : list of ExerciseField

    solution_outline : str

    explanation_outline : str

    hint_outlines : list of str

    difficulty_level : int

    mastery_points : int

    concepts : list of TODO: ????.Concept objects

    Attributes
    ----------
    TODO

    Methods
    -------
    TODO
    """
    def __init__(
        self,
        outline=None,
        fields=None,
        solution_outline=None,
        explanation_outline=None,
        hint_outlines=None,
        difficulty_level=None,
        mastery_points=None,
        concepts=None
    ):
        self.outline = outline
        self.fields = fields
        self.solution_outline = solution_outline
        self.explanation_outline = explanation_outline
        self.hint_outlines = hint_outlines
        self.difficulty_level = difficulty_level
        self.mastery_points = mastery_points
        self.concepts = concepts

        # to be set later
        self.exercise_values = None # dict of 'statement_field' --> array-like of vals
        self.solution = None        # str
        self.explanation = None     # str
        self.hints = None           # list of str

        self.statement = self.outline
        self.generate_exercise_values()
        self.generate_statement()

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
