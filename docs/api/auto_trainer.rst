``src.auto_trainer``
====================

Entry point for running AutoMAX hyperparameter search with a standard
LibAUC :class:`~libauc.trainer.Trainer` (image classification and similar tasks).

**CLI usage**

.. code-block:: bash

   python -m src.auto_trainer --config_file config.yaml

.. rubric:: Functions

.. py:function:: main()

   Parse CLI arguments, load the megaconf, build an
   :class:`~src.core.autopartial.autopartial` trainer, and run
   :meth:`~src.core.automax.AutoMAX.optimize`.

   Steps performed:

   1. Load YAML config and apply CLI overrides via :func:`apply_cli_overrides`.
   2. Set global random seeds via :func:`set_seed`.
   3. Load train / eval datasets with ``libauc.trainer.load_dataset``.
   4. Resolve default optimizer and loss configs from ``parse_defaultconfig``.
   5. Build an ``autopartial`` :class:`~libauc.trainer.TrainingArguments` that
      carries the search distributions.
   6. Construct an :class:`~src.core.automax_configration.AutoMAXConfigration`
      from the ``automax:`` config section.
   7. Build an ``autopartial`` :class:`~libauc.trainer.Trainer` and run
      :meth:`~src.core.automax.AutoMAX.optimize`.

.. py:function:: apply_cli_overrides(cfg, args)

   Merge CLI-supplied values into the megaconf in-place.

   :param cfg: Merged megaconf produced by ``_build_megaconf``.
   :type cfg: OmegaConf DictConfig
   :param args: Parsed CLI arguments from :mod:`argparse`.
   :type args: argparse.Namespace
   :returns: The mutated config (same object).
   :rtype: OmegaConf DictConfig

   The following CLI flags are supported:

   .. list-table::
      :header-rows: 1
      :widths: 35 65

      * - CLI flag
        - Config key overridden
      * - ``--epochs``
        - ``training.epochs``
      * - ``--batch_size``
        - ``training.batch_size``
      * - ``--eval_batch_size``
        - ``training.eval_batch_size``
      * - ``--sampling_rate``
        - ``training.sampling_rate``
      * - ``--num_workers``
        - ``training.num_workers``
      * - ``--output_path``
        - ``training.output_path``
      * - ``--seed``
        - ``training.SEED``
      * - ``--resume_from_checkpoint`` / ``--no-resume_from_checkpoint``
        - ``training.resume_from_checkpoint``
      * - ``--save_checkpoint_every``
        - ``training.save_checkpoint_every``

.. py:function:: set_seed(seed)

   Set all relevant random seeds for reproducibility.

   :param seed: Seed value to apply.
   :type seed: int

   Sets :mod:`numpy`, :mod:`torch` CPU, :mod:`torch` CUDA seeds, and enables
   ``torch.backends.cudnn.deterministic``.

.. rubric:: Megaconf defaults

``auto_trainer`` ships with the following built-in defaults, which are merged
*under* any user-supplied YAML:

.. code-block:: yaml

   training:
     optimizer: PESG
     optimizer_kwargs: {}
     loss: AUCMLoss
     loss_kwargs: {}
     SEED: 42
     batch_size: 128
     eval_batch_size: 128
     sampling_rate: 0.5
     epochs: 50
     decay_epochs: []
     num_workers: 2
     output_path: ./output
     resume_from_checkpoint: true
     save_checkpoint_every: 5
     project_name: libauc
     experiment_name: run_auto
     verbose: 1

   automax:
     deterministic: true
     n_trials: 5
     n_configs: 1
     SEED: 42
     name: automax_search
     output_directory: ./automax_output
     overwrite: true

   dataset:
     name: ""
     kwargs: {}
     eval_splits: [val]

   model:
     name: resnet18
     pretrained: false
     num_classes: 1
     in_channels: 3

   metrics: [AUROC]
   metric_kwargs: []
