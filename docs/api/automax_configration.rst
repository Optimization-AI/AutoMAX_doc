``AutoMAXConfigration``
=======================

.. py:class:: AutoMAXConfigration(**kwargs)

   Configuration container for an AutoMAX hyperparameter-optimisation run.

   All arguments are keyword-only and are consumed via ``**kwargs``.
   Maps directly to the ``automax:`` section of the YAML config file.

   :param deterministic: Enforce deterministic behaviour across trials.
   :type deterministic: bool
   :param n_trials: Total number of HPO trials to run.
   :type n_trials: int
   :param n_configs: Number of configurations evaluated per trial.
   :type n_configs: int
   :param SEED: Random seed used by the SMAC3 sampler (default: ``0``).
   :type SEED: int
   :param name: Human-readable identifier for the search run.
   :type name: str
   :param output_directory: Directory where AutoMAX writes results
       (default: ``"./automax_output"``).
   :type output_directory: str
   :param overwrite: Overwrite an existing output directory with the same *name*.
   :type overwrite: bool

   **Example**

   .. code-block:: python

      from src.core import AutoMAXConfigration

      automax_cfg = AutoMAXConfigration(
          deterministic=True,
          n_trials=50,
          n_configs=10,
          SEED=0,
          name="my_search",
          output_directory="./automax_output",
          overwrite=False,
      )

   **YAML equivalent**

   .. code-block:: yaml

      automax:
        deterministic: true
        n_trials: 50
        n_configs: 10
        SEED: 0
        name: my_search
        output_directory: ./automax_output
        overwrite: false

   .. rubric:: Attributes

   .. list-table::
      :header-rows: 1
      :widths: 25 15 60

      * - Attribute
        - Type
        - Description
      * - ``deterministic``
        - bool
        - Enforce deterministic training across all trials.
      * - ``n_trials``
        - int
        - Total number of HPO trials to run.
      * - ``n_configs``
        - int
        - Configurations evaluated per trial.
      * - ``SEED``
        - int
        - Random seed for the SMAC3 sampler (default: ``0``).
      * - ``name``
        - str
        - Unique run identifier; also used as the SMAC3 scenario name.
      * - ``output_directory``
        - str
        - Root output directory (default: ``"./automax_output"``).
      * - ``overwrite``
        - bool
        - Whether to overwrite an existing run with the same *name*.
