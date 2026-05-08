``src.auto_gnn``
================

Entry point for running AutoMAX hyperparameter search with a
:class:`~libauc.trainer.GNNTrainer` (graph neural network tasks).

**CLI usage**

.. code-block:: bash

   python -m src.auto_gnn --config_file config.yaml

This module mirrors :mod:`src.auto_trainer` but targets graph datasets and
uses LibAUC's :class:`~libauc.trainer.GNNTrainer`.  Key differences:

* The ``model:`` section uses GNN-specific keys (``emb_dim``, ``num_layers``, etc.).
* ``decay_factor`` is an additional training key for LR schedule scaling.
* Tasks are always treated as binary / single-label for sampler logic
  (``multilabel = False``).

.. rubric:: Functions

.. py:function:: main()

   Parse CLI arguments, load the GNN megaconf, build an
   :class:`~src.core.autopartial.autopartial` GNNTrainer, and run
   :meth:`~src.core.automax.AutoMAX.optimize`.

.. py:function:: apply_cli_overrides(cfg, args)

   Identical to :func:`src.auto_trainer.apply_cli_overrides`.

   :param cfg: Merged megaconf.
   :type cfg: OmegaConf DictConfig
   :param args: Parsed CLI arguments.
   :type args: argparse.Namespace
   :returns: The mutated config (same object).
   :rtype: OmegaConf DictConfig

.. py:function:: set_seed(seed)

   Identical to :func:`src.auto_trainer.set_seed`.

   :param seed: Seed value to apply.
   :type seed: int

.. rubric:: GNN megaconf defaults

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
     decay_factor: 10.0
     num_workers: 2
     output_path: ./output
     resume_from_checkpoint: true
     save_checkpoint_every: 5
     project_name: libauc
     experiment_name: run_auto_gnn
     verbose: 1

   automax:
     deterministic: true
     n_trials: 5
     n_configs: 1
     SEED: 42
     name: automax_gnn_search
     output_directory: ./automax_output
     overwrite: true

   dataset:
     name: ""
     kwargs: {}
     eval_splits: [val]

   model:
     name: gcn
     num_tasks: 1
     emb_dim: 256
     num_layers: 5

   metrics: [AUROC]
   metric_kwargs: []
