import os

os.makedirs('pages', exist_ok=True)

files = {
    'resnets.md': '# The Residual Network Precursor (ResNets, 2015)\n\n## Overview\nResidual Networks (ResNets) introduced the concept of shortcut connections. This allowed training of much deeper networks by bypassing some layers.\n\n## Mathematical Formulation\nInstead of learning the underlying mapping (x)$, ResNets learn the residual mapping (x) = H(x) - x$. The update step looks like:\nh_{t+1} = h_t + f(h_t, \\theta_t)\nThis discrete update formula mathematically resembles the Euler method for solving ODEs.\n\n## Diagram\n`mermaid\nflowchart TD\n    A[Input $] --> B[Weight Layer]\n    B --> C[ReLU]\n    C --> D[Weight Layer]\n    A --> E((+))\n    D --> E\n    E --> F[ReLU]\n    F --> G[Output]\n`\n',
    'neural_odes.md': '# The Neural ODE Breakthrough (Chen et al., 2018)\n\n## Overview\nNeural Ordinary Differential Equations (Neural ODEs) define the hidden state dynamics using an ODE specified by a neural network.\n\n## Mathematical Formulation\n\\frac{dh(t)}{dt} = f(h(t), t, \\theta)\nThis allows for continuous-depth networks. The Adjoint Sensitivity Method calculates gradients without storing intermediate activations, requiring only (1)$ memory.\n\n## Diagram\n`mermaid\nflowchart LR\n    A[Input (0)$] --> B{ODE Solver}\n    B -- continuous evaluation --> C[Output (T)$]\n    B -.-> D[f(h, t)]\n`\n',
    'stochastic_controlled.md': '# Stochastic and Controlled Scaling (~2020–Present)\n\n## Overview\nBuilding upon Neural ODEs, researchers expanded the continuous-time framework to incorporate environmental noise (SDEs) and continuous streams of data (CDEs).\n\n## Framework\n- **Neural SDEs**: Incorporate a diffusion term for noise.\n- **Neural CDEs**: Use an integral with respect to a continuous path constructed from data.\n\n## Diagram\n`mermaid\nflowchart TD\n    A[Neural ODEs] --> B[Neural CDEs]\n    A --> C[Neural SDEs]\n    B --> D[Irregular Data Streams]\n    C --> E[Stochastic Uncertainty]\n`\n',
    'cnf.md': '# Continuous Normalizing Flows (CNF)\n\n## Overview\nCNFs are generative models where the continuous evolution of a data distribution is governed by an ODE.\n\n## Mathematical Formulation\nUsing the Instantaneous Change of Variables formula, the log-likelihood can be computed efficiently:\n\\frac{\\partial \\log p(z(t))}{\\partial t} = - \\text{Tr} \\left( \\frac{\\partial f}{\\partial z} \\right)\n\n## Diagram\n`mermaid\nflowchart LR\n    A[Simple Distribution] -->|ODE Flow| B[Complex Data Distribution]\n`\n',
    'neural_cdes.md': '# Neural Controlled Differential Equations (Neural CDEs)\n\n## Overview\nNeural CDEs extend Neural ODEs to handle irregular time-series data seamlessly, serving as continuous-time RNNs.\n\n## Mechanism\nA continuous path (t)$ is interpolated from discrete observations, and the hidden state evolves according to:\ndh(t) = f(h(t), \\theta) dX(t)\n\n## Diagram\n`mermaid\nflowchart TD\n    A[Irregular Time Series] --> B[Continuous Path (t)$]\n    B --> C[Neural CDE System]\n    C --> D[Hidden State Evolution]\n`\n',
    'neural_sdes.md': '# Neural Stochastic Differential Equations (Neural SDEs)\n\n## Overview\nNeural SDEs incorporate Brownian motion directly into the differential equations, capturing uncertainty and complex noise patterns.\n\n## Mechanism\ndh(t) = f(h(t))dt + g(h(t))dW_t\n\n## Diagram\n`mermaid\nflowchart TD\n    A[Current State] --> B{Drift Network $}\n    A --> C{Diffusion Network $}\n    C --> D((Noise $))\n    B --> E[Update State]\n    D --> E\n`\n',
    'hnn.md': '# Hamiltonian / Lagrangian Neural Networks\n\n## Overview\nThese networks embed physics priors directly into the architecture by modeling the Hamiltonian (energy) or Lagrangian of the system.\n\n## Mechanism\nThis guarantees that energy conservation and other physical laws are respected.\n\n## Diagram\n`mermaid\nflowchart LR\n    A[Position/Momentum] --> B[HNN]\n    B --> C[Energy Gradient]\n    C --> D[Conservative Dynamics]\n`\n',
    'adaptive_solvers.md': '# Adaptive Step-Size Solvers\n\n## Overview\nAdaptive step-size solvers (e.g., Dormand-Prince, Runge-Kutta 45) dynamically change the step size based on estimated error.\n\n## Significance\nThey allow for faster computation in smooth regions and precise computation in complex regions.\n\n## Diagram\n`mermaid\nflowchart TD\n    A[Evaluate Step] --> B{Error < Tolerance?}\n    B -- Yes --> C[Accept Step & Increase Size]\n    B -- No --> D[Reject Step & Decrease Size]\n`\n',
    'fixed_solvers.md': '# Fixed Step-Size Solvers\n\n## Overview\nMethods like Euler or Midpoint method use a constant $\\Delta t$.\n\n## Significance\nThey guarantee predictable execution time, crucial for real-time systems and production.\n\n## Diagram\n`mermaid\nflowchart LR\n    A[t=0] -->|$\\Delta t$| B[t=1]\n    B -->|$\\Delta t$| C[t=2]\n    C -->|$\\Delta t$| D[t=3]\n`\n',
    'health_trackers.md': '# Irregularly Sampled Medical Health Trackers\n\n## Application\nMedical data is often irregularly sampled. Neural CDEs excel at processing vital signs and lab results without imputation.\n\n## Diagram\n`mermaid\ngantt\n    title Irregular Medical Data\n    dateFormat X\n    axisFormat %s\n    section Vital Signs\n    Heart Rate : 0, 1\n    Blood Pressure : 3, 4\n    Temp : 8, 9\n`\n',
    'physics_forecasting.md': '# Physical Dynamical Systems Forecasting\n\n## Application\nModels real-world systems like weather or orbits by embedding differential physics inside the network.\n\n## Diagram\n`mermaid\nflowchart TD\n    A[Initial State] --> B[Neural Network]\n    B --> C[Physical Constraints]\n    C --> D[Future State Prediction]\n`\n',
    'flow_matching.md': '# High-Fidelity Generative Flow Matching\n\n## Application\nA framework for training continuous normalizing flows without simulation, allowing straight-line probability paths and highly efficient image generation.\n\n## Diagram\n`mermaid\nflowchart LR\n    A[Noise] -->|Straight Line Path| B[Image]\n`\n'
}

for name, content in files.items():
    with open(f'pages/{name}', 'w', encoding='utf-8') as f:
        f.write(content)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

replacements = {
    '**The Residual Network Precursor (ResNets, 2015)**': '**[The Residual Network Precursor (ResNets, 2015)](pages/resnets.md)**',
    '**The Neural ODE Breakthrough (Chen et al., 2018)**': '**[The Neural ODE Breakthrough (Chen et al., 2018)](pages/neural_odes.md)**',
    '**Stochastic and Controlled Scaling (~2020–Present)**': '**[Stochastic and Controlled Scaling (~2020–Present)](pages/stochastic_controlled.md)**',
    '**Continuous Normalizing Flows (CNF)**': '**[Continuous Normalizing Flows (CNF)](pages/cnf.md)**',
    '**Neural Controlled Differential Equations (Neural CDEs)**': '**[Neural Controlled Differential Equations (Neural CDEs)](pages/neural_cdes.md)**',
    '**Neural Stochastic Differential Equations (Neural SDEs)**': '**[Neural Stochastic Differential Equations (Neural SDEs)](pages/neural_sdes.md)**',
    '**Hamiltonian / Lagrangian Neural Networks**': '**[Hamiltonian / Lagrangian Neural Networks](pages/hnn.md)**',
    '**Adaptive Step-Size Solvers (Dormand-Prince / Runge-Kutta 45)**': '**[Adaptive Step-Size Solvers (Dormand-Prince / Runge-Kutta 45)](pages/adaptive_solvers.md)**',
    '**Fixed Step-Size Solvers (Euler / Midpoint Method)**': '**[Fixed Step-Size Solvers (Euler / Midpoint Method)](pages/fixed_solvers.md)**',
    '**Irregularly Sampled Medical Health Trackers**': '**[Irregularly Sampled Medical Health Trackers](pages/health_trackers.md)**',
    '**Physical Dynamical Systems Forecasting**': '**[Physical Dynamical Systems Forecasting](pages/physics_forecasting.md)**',
    '**High-Fidelity Generative Flow Matching**': '**[High-Fidelity Generative Flow Matching](pages/flow_matching.md)**'
}

for old, new in replacements.items():
    readme = readme.replace(old, new)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
