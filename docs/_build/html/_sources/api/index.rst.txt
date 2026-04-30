API Reference
=============

.. note::

   Full API autodoc requires the AutoMAX source to be installed as a package.
   The entries below document the public interfaces.

Core
----

.. rubric:: ``AutoMAX``

The main search orchestrator. Wraps a LibAUC ``Trainer`` with a SMAC3
``HyperparameterOptimizationFacade``.

.. code-block:: python

   from src.core import AutoMAX, AutoMAXConfigration

   config = AutoMAXConfigration(
       name="my_search",
       n_trials=10,
       output_directory="./automax_output",
   )
   searcher = AutoMAX(trainer=trainer_fn, config=config, target="AUROC")
   searcher.run()

.. rubric:: ``AutoMAXConfigration``

Dataclass holding search settings. Maps directly to the ``automax:`` section
of the YAML config.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Attribute
     - Type
     - Description
   * - ``name``
     - str
     - Unique run identifier
   * - ``n_trials``
     - int
     - Number of configurations to evaluate (default: ``5``)
   * - ``SEED``
     - int
     - Random seed for the sampler (default: ``42``)
   * - ``deterministic``
     - bool
     - Enforce deterministic training across trials (default: ``True``)
   * - ``output_directory``
     - str
     - Output directory for results (default: ``./automax_output``)
   * - ``overwrite``
     - bool
     - Overwrite existing run with same name (default: ``True``)
