``src.core``
============

The ``src.core`` package exports all primary public symbols of AutoMAX.

.. code-block:: python

   from src.core import AutoMAX, AutoMAXConfigration, autopartial, parse_hyperparameters_from_dict

**Exported symbols**

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Symbol
     - Description
   * - :class:`~src.core.automax.AutoMAX`
     - Main HPO search orchestrator
   * - :class:`~src.core.automax_configration.AutoMAXConfigration`
     - Configuration dataclass for a search run
   * - :class:`~src.core.autopartial.autopartial`
     - ``functools.partial``-like wrapper that builds a ``ConfigurationSpace``
   * - :func:`~src.core.helpers.parse_hyperparameters_from_dict`
     - Converts raw dicts to ``ConfigSpace`` hyperparameter objects
