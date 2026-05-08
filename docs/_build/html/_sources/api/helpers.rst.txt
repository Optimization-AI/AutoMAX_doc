``src.core.helpers``
====================

.. py:function:: parse_hyperparameters_from_dict(items)

   Convert a raw hyperparameter specification dict into a mapping of
   :class:`~ConfigSpace.hyperparameters.Hyperparameter` objects.

   :param items: Mapping of hyperparameter name to its specification.
   :type items: dict[str, Any]
   :returns: Parsed hyperparameters keyed by name.
   :rtype: dict[str, Hyperparameter]
   :raises ValueError: If a specification is malformed or an unsupported type
       is encountered.

   .. rubric:: Supported specification formats

   .. list-table::
      :header-rows: 1
      :widths: 30 30 40

      * - Python value
        - Produced type
        - Notes
      * - ``int``, ``float``, ``str``
        - :class:`~ConfigSpace.hyperparameters.Constant`
        - Fixed value; not searched.
      * - ``(lower, upper)`` tuple
        - :class:`~ConfigSpace.hyperparameters.UniformFloatHyperparameter` or
          :class:`~ConfigSpace.hyperparameters.UniformIntegerHyperparameter`
        - Type inferred from bounds: ``float`` → Float HP, ``int`` → Int HP.
      * - ``[choice1, choice2, …]`` list
        - :class:`~ConfigSpace.hyperparameters.CategoricalHyperparameter`
        - First element used as default unless overridden.
      * - ``{"val": …, "default": …, "log": …}`` dict
        - Same as above, extended format
        - ``"val"`` is required; ``"default"`` and ``"log"`` are optional.
          ``"log": True`` enables log-scale sampling for numeric ranges.
      * - :class:`~ConfigSpace.hyperparameters.Hyperparameter` instance
        - Passed through unchanged
        - Allows mixing raw specs and pre-built ConfigSpace objects.

   **Example**

   .. code-block:: python

      from src.core.helpers import parse_hyperparameters_from_dict

      specs = {
          "lr":      {"val": (1e-4, 0.1), "default": 0.01, "log": True},
          "margin":  {"val": [0.6, 0.8, 1.0], "default": 1.0},
          "dropout": 0.5,
          "epochs":  (10, 100),
      }

      hps = parse_hyperparameters_from_dict(specs)
      # hps["lr"]      → UniformFloatHyperparameter (log-scale)
      # hps["margin"]  → CategoricalHyperparameter
      # hps["dropout"] → Constant(0.5)
      # hps["epochs"]  → UniformIntegerHyperparameter

   .. rubric:: Extended dict format

   The ``{"val": …}`` dict format gives you fine-grained control:

   .. code-block:: yaml

      # YAML equivalent used in AutoMAX config files
      optimizer_kwargs:
        lr:
          val: [0.0001, 0.1]
          default: 0.01
          log: true
        margin:
          val: [0.6, 0.8, 1.0]
          default: 1.0

   .. note::

      If both ``"log": true`` and a list-of-choices ``val`` are supplied,
      the ``log`` flag is silently ignored (categorical HPs have no
      log-scale concept).
