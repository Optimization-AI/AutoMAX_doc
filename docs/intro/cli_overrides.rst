CLI Overrides
=============

The following ``training`` fields can be overridden directly on the command
line. CLI values always take precedence over the config file.

.. code-block:: bash

   python -m src.ui.auto_trainer \
     --config_file config.yaml \
     --epochs 50 \
     --seed 0 \
     --output_path ./runs

Reference
---------

.. list-table::
   :header-rows: 1
   :widths: 35 35 30

   * - CLI flag
     - Config field
     - Type
   * - ``--epochs``
     - ``training.epochs``
     - int
   * - ``--batch_size``
     - ``training.batch_size``
     - int
   * - ``--eval_batch_size``
     - ``training.eval_batch_size``
     - int
   * - ``--sampling_rate``
     - ``training.sampling_rate``
     - float
   * - ``--num_workers``
     - ``training.num_workers``
     - int
   * - ``--output_path``
     - ``training.output_path``
     - string
   * - ``--seed``
     - ``training.SEED``
     - int
   * - ``--resume`` / ``--no-resume``
     - ``training.resume_from_checkpoint``
     - bool
   * - ``--save_checkpoint_every``
     - ``training.save_checkpoint_every``
     - int
