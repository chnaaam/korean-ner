import torch.nn as nn

class OutputLayer(nn.Module):
    def __init__(self, layer, parameters):
        super(OutputLayer, self).__init__()

        self.output_layer = layer(parameters)

    def __str__(self):
        return f"Output Layer Name : {self.output_layer}"

    def forward(self, features, parameters):
        return self.output_layer(features, parameters)