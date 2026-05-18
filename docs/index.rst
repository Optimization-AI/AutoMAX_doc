.. AutoMAX documentation master file

:github_url: https://github.com/Optimization-AI/AutoMAX

AutoMAX
=======

An Automated Hyperparameter Optimization Framework for AUC-based Metrics
================================================================================================================================

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <p align="center">
   <a href="https://github.com/Optimization-AI/AutoMAX">
   <img src="https://img.shields.io/badge/python-3.10-blue?style=flat" alt="Python 3.10"></a>

   <a href="https://github.com/Optimization-AI/AutoMAX">
   <img src="https://img.shields.io/badge/PyTorch-2.0+-orange?style=flat" alt="PyTorch"></a>

   <a href="https://github.com/Optimization-AI/AutoMAX">
   <img src="https://img.shields.io/badge/SMAC3-powered-7c6dff?style=flat" alt="SMAC3"></a>
   </p>


================================================================================================================================
Why AutoMAX?
================================================================================================================================

**AutoMAX** is an automated hyperparameter optimization framework for AUC-based metrics, built on top of `LibAUC <https://github.com/Optimization-AI/LibAUC>`_ and `SMAC3 <https://github.com/automl/SMAC3>`_.

Instead of manually sweeping learning rates, margins, and decay schedules, AutoMAX runs a Bayesian search over the predefined hyperparameter spaces for each supported loss/optimizer pair — then returns the best configuration for your dataset.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :glob:
   :maxdepth: 1
   :caption: Get Started

   Quick Start <intro/quickstart>
   Installation <intro/installation>
   Configuration <intro/configuration>

.. toctree::
   :glob:
   :maxdepth: 1
   :caption: AutoMAX Search

   AutoMAX Search <intro/automax_search>
   Loss-Optimizer Pairs <intro/loss_optimizer_pairs>
   Hyperparameter Format <intro/hyperparameter_format>
   CLI Overrides <intro/cli_overrides>

.. toctree::
   :glob:
   :maxdepth: 1
   :caption: API Reference

   api/index

.. toctree::
   :glob:
   :maxdepth: 2
   :caption: Recipes

   recipes/index


