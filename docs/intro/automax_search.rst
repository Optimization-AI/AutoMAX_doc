AutoMAX Search
==============

AutoMAX uses `SMAC3 <https://github.com/automl/SMAC3>`_ — a Bayesian
optimization framework — to search over hyperparameter configurations for
your chosen loss/optimizer pair.

How It Works
------------

1. AutoMAX reads your config and builds a **configuration space** from 
   the predefined search space of the selected loss function.
2. It starts with the **default configuration** (via ``DefaultInitialDesign``)
   to establish a baseline.
3. SMAC3 proposes new configurations, trains a full model for each trial,
   and uses the returned target metric to guide the next suggestion.
4. After ``n_trials`` evaluations, the best configuration is saved to
   ``output_directory``.

Resuming a Search
-----------------

SMAC3 serializes the run history to disk. If a search is interrupted,
it can be resumed by re-running the same command — as long as
``output_directory`` and ``name`` remain unchanged and ``overwrite: false``.

.. code-block:: yaml

   automax:
     name: my_search
     output_directory: ./automax_output
     overwrite: false   # don't wipe previous trials

What Gets Tuned
---------------

AutoMAX tunes the loss and optimizer hyperparameters defined in each
loss function's search space. Common parameters across all pairs include:

- **lr** — learning rate (log-scale range)
- **epoch_decay** — learning rate decay factor
- **weight_decay** — L2 regularization
- **margin** — surrogate loss margin

Loss-specific parameters (e.g. ``beta``, ``eta``, ``gamma``, ``Lambda``,
``tau``) are included automatically when that loss is selected.

See :doc:`loss_optimizer_pairs` for the full list per loss function.

Output
------

After the search completes, results are written to ``output_directory/name/``:

.. code-block:: text

   automax_output/
   └── my_search/
       ├── runhistory.json  #
       ├── configspace.json  #
       ├── intensifier.json  #
       ├── optimization.json #
       └── scenario.json #
