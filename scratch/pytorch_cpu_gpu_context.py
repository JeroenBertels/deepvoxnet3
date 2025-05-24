import torch

# List devices (PyTorch assumes GPU if available)
print("CUDA available:", torch.cuda.is_available())
print("Device count:", torch.cuda.device_count())

# Create tensor on CPU
x = torch.tensor([1.0, 2.0, 3.0], device='cpu')
print("CPU?: x device:", x.device)

# Use x in GPU context
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

print("GPU?: x device (still on CPU):", x.device)
x_ = x
print("GPU?: x_ device:", x_.device)

# Compute on GPU
y = x.to(device) * 2
print("GPU?: y device:", y.device)

# Create a new mutable version of x on GPU
x__ = x.to(device)
print("GPU?: x__ device:", x__.device)

x__[0] = 9  # In-place modification is allowed in PyTorch
print("Modified x__[0] = 9")

# Print final results
print("Final CPU x:", x)
print("GPU x_ (same as x):", x_)
print("GPU y:", y)
print("GPU x__:", x__)
