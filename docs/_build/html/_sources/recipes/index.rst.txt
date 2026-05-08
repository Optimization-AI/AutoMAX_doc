Recipes
=======

Ready-to-use config files for common tasks, located in ``recipes/``.
Each recipe corresponds directly to a YAML file in the
`AutoMAX repository <https://github.com/Optimization-AI/AutoMAX/tree/main/recipes>`_.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Recipe
     - Loss / Optimizer
     - When to use
   * - :doc:`auroc`
     - ``AUCMLoss`` / ``PESG``
     - AUROC maximization — standard imbalanced binary classification
   * - :doc:`auprc`
     - ``APLoss`` / ``SOAP``
     - AUPRC / AP maximization — when precision-recall tradeoff matters
   * - :doc:`opauc`
     - ``pAUCLoss (1w)`` / ``SOPAs``
     - One-way pAUC — restrict FPR to a specific range
   * - :doc:`tpauc`
     - ``pAUCLoss (2w)`` / ``SOTAs``
     - Two-way pAUC — restrict both FPR and TPR ranges
   * - :doc:`tpauc_cvar`
     - ``tpAUC_CVaR_loss`` / ``STACO``
     - Two-way pAUC with CVaR surrogate — robust tail-aware optimization

.. toctree::
   :hidden:

   auroc
   auprc
   opauc
   tpauc
   tpauc_cvar
