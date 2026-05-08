``AutoMAX``
===========

.. py:class:: AutoMAX(trainer, config, target)

   Automated AUC optimisation using SMAC3.

   Wraps a LibAUC :class:`~libauc.trainer.Trainer` with a SMAC3
   :class:`~smac.HyperparameterOptimizationFacade` to perform Bayesian
   hyperparameter search over the configuration space exposed by *trainer*.

   :param trainer: A callable (typically an :class:`~src.core.autopartial.autopartial`
       instance) that accepts a ``space`` argument and returns a
       :class:`~libauc.trainer.Trainer`.  The ``.cs`` attribute of the trainer
       is used as the SMAC3 configuration space.
   :type trainer: callable
   :param config: Run-level settings (number of trials, output directory, seed …).
   :type config: :class:`~src.core.automax_configration.AutoMAXConfigration`
   :param target: Name of the metric to maximise (e.g. ``"AUROC"``).
   :type target: str

   **Example**

   .. code-block:: python

      from src.core import AutoMAX, AutoMAXConfigration

      config = AutoMAXConfigration(
          name="my_search",
          n_trials=10,
          n_configs=1,
          SEED=42,
          output_directory="./automax_output",
          overwrite=True,
          deterministic=True,
      )

      tuner = AutoMAX(trainer=my_autopartial_trainer, config=config, target="AUROC")
      tuner.optimize()

   .. rubric:: Constructor details

   .. py:method:: __init__(trainer, config, target)

      Initialises the SMAC3 scenario and
      :class:`~smac.HyperparameterOptimizationFacade`.  If *config.overwrite*
      is ``False`` and a previous run exists, the trial log is restored from
      ``state.pkl``.

   .. rubric:: Methods

   .. py:method:: train(space, seed=0) -> float

      Train one model with the hyperparameter configuration *space*.

      Called automatically by SMAC3 during optimisation; you rarely need to
      call this directly.

      :param space: A SMAC3 / ConfigSpace ``Configuration`` object.
      :param seed: Random seed for this trial (passed in by SMAC3).
      :type seed: int
      :returns: **Negative** validation score (SMAC3 minimises cost).
      :rtype: float

      After training the method:

      * Appends the trial summary to ``self.log``.
      * Persists ``self.log`` to ``<output_directory>/<name>/state.pkl``.
      * Copies the model checkpoint directory to ``<experiment_name>_best``
        whenever a new best score is found.

   .. py:method:: optimize() -> Configuration

      Run the full SMAC3 optimisation loop and print a trial-history table.

      Resumes any interrupted trials before calling
      :meth:`~smac.HyperparameterOptimizationFacade.optimize`.

      :returns: The incumbent (best) configuration found.
      :rtype: :class:`~ConfigSpace.Configuration`

      **Trial history table** — printed to stdout after optimisation:

      .. code-block:: text

         ----------------------------------------
         Trial    Val AUROC
         ----------------------------------------
         1        0.823456
         2        0.851234
         …
         ----------------------------------------

   .. rubric:: Attributes

   .. list-table::
      :header-rows: 1
      :widths: 25 75

      * - Attribute
        - Description
      * - ``configspace``
        - The :class:`~ConfigSpace.ConfigurationSpace` taken from *trainer*.
      * - ``trainer``
        - The wrapped trainer callable.
      * - ``target``
        - Metric name string (e.g. ``"AUROC"``).
      * - ``config``
        - The :class:`~src.core.automax_configration.AutoMAXConfigration` instance.
      * - ``smac``
        - The underlying :class:`~smac.HyperparameterOptimizationFacade` instance.
      * - ``log``
        - List of per-trial summary dicts (``val``, ``test``, ``space``, …).
      * - ``finished``
        - Number of completed trials at initialisation time.
      * - ``best_score``
        - Running best validation score (``float('-inf')`` at start).
