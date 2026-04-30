.. AutoMAX documentation master file

AutoMAX
=======

.. image:: https://img.shields.io/badge/python-3.10-blue?style=flat
   :alt: Python 3.10

.. image:: https://img.shields.io/badge/PyTorch-2.0+-orange?style=flat
   :alt: PyTorch

.. image:: https://img.shields.io/badge/SMAC3-powered-7c6dff?style=flat
   :alt: SMAC3

|

**AutoMAX** is an automated hyperparameter optimization framework for
AUC-based metrics, built on top of `LibAUC <https://github.com/Optimization-AI/LibAUC>`_
and `SMAC3 <https://github.com/automl/SMAC3>`_.

Instead of manually sweeping learning rates, margins, and decay schedules,
AutoMAX runs a Bayesian search over the predefined hyperparameter spaces for
each supported loss/optimizer pair — then returns the best configuration
for your dataset.

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 🚀 Quick Start
      :link: intro/quickstart
      :link-type: doc

      Install AutoMAX and run your first AutoTune in minutes.

   .. grid-item-card:: ⚙️ Configuration
      :link: intro/configuration
      :link-type: doc

      Full reference for the YAML config file — all five sections.

   .. grid-item-card:: 🔍 AutoMAX Search
      :link: intro/automax_search
      :link-type: doc

      How the SMAC3-based search works and what it tunes.

   .. grid-item-card:: 📋 Recipes
      :link: recipes/index
      :link-type: doc

      Ready-to-use configs for AUROC, AUPRC, pAUC, and more.

----

.. toctree::
   :maxdepth: 1
   :caption: Get Started

   intro/quickstart
   intro/installation
   intro/configuration

.. toctree::
   :maxdepth: 1
   :caption: AutoMAX Search

   intro/automax_search
   intro/loss_optimizer_pairs
   intro/hyperparameter_format
   intro/cli_overrides

.. toctree::
   :maxdepth: 2
   :caption: Recipes

   recipes/index

.. toctree::
   :maxdepth: 1
   :caption: Reference

   api/index
