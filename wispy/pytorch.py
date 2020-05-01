"""
Helpful tools for Pytorch
"""
import torch
import torch.nn as nn
from torchvision.datasets import MNIST

# Dataset Classes -------------------------------------------------------------
class FastMNIST(MNIST):
    """
    A faster Dataset class for MNIST

    I copied this from:
    https://gist.github.com/y0ast/f69966e308e549f013a92dc66debeeb4
    """
    def __init__(self, device=torch.device("cpu"), normalize=False, *args, **kwargs):
        """Instantiate an object"""
        super().__init__(*args, **kwargs)

        # Scale data to [0,1]
        self.data = self.data.unsqueeze(1).float().div(255)

        # Normalize it with the usual MNIST mean and std
        if normalize:
            self.data = self.data.sub_(0.1307).div_(0.3081)

        # Put both data and targets on GPU in advance
        self.data, self.targets = self.data.to(device), self.targets.to(device)

    def __getitem__(self, index):
        """
        Return an example

        Parameters
        ----------
        index : int
            The index to return

        Returns
        -------
        tuple : tuple(torch.Tensor)
            Returns a tuple of (image, target) where target is index of
            the target class.
        """
        img, target = self.data[index], self.targets[index]
        return img, target


# Model Classes ---------------------------------------------------------------
class MLP(nn.Module):
    """
    Create a multilayer perceptron model with variable hidden layers.
    The network will have the specified number of layers and neurons,
    with each layer using the leaky ReLU activation function. 

    Parameters
    ----------
    input_dim : int
        The number of input features.

    hidden_dims : list of int
        The number of neurons in each hidden layer. Each element
        specifies a new hidden layer.
    """
    def __init__(self, input_dim, hidden_dims, output_dim, leaky_relu_slope=0.2,
                 batchnorm=False):
        """Instantiate an MLP object"""
        super(MLP, self).__init__()
        layers = hidden_dims

        if not input_dim or not isinstance(input_dim, int):
            raise ValueError("'input_dim' must be a non-zero integer.")

        if isinstance(layers, int):
            layers = [layers]

        if not all(layers) or not all(isinstance(l, int) for l in layers):
            raise ValueError("'hidden_dims' must be a list of non-zero "
                             "integers.")

        layers = list(layers)
        in_layers = [input_dim] + layers
        out_layers = layers + [output_dim]
        for idx, in_layer in enumerate(in_layers):
            self.add_module("linear_{}".format(idx),
                            nn.Linear(in_layer, out_layers[idx]))

            # Don't add leaky ReLU to output layer:
            if idx < len(in_layers) - 1:
                self.add_module("leakyReLU_{}".format(idx),
                                nn.LeakyReLU(negative_slope=leaky_relu_slope))

                if batchnorm:
                    self.add_module("BatchNorm_{}".format(idx),
                                    nn.BatchNorm1d(out_layers[idx]))


    def forward(self, x):
        """
        Run an example through the model

        Parameters
        ----------
        x : torch.Tensor
            A tensor to run through the model.

        Returns
        -------
        torch.Tensor
            The model predictions.
        """
        for idx, layer in enumerate(self._modules.values()):
            if idx < len(self._modules)-1:
                x = layer(x)
            else:
                return layer(x)

# Functions -------------------------------------------------------------------
def count_params(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
