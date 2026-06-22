<div align="center">
  <img src="assets/banner.svg" alt="Awesome Neural ODEs Banner">
</div>

# ✨ Awesome-Neural-Ordinary-Differential-Equations ✨
## 🚀 Neural Ordinary Differential Equations (Neural ODEs): Evolution, Variants, & Applications

<div align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>

<br/>

🧠 **Neural Ordinary Differential Equations (Neural ODEs)** redefine deep learning architectures by replacing discrete, stacked layers (like those in ResNets) with a continuous-time hidden state vector. Instead of updating features step-by-step ($h_{t+1} = h_t + f(h_t)), Neural ODEs parameterize the *derivative* of the hidden state using a neural network ($\frac{dh(t)}{dt} = f(h(t), t, \theta)). The final output is computed using standard, numerical ODE solvers, allowing networks to trade computation speed for mathematical precision dynamically.

---

## ⏳ 1. The Chronological Evolution

The progression of continuous-time deep learning maps a shift from standard discrete residual hopping to complex, boundary-constrained generative models.


`mermaid
flowchart LR
    A["Residual Networks (2015)<br/>(Discrete Layer Steps)"] ---> B["Neural ODEs (2018)<br/>(Continuous State Vector)"] 
    B ---> C["Continuous Normalizing Flows<br/>(Exact Density Estimation)"] 
    C ---> D["Neural CDEs / SDEs<br/>(Irregular / Noisy Streams)"]                       
`

| Evolution Stage | Concept | Year | Paper |
| :--- | :--- | :--- | :--- |
| **[The Residual Network Precursor (ResNets, 2015)](pages/resnets.md)** | Established the concept of shortcut connections. Researchers realized that as layer steps become infinitely thin, a ResNet mathematically approximates an Euler discretization of an ordinary differential equation. | 2015 | [Link](https://arxiv.org/abs/1512.03385) |
| **[The Neural ODE Breakthrough (Chen et al., 2018)](pages/neural_odes.md)** | Formally replaced discrete layers with a continuous vector field. Introduced the **Adjoint Sensitivity Method**, which allows backpropagation through standard black-box numerical ODE solvers with $O(1) memory complexity, bypassing the need to store intermediate activations. | 2018 | [Link](https://arxiv.org/abs/1806.07366) |
| **[Stochastic and Controlled Scaling (~2020–Present)](pages/stochastic_controlled.md)** | Expanded the mathematical framework to handle environmental noise (Neural SDEs) and continuous, incoming data streams (Neural Controlled Differential Equations). | 2020 | [Link](https://arxiv.org/abs/2005.08926) |

---

## 📐 2. Core Mathematical & Architectural Variants

These variations alter the underlying system of differential equations to make the neural network compatible with distinct physics laws or mathematical properties.

| Variant | Mechanism | Pros | Year | Paper |
| :--- | :--- | :--- | :--- | :--- |
| **[Continuous Normalizing Flows (CNF)](pages/cnf.md)** | A generative variant where the change in a data distribution's probability density is tracked over continuous time using the Instantaneous Change of Variables formula. | Computes exact log-likelihood values much faster than traditional discrete normalizing flows because it only requires tracking the trace of the Jacobian matrix. | 2018 | [Link](https://arxiv.org/abs/1806.07366) |
| **[Neural Controlled Differential Equations (Neural CDEs)](pages/neural_cdes.md)** | The continuous-time analogue to Recurrent Neural Networks (RNNs). The hidden state is driven by a continuous path constructed from irregularly sampled, incoming time-series data. | Naturally handles missing or unevenly spaced data observations without forcing artificial interpolation or zero-padding. | 2020 | [Link](https://arxiv.org/abs/2005.08926) |
| **[Neural Stochastic Differential Equations (Neural SDEs)](pages/neural_sdes.md)** | Inject a continuous Brownian motion (noise) term directly into the differential equation system: $dh(t) = f(h(t))dt + g(h(t))dW_t$. | Effectively models data distributions exhibiting high inherent uncertainty, serving as an ideal mathematical bridge to score-based diffusion networks. | 2019 | [Link](https://arxiv.org/abs/1905.09883) |
| **[Hamiltonian / Lagrangian Neural Networks](pages/hnn.md)** | Constrains the neural network's vector field to obey fundamental conservation laws of physics (like energy conservation) by modeling the system's kinetic and potential energies directly. | N/A | 2019 | [Link](https://arxiv.org/abs/1906.01563) |

---

## ⚙️ 3. Solver & Runtime Optimization Types

Because Neural ODEs evaluate a continuous system, their training and inference properties adapt dynamically based on the selection of numerical solvers.

| Solver Type | Behavior | Significance | Year | Paper |
| :--- | :--- | :--- | :--- | :--- |
| **[Adaptive Step-Size Solvers (Dormand-Prince / Runge-Kutta 45)](pages/adaptive_solvers.md)** | The solver automatically adjusts the thickness of its computation steps based on a user-defined error tolerance boundary. | Unlocks **Adaptive Computation**. The model can evaluate simple, clean inputs quickly with fewer steps, but automatically spends more computation steps on noisy, highly complex inputs. | 1980 | [Link](https://doi.org/10.1016/0771-050X(80)90013-3) |
| **[Fixed Step-Size Solvers (Euler / Midpoint Method)](pages/fixed_solvers.md)** | Forces the model to evaluate the vector field at unchanging, rigid intervals. | Eliminates runtime variance, ensuring predictable forward-pass latency in production deployments. | 1768 | [Link](https://en.wikipedia.org/wiki/Euler_method) |

---

## 🌍 4. Specialized Real-World Applications

| Application Area | Application Details | Year | Paper |
| :--- | :--- | :--- | :--- |
| **[Irregularly Sampled Medical Health Trackers](pages/health_trackers.md)** | Processes vital-sign streams from ICU patients, where heart rates and lab tests are logged at unpredictable, uneven intervals. Neural CDEs update patient health predictions continuously as time progresses. | 2019 | [Link](https://arxiv.org/abs/1907.03907) |
| **[Physical Dynamical Systems Forecasting](pages/physics_forecasting.md)** | Models complex, real-world physical systems—such as fluid dynamics, weather patterns, or celestial orbital trajectories—by embedding known differential physics formulas directly inside the network layer pipelines. | 2019 | [Link](https://arxiv.org/abs/1906.01563) |
| **[High-Fidelity Generative Flow Matching](pages/flow_matching.md)** | Serves as the mathematical basis for modern flow-matching and rectified-flow generative models, ensuring straight-line paths for extremely fast pixel generation loops. | 2022 | [Link](https://arxiv.org/abs/2210.02747) |

---

## 🌟 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Neural-Ordinary-Differential-Equations&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Neural-Ordinary-Differential-Equations&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Neural-Ordinary-Differential-Equations&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Neural-Ordinary-Differential-Equations&type=date&legend=bottom-right" />
</picture>
</a>
</div>
