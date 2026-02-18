LISA-AI: Active Noise Mitigation for Space-Based InterferometryProject OverviewThis repository implements a Multi-Agent Reinforcement Learning (MARL) framework designed for active noise mitigation in the Laser Interferometer Space Antenna (LISA). Laser frequency noise is traditionally the dominant noise source for space-based detectors; this project builds a "Digital Twin" to train AI agents to dynamically suppress residuals in the Time Delay Interferometry (TDI) processing layer.
1. Computational ArchitectureThe system follows a hierarchical control strategy to manage the three-spacecraft constellation:
Multi-Agent ControlLocal RL Agents: Each spacecraft runs an independent agent monitoring local states: 6-DOF test mass positions, laser phase fluctuations, and auxiliary thermal/magnetic sensors.Master Controller: A global coordination layer that processes the TDI X, Y, and Z observables to recognize global noise patterns across the 2.5 million km arms.+2Hybrid CNN-LSTM + Attention ControllerThe controller utilizes a multi-modal neural network designed for high-precision time-series data:CNN Branch: Extracts spectral features and pattern recognition from instrument spectrograms.
Dense Branch: Processes scalar telemetry (e.g., optical bench temperature, alignment).+2LSTM & Attention: A 128-unit LSTM with an 8-head Multi-Head Attention mechanism captures multi-scale temporal dependencies, tracking millihertz drifts and orbital perturbations.
2. Physics-Informed ImplementationUnlike standard RL, this agent is constrained by the underlying physics of the LISA mission:
Multi-Objective Reward Function
The agent is trained to maximize a reward signal composed of:
TDI Noise Minimization: Primary penalty on spectral power density in the $0.1\text{ mHz} - 1.0\text{ Hz}$ band.
HF Noise Avoidance: Prevents the injection of artifacts above $1\text{ Hz}$ that could interfere with high-frequency sensitivity.
Signal Integrity: Ensures the preservation of gravitational wave signal bands through injection-test correlation checks.
 Action SpaceThe agent commands a suite of high-precision actuators:Micro-Newton Thrusters: Force/torque commands for drag-free control.Laser Control: Real-time frequency adjustments and optical path length corrections.
3. Training & Validation StrategyThe project utilizes a Curriculum Learning approach to move from simplified noise models to a full LISA Digital Twin:
 Phase 1: Single noise source with perfect actuators.
 Phase 2: Correlated noise (Shot, Acceleration, Laser) with actuator saturation.
 Phase 3: Transfer Learning from LIGO-DeepClean architectures, fine-tuned for LISA-specific orbital dynamics.
4. Performance Metrics
Target Sensitivity Gain: $20\text{-}30\%$ SNR improvement in the primary science band.
Detection Volume: Estimated $30\text{-}50\%$ increase in detection range for galactic binaries and black hole mergers.Latency: Sub-second real-time inference for flight-software compatibility.
5. Conclusion & Future Outlook
This prototype demonstrates a Multi-Agent Reinforcement Learning approach to the LISA noise mitigation problem. By utilizing a hybrid CNN-LSTM architecture with Multi-Head Attention, the agent successfully processes high-dimensional spectral and scalar data to stabilize TDI observables.

Next Steps:

Hardware-in-the-loop (HIL) Testing: Transitioning from the Digital Twin to physical testbeds to validate real-time latency.

Transfer Learning: Fine-tuning the model using archival LIGO data to improve cross-platform robustness.

High-Fidelity Dynamics: Integrating full N-body gravitational perturbations for Phase 3 training.
